import re
from collections import defaultdict
from itertools import chain
from typing import List, Iterable

from japanki.lexicon.dekiru_nihongo.lesson import Lesson
from japanki.lexicon.dekiru_nihongo.topic import Topic
from japanki.lexicon.dekiru_nihongo.word import Word

TOPIC_START_PATTERNS = ('１：', '２：', '３：')


def extract_lesson_number(lesson_header: str) -> int:
    lesson, _ = lesson_header.split('\n', 1)
    _, lesson_number = lesson.strip().split()

    return lesson_number


def extract_lessons(pages: Iterable[str]) -> List[Lesson]:
    lesson_texts = defaultdict(list)
    lessons = []

    for page in pages:
        header, text = page.split('\n\n', 1)

        lesson_number = extract_lesson_number(header)

        lesson_texts[lesson_number].append(text)

    for lesson_number, texts in lesson_texts.items():
        lessons.append(Lesson(int(lesson_number), extract_topics(texts)))

    return lessons


def is_topic_start(text) -> int:
    for i, pattern in enumerate(TOPIC_START_PATTERNS):
        if text.startswith(pattern):
            return i + 1

    return 0


def extract_topic_name(first_line, second_line) -> Topic.Name:
    _, japanese_name = first_line.split('：')

    return Topic.Name(second_line, japanese_name.strip())


def extract_topics(texts: List[str]) -> List[Topic]:
    lines = map(str.strip, chain.from_iterable(map(lambda text: text.split('\n'), texts)))
    topics = []

    topic_name = None
    topic_number = 0
    words = []

    try:
        while True:
            line = next(lines)

            next_topic_number = is_topic_start(line)

            # Only for topic headers
            if next_topic_number > 0:
                if topic_name:
                    topics.append(Topic(topic_number, topic_name, words))

                topic_name = extract_topic_name(line, next(lines))
                topic_number = next_topic_number
                words = []
            # Word lines
            elif len(line) > 0:
                tokens = [token.strip() for token in re.split(r'\s{2,}', line)]

                if len(tokens) == 2:
                    words.append(Word(tokens[0], tokens[1]))
                elif len(tokens) == 3:
                    words.append(Word(tokens[0], tokens[2], tokens[1]))
    except StopIteration:
        topics.append(Topic(topic_number, topic_name, words))
        return topics
