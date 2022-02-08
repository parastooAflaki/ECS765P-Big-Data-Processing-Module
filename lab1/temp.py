
from mrjob.job import MRJob
import re

import re
import sys
WORD_REGEX = re.compile(r"\b\w+\b")
from mrjob.step import MRStep

class Lab1():

	def __init__(self):
		self.s = 0
		self.temp_func()
		print(self.s)
		

	def temp_func(self):
		with open('out2.txt') as f:
			lines = f.readlines()
        
		for line in lines:
			#print(line.split()[1])
			self.s+= int ( line.split()[1] )

if __name__ == '__main__': 
    		Lab1()
