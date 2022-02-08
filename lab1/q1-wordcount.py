
from mrjob.job import MRJob
import re

import re
import sys
WORD_REGEX = re.compile(r"\b\w+\b")
from mrjob.step import MRStep

class Lab1(MRJob):


	def mapper(self , _ ,line ):
			words = WORD_REGEX.findall(line)
			for word in words:
				yield (word, 1)
      

	def reducer(self, word, counts):
       	 	yield (word, sum(counts))
        
if __name__ == '__main__': 
    		Lab1.run()
