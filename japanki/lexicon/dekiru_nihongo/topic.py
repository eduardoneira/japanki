from __future__ import annotations

from typing import List


class Topic:

    def __init__(self, number: int, name: Name, words: List[str]):
        self.number = number
        self.name = name
        self._words = words

    def words(self) -> List[str]:
        return self._words

    def __hash__(self):
        return hash((self.number, self.name))

    def __eq__(self, other):
        return self.number == other.number and self.name == other.name

    def __str__(self):
        return f'{self.number}: {self.name}'

    class Name:

        def __init__(self, spanish: str, japanese: str):
            self.spanish = spanish
            self.japanese = japanese

        def __hash__(self):
            return hash((self.spanish, self.japanese))

        def __eq__(self, other):
            return self.spanish == other.spanish and self.japanese == other.japanese

        def __str__(self):
            return f'{self.japanese} -> {self.spanish}'
