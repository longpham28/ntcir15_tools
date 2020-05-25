from pathlib import Path
import pickle


def get_baselines():
    current_dir = Path(__file__).parent
    file_path = current_dir / "baselines.pkl"
    with open(file_path, "rb") as f:
        baselines = pickle.load(f)
    return baselines
