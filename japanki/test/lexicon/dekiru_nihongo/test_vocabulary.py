import os

import pytest

from japanki.lexicon.dekiru_nihongo.vocabulary import Vocabulary
from japanki.test import RESOURCES_DIR

VOCABULARY_FILE = os.path.join(RESOURCES_DIR, 'vocabulary.pdf')


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        Vocabulary('invalid.dekiru_nihongo')


def test_lessons():
    vocabulary = Vocabulary(VOCABULARY_FILE)

    assert len(vocabulary.lessons()) == 15
