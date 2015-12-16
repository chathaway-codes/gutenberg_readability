from settings import FEATURE_CSV
from score.get_gold_standard import *
from score.clustering import score_clusters
from nltk.metrics.scores import f_measure
import random

def run_baseline():
	gold_filter = []
	with open(FEATURE_CSV, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			gold_filter += [int(row['book_id'])]
	clusters = [[], []]
	for id in gold_filter:
		clusters[random.randint(0,len(clusters)-1)] += [id]
	f_score, recall, precision = score_clusters(clusters, get_gold_standard(gold_filter))
	print "%s,%s,%s" % (f_score, recall, precision )
	f_score, recall, precision = score_clusters([clusters[0] + clusters[1], [2098]], get_gold_standard(gold_filter))
	gold_standard  = get_gold_standard(gold_filter)
	print "f-score:", f_measure([set(clusters[0] + clusters[1]), set([])], [set(gold_standard[0]), set(gold_standard[1])])
	print "%s,%s,%s" % (f_score, recall, precision )



if __name__ == "__main__":
	run_baseline()
