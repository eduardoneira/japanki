from typing import List

from pypdf import PdfReader

from .lesson import Lesson
from .parser import extract_lessons


class Vocabulary:

    def __init__(self, filepath: str):
        self._reader = PdfReader(filepath)
        self._lessons = extract_lessons(
            map(lambda p: p.extract_text(extraction_mode='layout'), self._reader.pages))

    def lesson(self, index: int) -> Lesson:
        return self._lessons[index - 1]

    def lesson_count(self) -> int:
        return len(self._lessons)
