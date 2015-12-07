import unittest
import nltk
import re
from process.story import Story

# Pattern from http://nbviewer.ipython.org/github/lukewrites/NP_chunking_with_nltk/blob/master/NP_chunking_with_the_NLTK.ipynb
patterns = """
        NP: {<JJ>*<NN>+}
        {<JJ>*<NN><CC>*<NN>+}
        """
NPChunker = nltk.RegexpParser(patterns)

def main(book):
    noun_phrases = 0.0
    result = NPChunker.parse(book.pos_words)
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
        main(self.book)

if __name__ == "__main__":
    unittest.main()
