import re
import operator
f = open('newsout.txt','r')
words = {}
for el in f:
	w = el.split()
	for i in xrange(0, len(w)):
		element = w[i]
		if element not in words:
			words[element] = 1
		else:
			words[element] += 1
sorted_x = sorted(words.items(), key=operator.itemgetter(1))
for el in sorted_x:
	print el[0], el[1]