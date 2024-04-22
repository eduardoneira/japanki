from typing import List

from pypdf import PdfReader

from .lesson import Lesson


class Vocabulary:

    def __init__(self, filepath: str):
        self._reader = PdfReader(filepath)
        self._lessons: List[Lesson] = []

        texts = []
        current_lesson_number = 1

        for page in self._reader.pages:
            text = page.extract_text(extraction_mode="layout")

            title = text.split("\n", 1)[0]

            lesson_number = int(title.strip().split()[1])

            if lesson_number > current_lesson_number:
                self._lessons.append(Lesson(current_lesson_number, texts))
                current_lesson_number += 1
                texts = []

            texts.append(text)

        self._lessons.append(Lesson(current_lesson_number, texts))

    def lesson(self, index: int) -> Lesson:
        return self._lessons[index - 1]

    def lesson_count(self) -> int:
        return len(self._lessons)
