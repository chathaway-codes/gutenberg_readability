import xml.etree.ElementTree as ET
import urllib2
import argparse

def main(url):
	node = ET.fromstring(urllib2.urlopen(url).read())
	ret = []
	for item in node.iter():
		if 'title' in item.attrib and item.attrib['title'].startswith('ebook:'):
			ret += [item.attrib['title'].split(":")[1]]
	return ret

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Extract books from a 'bookshelf' on the gutenberg site")
        parser.add_argument("url", type=str, help="URL of the page to open")
	args = parser.parse_args()
	
	results = main(args.url)
	for r in results:
		print r

