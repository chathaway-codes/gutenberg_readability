import os
from nltk.parse import malt
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
mirror = 'file://%s/../mirror/' % PROJECT_ROOT
malt_parser = malt.MaltParser(os.path.join(PROJECT_ROOT, '..', 'maltparser-1.8.1'), model_filename=os.path.join(PROJECT_ROOT, '..', 'engmalt.linear-1.7.mco'))
