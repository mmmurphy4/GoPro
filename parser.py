#!/usr/bin/python

import sys

def wc(filename):
	words, chars, lines = 0, 0, 0
	with open(filename) as f:
		for line in f:
			num_words = line.split()
			lines+=1
			words+=len(num_words)
			chars+=len(line)

		print('{} {} {} ' + filename).format(lines, words, chars)


if __name__ == "__main__":
		wc(sys.argv[1])