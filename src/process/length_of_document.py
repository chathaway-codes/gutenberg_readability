import unittest

def main(book):
    return len(book.plain_text)

class LengthOfDocumentTest(unittest.TestCase):
    def test_length_of_document(self):
        class FakeBook:
            def __init__(self):
                self.plain_text = 'Hello, my name is Charles'
        self.assertEqual(main(FakeBook()), len(FakeBook().plain_text))

if __name__ == "__main__":
    unittest.main()
