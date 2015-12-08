import unittest

VOWELS = "AEIOUY"

def count_syllables(word):
    num = 0
    word = word.upper()
    if word[0] in VOWELS:
        num += 1
    for i in range(len(word) - 1):
        if word[i] not in VOWELS and word[i + 1] in VOWELS:
            num += 1
    if word.endswith("E") and not word.endswith("LE"):
        num -= 1
    if num == 0:
        num = 1
    return num


def main(book):
    total = sum([count_syllables(word) for word in book.words])
    return (1.0 * total) / len(book.words)


class AverageNumberOfSyllablesTest(unittest.TestCase):

    def test_average_number_of_syllables(self):
        class FakeBook:
            def __init__(self):
                self.words = ["Hello", "my", "name", "is", "David"]
        self.assertEqual(main(FakeBook()), 1.4)


if __name__ == "__main__":
    unittest.main()
