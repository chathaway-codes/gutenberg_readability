import unittest


def main(book):
    total = sum([len(word) for word in book.words])
    return (1.0 * total) / len(book.words)


class AverageWordLengthTest(unittest.TestCase):

    def test_average_word_length(self):
        class FakeBook:
            def __init__(self):
                self.words = ["Hello", "my", "name", "is", "David"]
        self.assertEqual(main(FakeBook()), 3.6)


if __name__ == "__main__":
    unittest.main()
