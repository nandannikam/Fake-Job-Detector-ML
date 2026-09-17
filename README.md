# Fake Job Posting Detector

## Project Title

**Fake Job Posting Detector** — a command-line tool that predicts whether a job listing is genuine or a scam, using a Logistic Regression model trained on real-world job posting data.

## Overview

Job scams are around these days and fresh graduates often fall for them because they haven't seen enough real job postings to spot the red flags. That’s why I decided to build a tool that actually helps with this problem. You paste in a job description and it tells you whether it looks real or fake along, with how sure it is.

Behind the scenes it’s not complicated. The text gets cleaned up turned into TF-IDF features and then fed into a Logistic Regression model that was trained on 18,000 labeled job ads. Half real half fake. It runs through a terminal interface so anyone can use it. No deep learning here no -trained models. This was made for an AI and ML fundamentals course. The point was to understand each step not just push buttons.

## Features

- Cleans and preprocesses job posting text by removing unnecessary noise and stripping out common stopwords

- Turns the cleaned text into TF-IDF features using both unigrams and bigrams to capture more context

- Trains a Logistic Regression model with class balancing to deal with the datasets strong imbalance favoring real postings

- After training reports accuracy, precision, recall and F1-score to measure how well the model performs

- Saves a confusion matrix as an image so you can quickly see where predictions go wrong

- Displays the top words and phrases that the model uses most for each class making the decisions easier to understand

- Stores the trained model and the vectorizer together so we don’t need to retrain every time we run the system

- Provides a command-line interface where you can paste any job posting and get an instant prediction

- Logs every training session and prediction result to a file, for tracking and debugging

- Includes unit tests that check the text-cleaning steps and make sure the model and vectorizer save and load correctly

## Technologies / Tools Used

| Category | Tool |
|---|---|
| Language | Python 3.10+ |
| ML library | scikit-learn (Logistic Regression, TF-IDF) |
| Data handling | pandas |
| Model persistence | joblib |
| Evaluation plots | matplotlib, seaborn |
| Testing | pytest |
| Version control | Git and GitHub |

## Project Structure

```
Fake-Job-Detector-ML/
├── data/                    # upload the Kaggle CSV here (not committed to the repo)
├── models/                  # trained model + confusion matrix is getting saved here
├── src/
│   ├── data_loader.py       # loads & validates the raw data CSV file
│   ├── text_cleaner.py      # text cleaning + TF-IDF vectorization is done here
│   ├── classifier.py        # Logistic Regression wrapper
│   ├── evaluator.py         # accuracy/F1all/precission + confusion matrix -> helps to evaluate the model
│   ├── model_saver.py       # saves/loads model+vectorizer as one bundle
│   ├── feature_analyzer.py  # shows which words drive predictions
│   ├── utils.py             # shared config paths + logging setup
│   ├── train.py             # run this first to train the model
│   └── main.py               # run this file to actually use the tool in the terminal
├── tests/
│   ├── test_text_cleaner.py
│   └── test_model_saver.py
├── statement.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Steps to Install & Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/nandannikam/Fake-Job-Detector-ML.git
cd Fake-Job-Detector-ML
```

### 2. Create a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```



### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

This project uses the **"Real / Fake Job Posting Prediction"** dataset from Kaggle:
https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

Download the CSV, rename it to `fake_job_postings.csv` if needed, and place it at:

```
data/fake_job_postings.csv
```

The dataset itself isn't included in the repo since it's not mine to redistribute — grab it directly from Kaggle.

### 5. Train the model

```bash
python src/train.py
```

This loads the dataset, cleans and vectorizes the text, trains the classifier, prints out the evaluation metrics, saves a confusion matrix image, and stores the trained model in `models/`.

### 6. Run the detector

```bash
python src/main.py
```

Paste in a job description when prompted, hit Enter on a blank line, and you'll get a verdict (`LEGITIMATE` or `SCAM`) with a confidence percentage.

## Instructions for Testing

Run the unit test suite from the project root:

```bash
python -m pytest tests/ -v
```

This runs tests covering the text-cleaning function and the model save/load round-trip, so you can confirm the core logic works on your machine before relying on it.


## Sample Inputs to Try

Here are a few example postings you can paste into `python src/main.py` to see how the tool responds. A mix of obvious scams and normal listings, so you can compare the outputs side by side.

### Likely to be flagged as SCAM

**Example 1 — fake work-from-home offer**
```
Congratulations! You've been selected for an exclusive work-from-home
position paying $5000 per week. No experience necessary. To claim your
spot, please wire a small processing fee of $50 to our HR department
today. Limited spots available, act now!
```



**Example 2 — vague "no skills needed" listing**
```
Amazing opportunity to make money fast from your phone. No skills or
experience required. Just pay a small registration fee to get started
and begin earning thousands within your first week.
```

### Likely to be flagged as LEGITIMATE

**Example 3 — standard tech job posting**
```
We are seeking a Software Engineer with 3+ years of experience in
Python and cloud infrastructure. Responsibilities include designing
scalable backend services, collaborating with the product team, and
participating in code reviews. Bachelor's degree in Computer Science
or related field required. Competitive salary and benefits package.
```

**Example 4 — standard finance role**
```
Our accounting department is looking for a Financial Analyst to
support quarterly reporting and budget forecasting. The ideal
candidate holds a degree in Finance or Accounting and has at least
two years of experience with financial modeling. This is a full-time
position based in our downtown office.
```



> **Note:** Predictions depend on the dataset the model was trained on, so exact confidence scores will vary. These examples are meant to demonstrate the range of inputs the tool is built to handle, not to guarantee a specific output every time.


## Screenshots



**Training output:**

![Training output](screenshots/training-output.png)

**Confusion matrix:**

![Confusion matrix](screenshots/confusion-matrix.png)

**CLI detecting a scam posting:**

![Scam detection](screenshots/cli-scam-example.png)

**CLI detecting a legitimate posting:**

![Legitimate detection](screenshots/cli-legit-example.png)

## Limitations

- The model works as well as the patterns found in the training data. New or more clever scam language might not be caught.
- Only posts, in the English language.
- This is a tool based on numbers, not a promise. It should be used as a thought not as something to rely on completely. Never give money or personal bank information to someone claiming to be a recruiter no matter what any tool says.

## Author

Name - Nandan Nikam <br>
Registration No.: - 25MIM10102 <br>
Course - Fundamentals in AI & ML <br>
Course code - CSA2001 <br>
