import unittest
from process.story import Story

def make_main(list_of_phrases):
    def main(book):
        adjectives = 0.0
        for word in book.pos_words:
            if word[1] in list_of_phrases:
                adjectives += 1
        return adjectives/len(book.sentences)
    return main

class AverageNumberOfAdjectivesTest(unittest.TestCase):
    def setUp(self):
        self.book = Story(2701)
    def test_length_of_document(self):
        print make_main(['NN', 'NNS', 'NNP', 'NNPS'])(self.book)

if __name__ == "__main__":
    unittest.main()
