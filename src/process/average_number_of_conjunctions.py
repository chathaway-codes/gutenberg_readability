import unittest
from process.story import Story

from process.count_number_of_occurances import make_main

main = make_main(['CC', 'IN'])

class AverageNumberOfConjuctionsTest(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_length_of_document(self):
        main(self.book)

if __name__ == "__main__":
    unittest.main()
