
from mrjob.job import MRJob
import re

import re
import sys
WORD_REGEX = re.compile(r"\b\w+\b")
from mrjob.step import MRStep

class Lab1(MRJob):

	def steps(self):

			return [
	
			MRStep(mapper=self.mapper,

			combiner=self.combiner,

			reducer=self.reducer)
		]

	def mapper(self , _ ,line ):
			words = WORD_REGEX.findall(line)
			for word in words:
				yield (word , 1)
                
	def combiner(self , word , counts):
     	   	    yield None , (sum(counts), word)

	def reducer(self , _ , count_words_pair):
			yield max(count_words_pair)

        
if __name__ == '__main__': 
    		Lab1.run()
