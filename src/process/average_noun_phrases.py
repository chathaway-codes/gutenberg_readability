import unittest
import nltk
from process.story import Story
from process.tag_chunker import phrase_chunker

def main(book):
    noun_phrases = 0.0
    def traverse(tree):
        noun_phrases = 0.0
        if not hasattr(tree, 'label'):
            return 0.0
        if tree.label() == 'NP':
            noun_phrases += 1
        for child in tree:
            noun_phrases += traverse(child)
        return noun_phrases
    noun_phrases = traverse(book.chunked_words)
    return noun_phrases/len(book.sentences)

class AverageNounPhrasesTests(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_can_run(self):
        main(self.book)

if __name__ == "__main__":
    unittest.main()
