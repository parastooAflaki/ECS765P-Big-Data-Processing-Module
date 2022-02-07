
from mrjob.job import MRJob
import re
import sys
WORD_REGEX = re.compile(r"\b\w+\b")


class Lab1(MRJob):

	def mapper(self , _ ,line ):
		words = WORD_REGEX.findall(line)

		for word in words:
			yield (word.lower(), 1)
	def reducer(self , word , counts):
		word_counts = sum(counts)
		if word_counts >= 10 :
	#		sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(word,counts))
			yield(word , word_counts)



if __name__=='__main__':
	Lab1.run()



