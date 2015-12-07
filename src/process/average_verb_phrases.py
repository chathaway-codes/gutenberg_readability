import unittest
from process.story import Story

def main(book):
    verb_phrases = 0.0
    def traverse(tree):
        verb_phrases = 0.0
        if not hasattr(tree, 'label'):
            return 0.0
        if tree.label() == 'VP':
            verb_phrases += 1
        for child in tree:
            verb_phrases += traverse(child)
        return verb_phrases
    verb_phrases = traverse(book.chunked_words)
    return verb_phrases/len(book.sentences)

class AverageVerbPhrasesTests(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_can_run(self):
        main(self.book)

if __name__ == "__main__":
    unittest.main()
