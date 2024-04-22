from typing import List

from japanki.lexicon.dekiru_nihongo.topic import Topic

TOPIC_START_PATTERNS = ('１：', '２：', '３：')


class Lesson:

    def __init__(self, number: int, pages: List[str]):
        self.number = number
        self._pages = pages
        self._topics = [None] * 3

        page_index = 0
        offset = 0

        for t, pattern in enumerate(TOPIC_START_PATTERNS):
            topic_found = False

            while not topic_found:
                page = pages[page_index]

                pattern_start = page.find(pattern, offset)

                if pattern_start == -1:
                    page_index += 1
                    offset = 0
                else:
                    pattern_end = page.find('\n\n', pattern_start)

                    if pattern_end == -1:
                        pattern_end = page.find('\n', page.find('\n', pattern_start) + 1)

                    name_text = page[pattern_start + len(pattern):pattern_end]

                    self._topics[t] = Topic(t + 1, name_text)

                    offset = pattern_end
                    topic_found = True

    def topic(self, index: int) -> Topic:
        return self._topics[index - 1]

    def topic_count(self) -> int:
        return len(self._topics)

    def __str__(self):
        return f'Lección {self.number}'
