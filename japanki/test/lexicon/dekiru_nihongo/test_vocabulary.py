import pytest

from japanki.lexicon.dekiru_nihongo.vocabulary import Vocabulary


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        Vocabulary('invalid.dekiru_nihongo')


def test_lessons(vocabulary):
    assert vocabulary.lesson_count() == 15
