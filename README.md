# Introduction 
This repo contains the demo code for License Plate Recognition using PaddleOCR.
Google Colab is used for this demonstration.

# Code Structure/Explanation
1.	[Setup on Google Colab](/Setup.ipynb)
2.	[HMean Calculation for Text Detection & Spotting Tasks](/Detection_Evaluation/HMean.ipynb)
3.	[Accuracy & Edit Distance Calculation for Text Recognition Task](/Detection_Evaluation/HMean.ipynb)
4.	[Data Exploration for the CCPD 2019 dataset](/License_Plate_Recognition/CCPD_2019.ipynb)
5.	[Text Detection, Recognition & Spotting on the CCPD 2019 dataset](/License_Plate_Recognition/EAST_CRNN_LPR.ipynb)

# Takeaway
1.	You will learn how the HMean is calculated for the text detection and text spotting tasks with detailed examples.
2.	You will learn how the accuracy, number of correctly recognized words, and total edit distance are calculated for the text recognition task.
3.	You will learn how to make use of the CCPD 2019, a commonly used license plate recognition dataset. Convert the dataset to PaddleOCR format and fine-tune text detection (EAST) and recognition methods (CRNN) on it. Then, compare the results of using pre-trained and fine-tuned checkpoints using the evaluation methods mentioned above.

# Credits
1.	[CCPD 2019 dataset](https://github.com/detectRecog/CCPD)
2.	[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
