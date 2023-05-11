from Levenshtein import distance


def total_edit_distance(gt, pred):
    total_edit_distance = 0
    total_edit_distance_case_insensitive = 0
    for x, y in zip(gt, pred):
        total_edit_distance += distance(x, y)
        total_edit_distance_case_insensitive += distance(x.upper(), y.upper())
    return total_edit_distance, total_edit_distance_case_insensitive


def total_accuracy(gt, pred):
    total_crw = 0
    total_crw_case_insensitive = 0
    for x, y in zip(gt, pred):
        if x == y:
            total_crw += 1
        if x.upper() == y.upper():
            total_crw_case_insensitive += 1
    return total_crw, total_crw_case_insensitive
