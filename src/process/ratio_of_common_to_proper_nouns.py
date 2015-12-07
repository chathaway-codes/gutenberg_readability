import unittest
from process.story import Story

from process.count_total_of import total_number_of_proper_nouns, total_number_of_common_and_proper_nouns
def main(book):
    total_proper_nouns = total_number_of_proper_nouns(book)
    total_common_nouns = (total_number_of_common_and_proper_nouns(book)-total_proper_nouns)
    return float(total_common_nouns)/total_proper_nouns

class AverageNounPhrasesTests(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_can_run(self):
        main(self.book)

if __name__ == "__main__":
    unittest.main()
