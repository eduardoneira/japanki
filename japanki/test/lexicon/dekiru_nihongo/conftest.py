import os

import pytest

from japanki.lexicon.dekiru_nihongo.vocabulary import Vocabulary
from japanki.test import RESOURCES_DIR

VOCABULARY_FILE = os.path.join(RESOURCES_DIR, 'vocabulary.pdf')


@pytest.fixture
def vocabulary():
    return Vocabulary(VOCABULARY_FILE)
