import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from classifier import FakeJobClassifier
from model_saver import load_bundle, save_bundle
from text_cleaner import TextVectorizer


def test_save_and_load_roundtrip(tmp_path):

    texts = [
        "free money cash prize now click here fast",
        "senior software engineer role at real company",
        "win free cash prize instantly click now",
        "experienced software engineer needed at real company",
    ]
    labels = [1, 0, 1, 0]

    vectorizer = TextVectorizer(max_features=50)
    X = vectorizer.fit_transform(texts)

    clf = FakeJobClassifier()
    clf.train(X, labels)

    save_path = str(tmp_path / "test_model.pkl")
    save_bundle(clf.model, vectorizer, save_path)

    loaded_model, loaded_vectorizer = load_bundle(save_path)

    original_preds = clf.model.predict(X)
    loaded_preds = loaded_model.predict(loaded_vectorizer.transform(texts))

    assert list(original_preds) == list(loaded_preds)


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_bundle("models/does_not_exist.pkl")
