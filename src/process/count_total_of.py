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

def make_total_phrases(phrase_types):
    def main(book):
        pos_phrases = 0.0
        def traverse(tree):
            pos_phrases = 0.0
            if not hasattr(tree, 'label'):
                return 0.0
            if tree.label() in phrase_types:
                pos_phrases += 1
            for child in tree:
                pos_phrases += traverse(child)
            return pos_phrases
        pos_phrases = traverse(book.chunked_words)
        return pos_phrases
    return main

total_number_of_adjectives = make_total_count(['JJ', 'JJR', 'JJS'])
total_number_of_conjunctions = make_total_count(['CC', 'IN'])
total_number_of_common_and_proper_nouns = make_total_count(['NN', 'NNS', 'NNP', 'NNPS'])
total_number_of_proper_nouns = make_total_count(['NNP', 'NNPS'])

total_number_of_noun_phrases = make_total_phrases(['NP'])
total_number_of_verb_phrases = make_total_phrases(['VP'])
total_number_of_prepositional_phrases = make_total_phrases(['PP'])

class CountTotalsTest(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_count_phrases_functions(self):
        count_functions = [total_number_of_noun_phrases, total_number_of_verb_phrases, total_number_of_prepositional_phrases]
        for f in count_functions:
            f(self.book)
    def test_count_functions(self):
        count_functions = [total_number_of_adjectives, total_number_of_conjunctions,
                total_number_of_common_and_proper_nouns, total_number_of_proper_nouns]
        for f in count_functions:
            f(self.book)

if __name__ == "__main__":
    unittest.main()
