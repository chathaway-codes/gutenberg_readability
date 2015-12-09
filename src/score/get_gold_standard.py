from settings import FLESCH_KINCAID_CSV
import csv

def get_gold_standard(filter_array):
        gold_clusters = []
        with open('../resources/childrens_fiction_books.txt') as f:
                children_stories = []
                for l in f.readlines():
                        book = int(l.strip())
                        if book in filter_array:
                                children_stories += [int(l.strip())]
                gold_clusters += [children_stories]

        with open('../resources/adult_fiction_books.txt') as f:
                children_stories = []
                for l in f.readlines():
                        book = int(l.strip())
                        if book in filter_array:
                                children_stories += [int(l.strip())]
                gold_clusters += [children_stories]
	return gold_clusters

def get_kincaid_cluster(filter_array):
	gold_clusters = {}
	with open(FLESCH_KINCAID_CSV, 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			if int(row['book_id']) in filter_array:
				if round(float(row['flesch_kincaid_grade'])) not in gold_clusters:
					gold_clusters[round(float(row['flesch_kincaid_grade']))] = []
				gold_clusters[round(float(row['flesch_kincaid_grade']))] += [int(row['book_id'])]
	ret = []
	for key in gold_clusters:
		ret += [gold_clusters[key]]
	return ret
