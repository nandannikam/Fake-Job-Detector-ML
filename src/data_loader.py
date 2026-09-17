# Handles loading the raw dataset from disk.


import os

import pandas as pd


class DataLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load(self):

        if not os.path.exists(self.csv_path):  # helps to give proper error message
            raise FileNotFoundError(
                f"Could not find dataset at '{self.csv_path}'. Did you "
                "download it from Kaggle and drop it into data/?"
            )

        df = pd.read_csv(self.csv_path)

        if "fraudulent" not in df.columns:
            raise ValueError(
                "This CSV doesn't have a 'fraudulent' column - wrong file?"
            )

        return df

    def build_text_column(self, df):

        text_cols = [
            "title",
            "company_profile",
            "description",
            "requirements",
            "benefits",
        ]
        cols_that_exist = [c for c in text_cols if c in df.columns]

        df = df.copy()
        df[cols_that_exist] = df[cols_that_exist].fillna("")
        df["full_text"] = df[cols_that_exist].agg(" ".join, axis=1)

        df = df[df["full_text"].str.strip() != ""]
        df = df.reset_index(drop=True)

        return df[["full_text", "fraudulent"]]


if __name__ == "__main__":
    loader = DataLoader("data/fake_job_postings.csv")
    raw = loader.load()
    print(f"loaded {len(raw)} rows")

    clean = loader.build_text_column(raw)
    print(f"{len(clean)} rows after building full_text")
    print(clean["fraudulent"].value_counts())
