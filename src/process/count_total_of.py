""" Due to laziness, this file contains all functions that
require counting the total number of something """
import nltk
import unittest
from process.story import Story

def make_total_count(types):
    def main(book):
        total = 0
        for word in book.pos_words:
            if word[1] in types:
                total += 1
        return total
    return main

total_number_of_adjectives = make_total_count(['JJ', 'JJR', 'JJS'])
total_number_of_conjunctions = make_total_count(['CC', 'IN'])
total_number_of_common_and_proper_nouns = make_total_count(['NN', 'NNS', 'NNP', 'NNPS'])
total_number_of_proper_nouns = make_total_count(['NNP', 'NNPS'])

class CountTotalsTest(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_count_functions(self):
        count_functions = [total_number_of_adjectives, total_number_of_conjunctions,
                total_number_of_common_and_proper_nouns, total_number_of_proper_nouns]
        for f in count_functions:
            f(self.book)

if __name__ == "__main__":
    unittest.main()
