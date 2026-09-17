# Problem Statement

## Problem Statement

Online job scams are happening more and more. The people who get hurt the most are people who just finished school and are looking for their job. They don't have experience yet to know the difference between a real job and a fake one. A normal scam job posting offers high pay for very little work. It might ask for money upfront to register or process something.. It might try to get personal and bank information by saying it's, for a signing bonus. Since many people look for jobs online these days there is real importance in a tool that can check the words of a job posting and see if it has the signs that usually show a scam.

This project addresses that problem by building a machine learning model that classifies a job posting's text as either **legitimate** or **fraudulent**, based on patterns learned from a labelled dataset of real and fake postings.

## Scope of the Project

The goal of this project is a command-line application that:

- Takes the text from a job posting that you paste directly into the terminal.

- Cleans and converts that job posting text into a representation.

- Feeds the job posting representation into a trained Logistic Regression model.

- Outputs a prediction – Legitimate or Scam – with a confidence score.

What this project is **not**:

- A web application or browser extension; it is designed to run from the command line as required by the course.

- A guarantee of accuracy; it is a model trained on past data and like any machine‑learning model it can make mistakes especially with job posting styles that it has not seen before.

- A replacement for basic caution; advice such, as "never pay money for a job offer" remains important no matter what the tool says.

## Target Users

- Job seekers, students and recent graduates want a quick second opinion on a job posting that seems too good to be true. They want to check before they share information or apply.

- Anyone who is interested in seeing which specific words or phrases separate job postings, from fraudulent ones should notice that the tool also shows the models most influential features.

## High-Level Features

1. **Data loading and preprocessing** — reads the raw Kaggle dataset, validates it, and merges the separate text fields (title, description, requirements, etc.) into a single usable input per posting.
2. **Text cleaning and vectorization** — lowercases text, strips punctuation and numbers, removes stopwords, and converts the result into TF-IDF features (unigrams and bigrams).
3. **Model training** — trains a Logistic Regression classifier with class balancing, since fraudulent postings make up a small minority of the dataset.
4. **Evaluation** — computes accuracy, precision, recall, and F1-score, and generates a confusion matrix image so performance can be assessed properly rather than judged on accuracy alone.
5. **Model interpretability** — extracts and displays the top words/phrases pushing predictions toward "fake" versus "legitimate," so the model's reasoning isn't a complete black box.
6. **Command-line interface** — lets the user paste in a job description and receive an instant verdict with a confidence percentage.
7. **Model persistence** — saves the trained model and its matching vectorizer together, so the tool doesn't need to retrain from scratch every time it runs.
8. **Logging** — records training runs and predictions to a log file for basic traceability and debugging.
9. **Automated testing** — unit tests validate the text-cleaning logic and confirm the model save/load process works correctly.
