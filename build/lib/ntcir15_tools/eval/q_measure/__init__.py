from ntcir15_tools.eval import get_qrels
from pyNTCIREVAL import Labeler
from pyNTCIREVAL.metrics import QMeasure
from collections import defaultdict
from ntcir15_tools.data import ng_queries
import numpy as np


def get_qmeasure_by_query_id(query_id, ranked_list, n, beta=1, limited=True):
    assert len(ranked_list) > 0, "empty list"
    assert n >= 1, "not valid n"
    if len(ranked_list[0]) > 1:
        ranked_list = [item[0] for item in ranked_list]
    qrels = get_qrels(query_id)
    if limited:
        ranked_list = [doc_id for doc_id in ranked_list if doc_id in qrels]
    else:
        for doc_id in ranked_list:
            if not doc_id in qrels:
                qrels[doc_id] = 0
    labeler = Labeler(qrels)
    grades = [1, 2]
    rel_level_num = 3
    xrelnum = labeler.compute_per_level_doc_num(rel_level_num)
    metric = QMeasure(xrelnum, grades, beta, cutoff=n)

    labeled_ranked_list = labeler.label(ranked_list)
    result = metric.compute(labeled_ranked_list)
    return result


def evaluate_by_dict(data, n, beta=1, limited=True):
    result = {}
    for query_id, ranked_list in data.items():
        if query_id in ng_queries:
            continue
        result[query_id] = get_qmeasure_by_query_id(
            query_id, ranked_list, n, beta,limited)
    return result


def evaluate_by_list(data, n, beta=1,limited=True):
    dic = defaultdict(list)
    data = np.array(data)
    query_ids = np.unique(data[:, 0])
    for query_id, col_id in data:
        if query_id in ng_queries:
            continue
        dic[query_id].append(col_id)
    return evaluate_by_dict(dic, n, beta,limited)


def evaluate(data, n, beta=1,limited=True):
    assert isinstance(data, dict) or isinstance(
        data, list) or isinstance(data, np.ndarray), "Not valid input"
    if isinstance(data, dict):
        return evaluate_by_dict(data, n, beta, limited)
    if isinstance(data, list) or isinstance(data, np.ndarray):
        return evaluate_by_list(data, n, beta, limited)
