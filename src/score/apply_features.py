""" This file defines a function which takens in a list of Gutenberg ID's,
a list of features to apply, and applies those features to the Gutenberg ID's
It then writes these features to a csv file specified in settings.FEATURE_CSV """
from process.story import Story
from settings import FEATURE_CSV
import csv

def run_features(book_ids, features):
    # Get a list of the books loaded
    books = []
    for id in book_ids:
        try:
            books += [Story(id)]
            print "Loaded book", id
        except:
            print "Error finding book", id


    # Open the CSV file for writing; headers should be in the form of
    #  book_id,feature1,feature2,feature3...
    fieldnames = ['book_id'] + [name for name in features]
    with open(FEATURE_CSV, 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for book in books:
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
