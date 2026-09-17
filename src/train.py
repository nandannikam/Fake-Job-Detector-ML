# This has the code to train the model.

from sklearn.model_selection import train_test_split

from classifier import FakeJobClassifier
from data_loader import DataLoader
from evaluator import Evaluator
from feature_analyzer import print_top_features
from model_saver import save_bundle
from text_cleaner import TextVectorizer
from utils import (
    CONFUSION_MATRIX_PATH,
    DATA_PATH,
    MODEL_PATH,
    RANDOM_STATE,
    TEST_SIZE,
    get_logger,
)

logger = get_logger("train")


def main():
    logger.info("starting training run")

    loader = DataLoader(DATA_PATH)
    raw_df = loader.load()
    df = loader.build_text_column(raw_df)
    logger.info(f"got {len(df)} usable rows after cleanup")

    X_train_text, X_test_text, y_train, y_test = train_test_split(
        df["full_text"],
        df["fraudulent"],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["fraudulent"],
    )
    logger.info(f"train size: {len(X_train_text)}, test size: {len(X_test_text)}")

    vectorizer = TextVectorizer(max_features=5000)
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)
    logger.info(f"vectorized into {X_train.shape[1]} features")

    clf = FakeJobClassifier()
    clf.train(X_train, y_train)
    logger.info("training done")

    y_pred = clf.predict(X_test)
    evaluator = Evaluator(y_test, y_pred)
    evaluator.print_report()
    evaluator.save_confusion_matrix(CONFUSION_MATRIX_PATH)
    logger.info(f"metrics: {evaluator.summary()}")

    print_top_features(clf.model, vectorizer)

    save_bundle(clf.model, vectorizer, MODEL_PATH)
    logger.info("all done")


if __name__ == "__main__":
    main()
