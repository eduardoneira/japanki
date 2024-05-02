class Word:

    def __init__(self, kana, spanish, kanji=None):
        self.kana = kana
        self.kanji = kanji
        self.spanish = spanish

    def __str__(self):
        if self.kanji:
            return f'{self.kana} - {self.kanji}: {self.spanish}'

        return f'{self.kana}: {self.spanish}'
