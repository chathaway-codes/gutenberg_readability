import xml.etree.ElementTree as ET
import urllib2
import os
import argparse
from bs4 import BeautifulSoup

try:
	from settings import mirror
except:
	mirror = 'http://www.gutenberg.lib.md.us/'

def main(book_id, mirror=mirror):
	""" Fetches a book by ID; please override mirror to use a local copy if being used automatically
	Returns the book in plain text
	"""
	url = mirror
	book_id = str(book_id)
	for c in book_id[:-1]:
		url += c + '/'
	url += book_id + '/'
	url2 = ''

	if url.startswith('file://'):
		# If it's a local file, get the url2 variable using os
		for n in os.listdir(url[len('file://'):]):
			if n.startswith(book_id) and n.endswith('.txt'):
				url2 = n
				break
	else:
		data = urllib2.urlopen(url).read().split("\n", 1)[1]
		soup = BeautifulSoup(data, 'html.parser')
		for n in soup.find_all('a'):
			href = n.get('href')
			if href.startswith(book_id) and href.endswith('.txt'):
				url2 = href
				break
	if url2 == "":
		print book_id
		print url
		raise Exception("Book not found")
	return urllib2.urlopen(url + url2).read().decode('utf-8')

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Returns the plain text of a book for given id")
	parser.add_argument("--url", dest="mirror_url", type=str, default="http://www.gutenberg.lib.md.us/", help="URL of the page to open")
	parser.add_argument("book_id", type=str, help="File to store the .pickle array in")
	args = parser.parse_args()
	
	results = main(args.book_id, args.mirror_url)
	print results

