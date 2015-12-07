import unittest
from process.story import Story

def main(book):
    prepositional_phrases = 0.0
    def traverse(tree):
        prepositional_phrases = 0.0
        if not hasattr(tree, 'label'):
            return 0.0
        if tree.label() == 'PP':
            prepositional_phrases += 1
        for child in tree:
            prepositional_phrases += traverse(child)
        return prepositional_phrases
    prepositional_phrases = traverse(book.chunked_words)
    return prepositional_phrases/len(book.sentences)

class AveragePrepositionalPhrasesTests(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_can_run(self):
        main(self.book)

if __name__ == "__main__":
    unittest.main()
