import pytest

from japanki.pdf.vocabulary import Vocabulary


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        Vocabulary('invalid.pdf')


def test_lessons():
    vocabulary = Vocabulary('../../resources/vocabulary.pdf')

    assert len(vocabulary.lessons()) == 15
