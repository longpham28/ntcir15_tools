

from collections import defaultdict
import numpy as np


gr_id = "uhai"


def get_row(query_id, doc_id, rank, score):
    return "{} 0 {} {} {} uhai".format(query_id, doc_id, str(rank), str(score))


def get_fname(lang, priority):
    return "uhai-{}-{}".format(lang, str(priority))


def get_rows_from_dict(dic):
    result = ""
    for query_id in dic:
        current_rank = 1
        for doc_id, score in dic[query_id]:
            result += get_row(query_id, doc_id, current_rank, score) + "\n"
            current_rank += 1
    return result


def get_rows_from_list(rows):
    result = ""
    query_current_ranks = defaultdict(int)
    for query_id, doc_id, score in rows:
        current_rank = query_current_ranks[query_id] + 1
        result += get_row(query_id, doc_id, current_rank, score) + "\n"
        query_current_ranks[query_id] += 1
    return result


def get_rows(data):
    assert isinstance(data, dict) or isinstance(
        data, list) or isinstance(data, np.ndarray), "Not valid input"
    if isinstance(data, dict):
        return get_rows_from_dict(data)
    if isinstance(data, list) or isinstance(data, np.ndarray):
        return get_rows_from_list(data)


def get_texts(data, algorithm):
    result = "<SYSDESC>{}</SYSDESC>\n".format(algorithm)
    return result + get_rows(data)



def save(lang, data, algorithm, priority="1"):
    fname = get_fname(lang, priority)
    with open(fname, "w") as f:
        texts = get_texts(data, algorithm)
        f.write(texts)
