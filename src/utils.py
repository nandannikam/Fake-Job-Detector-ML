"""
Shared config + logging setup so I'm not hardcoding paths in every
script and repeating print() everywhere.
"""

import logging
import os

DATA_PATH = "data/fake_job_postings.csv"
MODEL_PATH = "models/fake_job_model.pkl"
CONFUSION_MATRIX_PATH = "models/confusion_matrix.png"
LOG_PATH = "logs/app.log"

RANDOM_STATE = 42
TEST_SIZE = 0.2


def get_logger(name):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    logger = logging.getLogger(name)
    if logger.handlers:
        # avoids duplicate log lines if this gets called more than once
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(LOG_PATH)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
