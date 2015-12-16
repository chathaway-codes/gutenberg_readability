from settings import PROJECT_ROOT, FLESCH_KINCAID_CSV
import csv


def main():
    books = []
    with open(FLESCH_KINCAID_CSV, 'r') as incsv:
        reader = csv.DictReader(incsv)
        for row in reader:
            books.append(row['book_id'])
    adult_books = []
    child_books = []
    with open('../resources/adult_fiction_books.txt') as adult:
        adult_books = adult.readlines()
        adult_books = [x.strip() for x in adult_books]
        
    with open('../resources/childrens_fiction_books.txt') as child:
        child_books = child.readlines()
        child_books = [x.strip() for x in child_books]

    adult_books = [book for book in adult_books if book in books]
    child_books = [book for book in child_books if book in books]

    print "Total number of books: ", len(books)
    print "Total number of adult books: ", len(adult_books)
    print "Total number of child books: ", len(child_books)
    print "Overlap between books: ", (len(adult_books) + len(child_books) - len(books))
        
            

if __name__ == "__main__":
    main()
