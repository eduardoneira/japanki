import pytest


def test_topic_name(vocabulary):
    lesson = vocabulary.lesson(1)

    for i, names in enumerate([
        ('Mi nombre, País, Trabajo', '私の名前・国・仕事'),
        ('Mi cumpleaños', '私の誕生日'),
        ('Mi pasatiempo', '私の趣味')
    ]):
        topic_name = lesson.topic(i + 1).name
        spanish, japanese = names

        assert topic_name.spanish == spanish
        assert topic_name.japanese == japanese


def test_invalid_topic(vocabulary):
    for i in range(vocabulary.lesson_count()):
        lesson = vocabulary.lesson(i)

        with pytest.raises(IndexError):
            lesson.topic(lesson.topic_count() + 1)
