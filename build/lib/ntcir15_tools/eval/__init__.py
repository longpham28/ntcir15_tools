import numpy as np
from pyNTCIREVAL import Labeler
from pyNTCIREVAL.metrics import MSnDCG
from collections import defaultdict
from ntcir15_tools.data import en_query_ids, ja_query_ids, en_labels, ja_labels


def get_rel_level(text):
    if text == "L0":
        return 0
    if text == "L1":
        return 1
    if text == "L2":
        return 2
    return 0


def get_qrels(query_id):
    lang = query_id.split("-")[1]
    assert query_id in en_query_ids or query_id in ja_query_ids, "not valid query_id"
    if lang == "E":
        labels = en_labels
    else:
        labels = ja_labels
    temp = labels[labels[:, 0] == query_id]
    temp = temp[:, 1:]
    result = {}
    for col_id, text in temp:
        result[col_id] = get_rel_level(text)
    return result


def get_MSnDCG_by_query_id(query_id, ranked_list, n):
    assert len(ranked_list) > 0, "empty list"
    assert n >= 1, "not valid n"

    qrels = get_qrels(query_id)
    labeler = Labeler(qrels)
    grades = [1, 2]
    rel_level_num = 3
    xrelnum = labeler.compute_per_level_doc_num(rel_level_num)
    metric = MSnDCG(xrelnum, grades, cutoff=n)

    labeled_ranked_list = labeler.label(ranked_list)
    result = metric.compute(labeled_ranked_list)
    return result


def evaluate_by_dict(data, n):
    result = {}
    for query_id, ranked_list in data.items():
        result[query_id] = get_MSnDCG_by_query_id(query_id, ranked_list, n)
    return result


def evaluate_by_list(data, n):
    dic = defaultdict(list)
    data = np.array(data)
    query_ids = np.unique(data[:, 0])
    for query_id, col_id in data:
        dic[query_id].append(col_id)
    return evaluate_by_dict(dic, n)


def evaluate(data, n):
    assert isinstance(data, dict) or isinstance(
        data, list) or isinstance(data, np.ndarray), "Not valid input"
    if isinstance(data, dict):
        return evaluate_by_dict(data, n)
    if isinstance(data, list) or isinstance(data, np.ndarray):
        return evaluate_by_list(data, n)
