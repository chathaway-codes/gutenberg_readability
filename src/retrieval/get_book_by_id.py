import xml.etree.ElementTree as ET
import urllib2
import argparse
from bs4 import BeautifulSoup

def main(book_id, mirror='http://www.gutenberg.lib.md.us/'):
	""" Fetches a book by ID; please override mirror to use a local copy if being used automatically
	Returns the book in plain text
	"""
	url = mirror
	for c in str(book_id)[:-1]:
		url += c + '/'
	url += book_id + '/'
	url2 = ''

	data = urllib2.urlopen(url).read().split("\n", 1)[1]
	soup = BeautifulSoup(data, 'html.parser')
	for n in soup.find_all('a'):
		href = n.get('href')
		if href.startswith(book_id) and href.endswith('.txt'):
			print "Here"
			url2 = href
			break
	if url2 == "":
		raise Exception("Book not found")
	return urllib2.urlopen(url + url2).read()

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Returns the plain text of a book for given id")
	parser.add_argument("--url", dest="mirror_url", type=str, default="http://www.gutenberg.lib.md.us/", help="URL of the page to open")
	parser.add_argument("book_id", type=str, help="File to store the .pickle array in")
        args = parser.parse_args()
        
        results = main(args.book_id, args.mirror_url)
	print results

