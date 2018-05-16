import os
import collections
from io import open


SearchResult = collections.namedtuple('SearchResult', 
										'file, fileline, text')
def main():
	print_header()
	folder = get_folder_from_user()
	if not folder:
		print("Sorry, we can't search that location")

	text = get_search_text()
	if not text:
		print("We can't search for nothing")


	matches = search_folders(folder, text)
	match_count = 0
	for m in matches:
		match_count += 1
		#print("match")
		#print("file: " + m.file)
		#print("line: " + m.fileline)
		#print("text: " + m.text.strip())
		#print('')

	print("Found {:,} matche.".format(match_count))


def print_header():
	print('----------------------------')
	print('    FILE SEARCH APP')
	print('-----------------------------')
	print(' ')


def get_folder_from_user():
	folder = raw_input("What folder do you want to search?")
	if not folder or not folder.strip():
		return None

	if not os.path.isdir(folder):
		return None

	return os.path.abspath(folder)


def get_search_text():
	text = raw_input("What are you searching for [single phrases only]")
	return text.lower()


def search_folders(folder, text):
	#all_matches = []
	items = os.listdir(folder)
	for item in items:
		full_item = os.path.join(folder, item)
		if os.path.isdir(full_item):
			matches = search_folders(full_item, text)
			#all_matches.extend(matches)
			for m in matches:
				yield m
		else:
			matches = search_file(full_item, text)
			#ll_matches.extend(matches)
			for m in matches:
				yield m


def search_file(filename, search_text):
	#matches = []
	with open(filename, 'r', encoding = "ISO-8859-1") as fin:
		line_num = 0
		for line in fin:
			line_num += 1
			if line.find(search_text) >=0:
				m = SearchResult(fileline = line_num, file = filename, text = line)
				yield m

	#return matches

if __name__ == '__main__':
    main()