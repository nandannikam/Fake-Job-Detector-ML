import sys

from model_saver import load_bundle
from utils import MODEL_PATH, get_logger

logger = get_logger("main")


def get_multiline_input():

    print(
        "Paste the job description below, then press ENTER on a blank line when done:\n"
    )

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)

    return " ".join(lines)


def predict_posting(text, model, vectorizer):
    if not text.strip():
        raise ValueError("Please, give a valid input.")

    features = vectorizer.transform([text])
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    verdict = "SCAM" if pred == 1 else "LEGITIMATE"
    confidence = proba[pred]
    return verdict, confidence


def run_cli():
    print("=" * 55)
    print(" FAKE JOB POSTING DETECTOR")
    print("=" * 55)

    try:
        model, vectorizer = load_bundle(MODEL_PATH)
    except FileNotFoundError as e:
        logger.error(str(e))
        print(f"\n{e}")
        sys.exit(1)

    while True:
        text = get_multiline_input()

        try:
            verdict, confidence = predict_posting(text, model, vectorizer)
        except ValueError as e:
            print(f"\n{e}\n")
            continue

        print("\n" + "-" * 55)
        print(f" Verdict    : {verdict}")
        print(f" Confidence : {confidence * 100:.1f}%")
        print("-" * 55)

        logger.info(f"prediction: {verdict}, confidence={confidence:.4f}")

        again = input("\nDo you want to check other job post? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you!")
            break


if __name__ == "__main__":
    run_cli()
