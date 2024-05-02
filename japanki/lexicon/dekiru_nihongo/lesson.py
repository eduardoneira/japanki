from typing import List

from japanki.lexicon.dekiru_nihongo.topic import Topic


class Lesson:

    def __init__(self, number: int, topics: List[Topic]):
        self.number = number
        self._topics = topics

    def topic(self, index: int) -> Topic:
        return self._topics[index - 1]

    def topic_count(self) -> int:
        return len(self._topics)

    def __str__(self):
        return f'Lección {self.number}'
