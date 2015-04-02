#!/usr/bin/python

import sys

def wc(filename):
	words, chars, lines = 0, 0, 0
	pwords, pchars, plines = 0, 0, 0
	with open(filename) as f:
		print f
		for line in f:
			print line
			num_words = line.split()
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


if __name__ == "__main__":
		wordlist = ['I', 'We', 'You', 'They', 
					'a', 'and', 'the', 'that', 
					'of', 'for', 'with']
		# wordlist = []
		wc(sys.argv[1])