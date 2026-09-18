# Fake Job Detector

## Problem Statement

Online job scams are becoming increasingly common in the job market. The primary targets of these scams are inexperienced job seekers who are fresh out of college and looking to secure their first job. These individuals are easy to target because they lack the working experience needed to differentiate between a genuine and a fraudulent job description. In most cases, a scam job description promises high salaries for minimal effort and may ask the victim to pay upfront fees to sign up or process their payment. Some scammers may ask for sensitive personal and banking details by tricking victims into providing them for a signing bonus. With the current boom in job searches online, there is a need for a system that can quickly scan through job descriptions to identify any of the common scam features mentioned above.

This project addresses that problem by building a machine learning model that classifies a job posting's text as either **legitimate** or **fraudulent**, based on patterns learned from a labelled dataset of real and fake postings.

## Scope of the Project

The main idea behind this project is to design a console-based software that:

1. Accepts the text of a job posting you copy there

2. Processes and encodes the job description into a representation

3. Feeds the data into a trained Logistic Regression model

4. Outputs the probability of Legitimate/Scam labels

What this project is **not**:

- A web application or browser extension, designed to run from the command line, as required by the course.

- A guarantee of accuracy; it is a model trained on past data, and like any machine‑learning model it can make mistakes, especially with job posting styles that it has not seen before.

- A replacement for basic caution; advice such, as 'never pay money for a job offer' remains important no matter what the tool says..

## Target Users

- Job seekers, students and recent graduates want a quick second opinion on a job posting that seems too good to be true. They want to check before they share information or apply.

- Anyone who is interested in seeing which specific words or phrases separate job postings, from fraudulent ones should notice that the tool also shows the models most influential features.

## High-Level Features

1. **Data loading and preprocessing**: loads the raw Kaggle dataset, sanity checks it, and combines the separate text fields (title, description, requirements, etc.) into a single text field per posting that can be used for modeling.
2. **Text cleaning and vectorization**: cleans text of lowercase, punctuation, numbers, and stopwords, then converts it to TF-IDF features using unigrams and bigrams.
3. **Model training**: trains a Logistic Regression classifier with class balancing, since fraudulent postings will compose a minority class in this highly imbalanced dataset.
4. **Evaluation**: reports accuracy, precision, recall, and F1 scores, and plots a confusion matrix image so that the model’s performance can be adequately assessed beyond just accuracy.
5. **Model interpretability**: extracts and displays the terms that most push the prediction towards one class or the other, so that users can understand what the model considers “fake” or “legitimate.”
6. **Command-line interface**: provides a simple way for the user to paste in a job description and receive an automated prediction with a confidence score.
7. **Model persistence**: saves the trained model and vectorizer together so that the ML pipeline does not need to be retrained from scratch on every run.
8. **Logging**: records training runs and predictions to a log file for simple debugging and tracing of individual predictions back through the ML pipeline.
9. **Automated testing**: automated unit tests sanity check the text-cleaning utility functions and verify that the model can be persisted and loaded correctly.
