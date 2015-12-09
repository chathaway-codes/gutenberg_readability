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
