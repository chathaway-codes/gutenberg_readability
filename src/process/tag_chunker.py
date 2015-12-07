# More or less copied from https://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf
import nltk.chunk
import itertools

class ChunkParser(nltk.ChunkParserI):
    def __init__(self, train_sentences):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
            for sent in train_sentences]
        self.tagger = nltk.TrigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag)
            in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

phrase_chunker = ChunkParser(nltk.corpus.conll2000.chunked_sents())
