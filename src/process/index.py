from average_noun_phrases import main as average_noun_phrases
from average_number_of_adjectives import main as average_number_of_adjectives
from average_number_of_common_proper_nouns import main as average_number_of_common_proper_nouns
from average_number_of_conjunctions import main as average_number_of_conjunctions
from average_number_of_proper_nouns import main as average_number_of_proper_nouns
from average_prepositional_phrases import main as average_prepositional_phrases
from average_verb_phrases import main as average_verb_phrases
from count_total_of import *
from length_of_document import main as length_of_document
from ratio_of_common_to_proper_nouns import main as ratio_of_common_to_proper_nouns
from average_syllables import main as average_syllables
from average_word_length import main as average_word_length
from average_words import main as average_words
from count_number_unique_words import main as count_number_unique_words


all_functions = {
    'average_noun_phrases': average_noun_phrases,
    'average_number_of_adjectives': average_number_of_adjectives,
    'average_number_of_common_proper_nouns': average_number_of_common_proper_nouns,
    'average_number_of_conjunctions': average_number_of_conjunctions,
    'average_number_of_proper_nouns': average_number_of_proper_nouns,
    'average_prepositional_phrases': average_prepositional_phrases,
    'average_verb_phrases': average_verb_phrases,
    'length_of_document': length_of_document,
    'ratio_of_common_to_proper_nouns': ratio_of_common_to_proper_nouns,
    'total_number_of_adjectives': total_number_of_adjectives,
    'total_number_of_conjunctions': total_number_of_conjunctions,
    'total_number_of_common_and_proper_nouns': total_number_of_common_and_proper_nouns,
    'total_number_of_proper_nouns': total_number_of_proper_nouns,
    'total_number_of_noun_phrases': total_number_of_noun_phrases,
    'total_number_of_verb_phrases': total_number_of_verb_phrases,
    'total_number_of_prepositional_phrases': total_number_of_prepositional_phrases,
    'average_syllables': average_syllables,
    'average_word_length': average_word_length,
    'average_words': average_words,
    'count_number_unique_words': count_number_unique_words,
}
