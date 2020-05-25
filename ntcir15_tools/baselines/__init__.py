from pathlib import Path
import _pickle as pickle
import bz2
from ntcir15_tools.data import baselines


def get_baselines_list():
    return baselines


def get_baseline_result(name, lang):
    assert name in get_baselines_list(), "Not valid baseline"
    assert lang in ["en", "ja"], "Language must be either ja or en"
    current_dir = Path(__file__).parent
    file_path = current_dir / "baselines.pbz2"
    with bz2.BZ2File(file_path, "rb") as f:
        baselines = pickle.load(f)
    return baselines[name][lang]
