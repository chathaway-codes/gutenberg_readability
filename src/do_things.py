all_books = []
with open('../resources/adult_fiction_books.txt', 'r') as f:
  for line in f.readlines():
    all_books += [int(line)]

with open('../resources/childrens_fiction_books.txt', 'r') as f:
  for line in f.readlines():
    all_books += [int(line)]

from process.index import all_functions
from score.apply_features import run_features
run_features(all_books, all_functions)
