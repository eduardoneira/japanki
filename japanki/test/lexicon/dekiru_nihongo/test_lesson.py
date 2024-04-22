import pytest
from japanki.test.lexicon.dekiru_nihongo.test_vocabulary import Vocabulary


def test_lesson(vocabulary):
    for i in range(1, vocabulary.lesson_count() + 1):
        lesson = vocabulary.lesson(i)

        assert lesson
        assert lesson.number == i
        assert lesson.topic_count() == 3

    with pytest.raises(IndexError):
        vocabulary.lesson(vocabulary.lesson_count() + 1)
