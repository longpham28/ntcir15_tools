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
