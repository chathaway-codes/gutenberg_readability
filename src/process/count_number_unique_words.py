import unittest


def main(book):
    return len(set([word.upper() for word in book.words]))


class NumberOfUniqueWordsTest(unittest.TestCase):

    def test_number_of_unique_words(self):
        class FakeBook:

            def __init__(self):
                self.words = ["Hello", "my", "my", "name", "is", "David"]
        self.assertEqual(main(FakeBook()), 5)


if __name__ == "__main__":
    unittest.main()
