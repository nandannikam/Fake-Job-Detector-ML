import os

import joblib
from sklearn.linear_model import LogisticRegression


class FakeJobClassifier:
    def __init__(self, class_weight="balanced"):

        self.model = LogisticRegression(
            class_weight=class_weight,
            max_iter=1000,
            random_state=42,
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        print(f"saved model -> {path}")

    def load(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"no model found at '{path}', run train.py first")
        self.model = joblib.load(path)
        return self.model


if __name__ == "__main__":
    print(
        "this file just defines the classifier class - run train.py to actually train something"
    )
