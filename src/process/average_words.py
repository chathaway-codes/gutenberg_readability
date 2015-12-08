import unittest
from process.story import Story


def main(book):
    return (1.0 * len(book.words)) / len(book.sentences)

class AverageNumberOfWordsTest(unittest.TestCase):
    def test_average_number_of_words(self):
        class FakeBook:
            def __init__(self):
                self.words = ["Hello", "my", "name", "is", "David"]
                self.sentences = ["Hello", "my name is David"]
        self.assertEqual(main(FakeBook()), 2.5)

if __name__ == "__main__":
    unittest.main()
