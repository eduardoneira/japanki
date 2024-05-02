import pytest


@pytest.fixture
def first_lesson(vocabulary):
    return vocabulary.lesson(1)


def test_topic_name(first_lesson):
    for i, names in enumerate([
        ('Mi nombre, País, Trabajo', '私の名前・国・仕事'),
        ('Mi cumpleaños', '私の誕生日'),
        ('Mi pasatiempo', '私の趣味')
    ]):
        topic_name = first_lesson.topic(i + 1).name
        spanish, japanese = names

        assert topic_name.spanish == spanish
        assert topic_name.japanese == japanese


def test_topic_words(first_lesson):
    topic = first_lesson.topic(2)

    assert len(topic.words()) == 6


def test_invalid_topic(vocabulary):
    for i in range(vocabulary.lesson_count()):
        lesson = vocabulary.lesson(i)

        with pytest.raises(IndexError):
            lesson.topic(lesson.topic_count() + 1)
