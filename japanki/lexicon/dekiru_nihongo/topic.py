from __future__ import annotations


class Topic:

    def __init__(self, number, text_name: str):
        self.number = number

        japanese, spanish = [name.strip() for name in text_name.split('\n')]

        self.name = Topic.Name(spanish, japanese)

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
