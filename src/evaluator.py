# Helps to get the accuracy of the model

import os

import matplotlib

matplotlib.use("Agg")  # headless backend, this needed since it runs from CLI/servers
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


class Evaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def summary(self):
        return {
            "accuracy": accuracy_score(self.y_true, self.y_pred),
            "precision": precision_score(self.y_true, self.y_pred, zero_division=0),
            "recall": recall_score(self.y_true, self.y_pred, zero_division=0),
            "f1_score": f1_score(self.y_true, self.y_pred, zero_division=0),
        }

    def print_report(self):
        m = self.summary()
        print("\n----- evaluation -----")
        for k, v in m.items():
            print(f"{k}: {v:.4f}")

        print("\nfull report:")
        print(
            classification_report(
                self.y_true,
                self.y_pred,
                target_names=["Legitimate", "Fraudulent"],
                zero_division=0,
            )
        )

    def save_confusion_matrix(self, out_path="models/confusion_matrix.png"):
        cm = confusion_matrix(self.y_true, self.y_pred)

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        plt.figure(figsize=(5, 4))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["Legitimate", "Fraudulent"],
            yticklabels=["Legitimate", "Fraudulent"],
        )
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
        print(f"saved confusion matrix -> {out_path}")


if __name__ == "__main__":
    # dummy numbers, just checking the functions don't error out
    y_true = [0, 1, 0, 1, 1, 0]
    y_pred = [0, 1, 0, 0, 1, 1]
    Evaluator(y_true, y_pred).print_report()
