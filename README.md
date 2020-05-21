# NTCIR15 TOOLS

This package contains tools for NTCIR15 data search task

https://ntcir.datasearch.jp/

## Installation

```bash
git clone https://github.com/longpham28/ntcir15_tools.git
cd ntcir15_tools
pip install .
```

## How to use

### Evaluating

The __evaluate__ function accepts either dict or list as input

#### msNDCG

```python
from ntcir15_tools.eval.ms_ndcg import evaluate

ranked_dict = {
    "DS1-J-0001": [
        "000000700005",
        "000000700025",
        "000000700137",
        "000000700138"
    ],
    "DS1-J-0002": [
        "000002216626",
        "000006875252",
        "000006875263",
        "000006875280"
    ]
}

ranked_list = [
    ["DS1-J-0001", "000000700005"],
    ["DS1-J-0001", "000000700025"],
    ["DS1-J-0001", "000000700137"],
    ["DS1-J-0001", "000000700138"],
    ["DS1-J-0002", "000002216626"],
    ["DS1-J-0002", "000006875252"],
    ["DS1-J-0002", "000006875263"],
    ["DS1-J-0002", "000006875280"],
]

result = evaluate(ranked_dict, n=5)

print(result)
# {'DS1-J-0001': 0.4, 'DS1-J-0002': 1.0}
```

#### q_measure

```python
from ntcir15_tools.eval.q_measure import evaluate

ranked_dict = {
    "DS1-J-0001": [
        "000000700005",
        "000000700025",
        "000000700137",
        "000000700138"
    ],
    "DS1-J-0002": [
        "000002216626",
        "000006875252",
        "000006875263",
        "000006875280"
    ]
}

ranked_list = [
    ["DS1-J-0001", "000000700005"],
    ["DS1-J-0001", "000000700025"],
    ["DS1-J-0001", "000000700137"],
    ["DS1-J-0001", "000000700138"],
    ["DS1-J-0002", "000002216626"],
    ["DS1-J-0002", "000006875252"],
    ["DS1-J-0002", "000006875263"],
    ["DS1-J-0002", "000006875280"],
]

result = evaluate(ranked_list, beta=1, n=5)
```

### Save result as file

The __save__ function accepts ranking result as either list or dict type.

Note that score for each document is required.

A result file will be then generated within the working directory.

```python
from ntcir15_tools.output import save
ranked_dict = {
    "DS1-J-0001": [
        ["000000700005", 10.0],
        ["000000700025", 7.0],
        ["000000700137", 3.0],
        ["000000700138", 1.0]
    ],
    "DS1-J-0002": [
        ["000002216626", 8.5],
        ["000006875252", 4.6],
        ["000006875263", 3.2],
        ["000006875280", 1.2]
    ]
}
save(lang="J", data=ranked_dict, algorithm="BERT", priority="1")

```
