#!/usr/bin/python

import sys
import re

def wc(filename):
	words, chars, lines = 0, 0, 0
	pwords, pchars, plines = 0, 0, 0
	articles, sections = 0, 0
	subarticles=[]
	subarticles.append(0)
	with open(filename) as f:
		for line in f:
			num_words = line.split()
			r=re.match('Article (\d).', line, 0)
			if r:
				artnum = int(r.groups()[0])
				articles+=1
				subarticles.append(0)
			if re.match('Section \d', line, 0):
				sections+=1
				subarticles[artnum] += 1
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
		print('Total Sections per Article:')
		for i in range(1,articles+1):
			print('\tArticle {}: {}').format(i, subarticles[i])


if __name__ == "__main__":
		wordlist = ['I', 'We', 'You', 'They', 
					'a', 'and', 'the', 'that', 
					'of', 'for', 'with']
		# wordlist = []
		wc(sys.argv[1])