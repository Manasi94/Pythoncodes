import itertools
import enchant
d = enchant.Dict("en_US")
testVar=raw_input("Ask user for input")
combinations = list(map("".join, itertools.permutations(testVar)))
for i in xrange(0,len(combinations)):
	if d.check(combinations[i]):
		print combinations[i]
