from settings import FEATURE_CSV, FLESCH_KINCAID_CSV
import csv

def fkscore(words_per_sentence, syllables_per_word):
    return (206.835 - (1.015 * words_per_sentence) - (84.6 * syllables_per_word))

def fkgrade(words_per_sentence, syllables_per_word):
    return ((0.39 * words_per_sentence) + (11.8 * syllables_per_word) - 15.59)

def main():
    with open(FEATURE_CSV, 'r') as incsv:
        with open(FLESCH_KINCAID_CSV, 'a+') as outcsv:
            fieldnames = ['book_id', 'flesch_kincaid_score', 'flesch_kincaid_grade']
            writer = csv.DictWriter(outcsv, fieldnames=fieldnames)
            writer.writeheader()
            
            reader = csv.DictReader(incsv)
            for row in reader:
                results = {}
                results['book_id'] = row["book_id"]
                words = float(row["average_words"])
                syllables = float(row["average_syllables"])
                results['flesch_kincaid_score'] = fkscore(words, syllables)
                results['flesch_kincaid_grade'] = fkgrade(words, syllables)
                writer.writerow(results)


if __name__ == "__main__":
    main()
