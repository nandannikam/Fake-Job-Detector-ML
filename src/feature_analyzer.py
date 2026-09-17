import numpy as np


def get_top_features(model, vectorizer, top_n=15):
    feature_names = np.array(vectorizer.vectorizer.get_feature_names_out())
    coefs = model.coef_[0]

    fraud_idx = np.argsort(coefs)[-top_n:][::-1]  # most positive
    legit_idx = np.argsort(coefs)[:top_n]  # most negative

    fraud_words = list(zip(feature_names[fraud_idx], coefs[fraud_idx]))
    legit_words = list(zip(feature_names[legit_idx], coefs[legit_idx]))

    return fraud_words, legit_words


def print_top_features(model, vectorizer, top_n=15):
    fraud_words, legit_words = get_top_features(model, vectorizer, top_n)

    print("\nwords pushing towards FAKE:")
    for word, w in fraud_words:
        print(f"  {word:<25} {w:+.3f}")

    print("\nwords pushing towards LEGITIMATE:")
    for word, w in legit_words:
        print(f"  {word:<25} {w:+.3f}")


if __name__ == "__main__":
    print(
        "call print_top_features(model, vectorizer) after training to see this in action"
    )
