import unittest
import nltk
from process.story import Story

def main(book):
    # This was copied from the documentation
    #  here: http://www.nltk.org/book/ch07.html
    # We should probably find a better one
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(book.pos_words)
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
    noun_phrases = traverse(result)
    return noun_phrases/len(book.sentences)

class AverageNounPhrasesTests(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_can_run(self):
        print main(self.book)

if __name__ == "__main__":
    unittest.main()
