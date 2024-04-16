from typing import List

from pypdf import PdfReader

from japanki.pdf.lesson import Lesson


class Vocabulary:

    def __init__(self, filepath: str):
        self.reader = PdfReader(filepath)

    def lessons(self) -> List[Lesson]:
        lessons = []

        for page in self.reader.pages:
            text = page.extract_text(extraction_mode="layout")

            title = text.split("\n", 1)[0]

            lesson_id = int(title.strip().split()[1])

            if lesson_id > len(lessons):
                lessons.append(Lesson())

        return lessons

