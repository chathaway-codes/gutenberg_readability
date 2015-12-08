""" This file defines a function which takens in a list of Gutenberg ID's,
a list of features to apply, and applies those features to the Gutenberg ID's
It then writes these features to a csv file specified in settings.FEATURE_CSV """
from process.story import Story
from settings import FEATURE_CSV
import csv
import os


def run_features(book_ids, features):
    read_ids = []
    fieldnames = ['book_id'] + [name for name in features]
    if os.path.isfile(FEATURE_CSV):
        with open(FEATURE_CSV, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                read_ids.append(int(row['book_id']))
    else:
        with open(FEATURE_CSV, 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    # Get a list of the books loaded
    books = []

    # Open the CSV file for writing; headers should be in the form of
    #  book_id,feature1,feature2,feature3...

    for book_id in book_ids:
        book = None
        if int(book_id) in read_ids:
            print "Already processed book", book_id
            continue
        else:
            try:
                book = Story(book_id)
                print "Loaded book", book_id
            except:
                print "Error finding book", book_id
                continue
        book_results = {'book_id': book.book_id}
        print "Processing book ", book.book_id
        for name in features:
            print "->", name
            result = features[name](book)
            print "--> done!"
            book_results[name] = result
        with open(FEATURE_CSV, 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(book_results)

if __name__ == "__main__":
    from process.index import all_functions
    run_features([2701], all_functions)
