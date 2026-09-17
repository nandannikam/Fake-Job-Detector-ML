import os

import joblib


def save_bundle(model, vectorizer, path="models/fake_job_model.pkl"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump({"model": model, "vectorizer": vectorizer}, path)
    print(f"bundle saved -> {path}")


def load_bundle(path="models/fake_job_model.pkl"):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"no bundle at '{path}' - train the model first (python src/train.py)"
        )
    bundle = joblib.load(path)
    return bundle["model"], bundle["vectorizer"]


if __name__ == "__main__":
    print("bundles model + vectorizer together so they always get loaded as a pair")
