from ntcir15_tools.eval import get_qrels
from pyNTCIREVAL import Labeler
from pyNTCIREVAL.metrics import MSnDCG
from collections import defaultdict
import numpy as np
from ntcir15_tools.data import ng_queries


def get_MSnDCG_by_query_id(query_id, ranked_list, n):
    assert len(ranked_list) > 0, "empty list"
    assert n >= 1, "not valid n"
    if len(ranked_list[0]) > 1:
        ranked_list = [item[0] for item in ranked_list]
    qrels = get_qrels(query_id)
    for doc_id in ranked_list:
        if not doc_id in qrels:
            qrels[doc_id] = 0
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
        if query_id in ng_queries:
            continue
        result[query_id] = get_MSnDCG_by_query_id(query_id, ranked_list, n)
    return result


def evaluate_by_list(data, n):
    dic = defaultdict(list)
    data = np.array(data)
    query_ids = np.unique(data[:, 0])
    for query_id, col_id in data:
        if query_id in ng_queries:
            continue
        dic[query_id].append(col_id)
    return evaluate_by_dict(dic, n)


def evaluate(data, n):
    assert isinstance(data, dict) or isinstance(
        data, list) or isinstance(data, np.ndarray), "Not valid input"
    if isinstance(data, dict):
        return evaluate_by_dict(data, n)
    if isinstance(data, list) or isinstance(data, np.ndarray):
        return evaluate_by_list(data, n)
