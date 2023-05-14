from Levenshtein import distance
from typing import List


def total_edit_distance(gt: List[str], pred: List[str]):
    """Calculate the total edit distance to convert all predictions into respective ground-truths.
    Edit distance for case sensitive and case insensitive are computed.

    Args:
        gt (List[str]): List of ground-truth text
        pred (List[str]): List of predicted text

    Returns:
        total_edit_distance (int): Total edit distance (case-sensitive)
        total_edit_distance_case_insensitive (int): Total edit distance (case-insensitive)
    """
    total_edit_distance = 0
    total_edit_distance_case_insensitive = 0
    for x, y in zip(gt, pred):
        total_edit_distance += distance(x, y)
        total_edit_distance_case_insensitive += distance(x.upper(), y.upper())
    return total_edit_distance, total_edit_distance_case_insensitive


def total_accuracy(gt: List[str], pred: List[str]):
    """Calculate the total correct prediction.
    Both case sensitive and case insensitive evaluation are computed.

    Args:
        gt (List[str]): List of ground-truth text
        pred (List[str]): List of predicted text

    Returns:
        total_crw (int): Total number of correctly predicted text (case-sensitive)
        total_crw_case_insensitive (int):Total number of correctly predicted text (case-insensitive)
    """
    total_crw = 0
    total_crw_case_insensitive = 0
    for x, y in zip(gt, pred):
        if x == y:
            total_crw += 1
        if x.upper() == y.upper():
            total_crw_case_insensitive += 1
    return total_crw, total_crw_case_insensitive
