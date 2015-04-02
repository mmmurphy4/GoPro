#!/usr/bin/python

import sys
import re

def wc(filename):
	words, chars, lines = 0, 0, 0
	pwords, pchars, plines = 0, 0, 0
	articles, sections = 0, 0
	print articles
	with open(filename) as f:
		for line in f:
			# print line
			num_words = line.split()
			r=re.match('Article (\d).', line, 0)
			if r:
				print line
				artnum = r.groups()[0]
				articles+=1
			if re.match('Section \d', line, 0):
				print line
				sections+=1
			for word in num_words:
				if word not in wordlist:
					pwords += 1
				else:
					pchars -= len(word)

			lines+=1
			words+=len(num_words)
			chars+=len(line)
			pchars+=len(line)

		print('all: {}   {}   {}   ' + filename).format(lines, words, chars)
		print('proper: {}   {}   {}   ').format(lines, pwords, pchars)
		print('Total Article {}').format(articles)
		print('Total Section {}').format(sections)


if __name__ == "__main__":
		wordlist = ['I', 'We', 'You', 'They', 
					'a', 'and', 'the', 'that', 
					'of', 'for', 'with']
		# wordlist = []
		wc(sys.argv[1])