import re

from sklearn.feature_extraction.text import TfidfVectorizer

STOPWORDS = {  # covers the common words
    "the",
    "a",
    "an",
    "and",
    "or",
    "but",
    "if",
    "then",
    "so",
    "to",
    "of",
    "in",
    "on",
    "at",
    "for",
    "with",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "this",
    "that",
    "these",
    "those",
    "it",
    "its",
    "as",
    "by",
    "from",
    "we",
    "you",
    "your",
    "our",
    "will",
    "can",
    "they",
    "their",
    "he",
    "she",
    "his",
    "her",
    "i",
    "me",
    "my",
    "not",
    "no",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "than",
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)  # numbers/punctuation
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [w for w in words if w not in STOPWORDS and len(w) > 1]
    return " ".join(words)


class TextVectorizer:
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 2),  # bigrams help's to catch phrases like "wire transfer"
            min_df=2,
        )

    def fit_transform(self, texts):
        cleaned = [clean_text(t) for t in texts]
        return self.vectorizer.fit_transform(cleaned)

    def transform(self, texts):
        cleaned = [clean_text(t) for t in texts]
        return self.vectorizer.transform(cleaned)


if __name__ == "__main__":
    sample = "URGENT!! Earn $5000/week from HOME, no experience needed!!!"
    print("before:", sample)
    print("after :", clean_text(sample))
