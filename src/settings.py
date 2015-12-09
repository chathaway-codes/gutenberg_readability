import os
from nltk.parse import malt
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
mirror = 'file:///home/chathaway/gutenberg/www.gutenberg.lib.md.us/'
FEATURE_CSV = os.path.join(PROJECT_ROOT, 'output.csv')
FLESCH_KINCAID_CSV = os.path.join(PROJECT_ROOT, 'flesch_kincaid_results.csv')
