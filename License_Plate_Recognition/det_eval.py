from collections import namedtuple
import numpy as np
import Polygon as plg
from typing import Dict, List


def evaluation(gt_dict: Dict[str, List], det_dict: Dict[str, List], eval_config: Dict):
    """Evaluate the prediction results in terms of precision, recall and HMean.
    The matching between ground-truth and predicted bounding box is based on the order in the list.
    In other words, a ground-truth box will match with the first predicted bounding box with IoU > IOU_CONSTRAINT.

    Args:
        gt_dict (Dict[str, list]): A dictionary with image id as the key and a list of its ground-truth
         bounding boxes as the value.
         e.g.: gt_dict = {'img1': [[20, 20, 120, 60, "Hello"],
                                 [200, 100, 300, 140, "World"],
                                 [80, 180, 180, 220, "###"]]}
        det_dict (Dict[str, list]): A dictionary with image id as the key and a list of its predicted
         bounding boxes as the value.
         e.g.: det_dict = {'img1': [[105, 40, 205, 80, "Hello"],
                                  [210, 105, 310, 145, "World"],
                                  [70, 170, 170, 210, "Random"]]}
        eval_config (dict): A dictionary storing the evaluation configuration.
         e.g.: eval_config = {"IOU_CONSTRAINT": 0.5,
                            "AREA_PRECISION_CONSTRAINT": 0.5,
                            "WORD_SPOTTING": True,
                        }
    Returns:
        resDict (Dict): A dict storing overall and per-sample evaluation result
    """

    def rectangle_to_polygon(rect):
        resBoxes = np.empty([1, 8], dtype="int32")
        resBoxes[0, 0] = int(rect.xmin)
        resBoxes[0, 4] = int(rect.ymax)
        resBoxes[0, 1] = int(rect.xmin)
        resBoxes[0, 5] = int(rect.ymin)
        resBoxes[0, 2] = int(rect.xmax)
        resBoxes[0, 6] = int(rect.ymin)
        resBoxes[0, 3] = int(rect.xmax)
        resBoxes[0, 7] = int(rect.ymax)

        pointMat = resBoxes[0].reshape([2, 4]).T

        return plg.Polygon(pointMat)

    def get_union(pD, pG):
        areaA = pD.area()
        areaB = pG.area()
        return areaA + areaB - get_intersection(pD, pG)

    def get_intersection_over_union(pD, pG):
        try:
            return get_intersection(pD, pG) / get_union(pD, pG)
        except:
            return 0

    def get_intersection(pD, pG):
        pInt = pD & pG
        if len(pInt) == 0:
            return 0
        return pInt.area()

    perSampleMetrics = {}
    matchedSum = 0
    Rectangle = namedtuple("Rectangle", "xmin ymin xmax ymax")
    numGlobalCareGt = 0
    numGlobalCareDet = 0

    # loop through each image id
    for gt_key, gt_val in gt_dict.items():
        recall = 0
        precision = 0
        hmean = 0
        detMatched = 0
        iouMat = np.empty([1, 1])

        gtPols = []
        detPols = []
        gtPolPoints = []
        detPolPoints = []
        # Array of Ground Truth Polygons' keys marked as don't Care
        gtDontCarePolsNum = []
        # Array of Detected Polygons' matched with a don't Care GT
        detDontCarePolsNum = []
        pairs = []
        detMatchedNums = []
        if eval_config["WORD_SPOTTING"]:
            gtTrans = []
            detTrans = []

        evaluationLog = ""

        # loop through all bounding boxes in an image
        for n in range(len(gt_val)):
            list_entry = gt_val[n]

            if eval_config["WORD_SPOTTING"]:
                # append ground-truth transcript
                gtTrans.append(list_entry[-1])

            points = list_entry[:4]
            transcription = list_entry[4]
            gtRect = Rectangle(*points)
            gtPol = rectangle_to_polygon(gtRect)

            gtPols.append(gtPol)
            gtPolPoints.append(points)
            if transcription == "###":
                gtDontCarePolsNum.append(len(gtPols) - 1)

        evaluationLog += (
            "GT polygons: "
            + str(len(gtPols))
            + (
                " (" + str(len(gtDontCarePolsNum)) + " don't care)\n"
                if len(gtDontCarePolsNum) > 0
                else "\n"
            )
        )

        # if there's bounding box in prediction
        if gt_key in det_dict.keys():
            det_val = det_dict[gt_key]
            for n in range(len(det_val)):
                points = det_val[n][:4]
                if eval_config["WORD_SPOTTING"]:
                    detTrans.append(det_val[n][-1])

                detRect = Rectangle(*points)
                detPol = rectangle_to_polygon(detRect)

                detPols.append(detPol)
                detPolPoints.append(points)
                # if there's 'dont care' boxes in ground-truth
                if len(gtDontCarePolsNum) > 0:
                    # we only care about the predicted bounding box
                    for dontCarePol in gtDontCarePolsNum:
                        dontCarePol = gtPols[dontCarePol]
                        intersected_area = get_intersection(dontCarePol, detPol)
                        pdDimensions = detPol.area()
                        precision = (
                            0 if pdDimensions == 0 else intersected_area / pdDimensions
                        )
                        if precision > eval_config["AREA_PRECISION_CONSTRAINT"]:
                            detDontCarePolsNum.append(len(detPols) - 1)
                            break

            evaluationLog += (
                "DET polygons: "
                + str(len(detPols))
                + (
                    " (" + str(len(detDontCarePolsNum)) + " don't care)\n"
                    if len(detDontCarePolsNum) > 0
                    else "\n"
                )
            )

            if len(gtPols) > 0 and len(detPols) > 0:
                # Calculate IoU and precision matrixs
                outputShape = [len(gtPols), len(detPols)]
                iouMat = np.empty(outputShape)
                gtRectMat = np.zeros(len(gtPols), np.int8)
                detRectMat = np.zeros(len(detPols), np.int8)
                for gtNum in range(len(gtPols)):
                    for detNum in range(len(detPols)):
                        pG = gtPols[gtNum]
                        pD = detPols[detNum]
                        iouMat[gtNum, detNum] = get_intersection_over_union(pD, pG)

                for gtNum in range(len(gtPols)):
                    for detNum in range(len(detPols)):
                        if (
                            gtRectMat[gtNum] == 0
                            and detRectMat[detNum] == 0
                            and gtNum not in gtDontCarePolsNum
                            and detNum not in detDontCarePolsNum
                        ):
                            if iouMat[gtNum, detNum] > eval_config["IOU_CONSTRAINT"]:
                                gtRectMat[gtNum] = 1
                                detRectMat[detNum] = 1
                                if eval_config["WORD_SPOTTING"]:
                                    correct = (
                                        gtTrans[gtNum].upper()
                                        == detTrans[detNum].upper()
                                    )
                                    if correct:
                                        detMatched += 1
                                        pairs.append(
                                            {
                                                "gt": gtNum,
                                                "det": detNum,
                                                "correct": correct,
                                            }
                                        )
                                        detMatchedNums.append(detNum)
                                        evaluationLog += (
                                            "Match GT #"
                                            + str(gtNum)
                                            + " with Det #"
                                            + str(detNum)
                                            + " trans. correct: "
                                            + str(correct)
                                            + "\n"
                                        )
                                else:
                                    detMatched += 1
                                    pairs.append({"gt": gtNum, "det": detNum})
                                    detMatchedNums.append(detNum)
                                    evaluationLog += (
                                        "Match GT #"
                                        + str(gtNum)
                                        + " with Det #"
                                        + str(detNum)
                                        + "\n"
                                    )

            numGtCare = len(gtPols) - len(gtDontCarePolsNum)
            # print(len(gtPols), len(gtDontCarePolsNum))
            numDetCare = len(detPols) - len(detDontCarePolsNum)
            # print(len(detPols), len(detDontCarePolsNum))
            if numGtCare == 0:
                recall = float(1)
                precision = float(0) if numDetCare > 0 else float(1)
            else:
                recall = float(detMatched) / numGtCare
                precision = 0 if numDetCare == 0 else float(detMatched) / numDetCare

            hmean = (
                0
                if (precision + recall) == 0
                else 2.0 * precision * recall / (precision + recall)
            )

            matchedSum += detMatched
            numGlobalCareGt += numGtCare
            numGlobalCareDet += numDetCare

            perSampleMetrics[gt_key] = {
                "precision": precision,
                "recall": recall,
                "hmean": hmean,
                "pairs": pairs,
                "iouMat": [] if len(detPols) > 100 else iouMat.tolist(),
                "gtPolPoints": gtPolPoints,
                "detPolPoints": detPolPoints,
                "gtDontCare": gtDontCarePolsNum,
                "detDontCare": detDontCarePolsNum,
                "eval_config": eval_config,
                "evaluationLog": evaluationLog,
            }

            if eval_config["WORD_SPOTTING"]:
                perSampleMetrics[gt_key]["gtTrans"] = gtTrans
                perSampleMetrics[gt_key]["detTrans"] = detTrans

    methodRecall = 0 if numGlobalCareGt == 0 else float(matchedSum) / numGlobalCareGt
    methodPrecision = (
        0 if numGlobalCareDet == 0 else float(matchedSum) / numGlobalCareDet
    )
    methodHmean = (
        0
        if methodRecall + methodPrecision == 0
        else 2 * methodRecall * methodPrecision / (methodRecall + methodPrecision)
    )

    methodMetrics = {
        "precision": methodPrecision,
        "recall": methodRecall,
        "hmean": methodHmean,
    }

    resDict = {
        "calculated": True,
        "Message": "",
        "method": methodMetrics,
        "per_sample": perSampleMetrics,
    }

    return resDict
