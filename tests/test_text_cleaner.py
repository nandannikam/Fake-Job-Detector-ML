import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from text_cleaner import clean_text


def test_lowercases():
    assert clean_text("HELLO World") == "hello world"


def test_strips_punctuation_and_numbers():
    result = clean_text("Earn $5000/week NOW!!!")
    assert "$" not in result
    assert "5000" not in result
    assert "!" not in result


def test_drops_stopwords():
    result = clean_text("this is a job for the best candidate").split()
    assert "is" not in result
    assert "the" not in result
    assert "job" in result
    assert "candidate" in result


def test_empty_input():
    assert clean_text("") == ""


def test_single_letters_dropped():
    result = clean_text("a b c developer")
    assert "developer" in result
    assert " a " not in f" {result} "
