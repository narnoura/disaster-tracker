import os
import re
import csv
from ngram import NGram

class CorpusAttributes(object):

	def __init__(self, corpus_parser):
		'''
		Find frequent words with a given attribute (e.g. "Strong," "Race") 

		Args:
		    corpus_parser: contains 
			a list of articles, 
			a list of stop_words,
			the command-line arguments 'argv', such that 
			    - argv[0]: 'word_stats.py'
			    - argv[1]: path/to/articles 
			    - argv[2]: path/to/stop_words
			    - argv[3]: attribute
		'''
		self.articles = corpus_parser.articles
		self.word_dict = {}
		self.stop_words = corpus_parser.stop_words
		self.argv = corpus_parser.argv
		self.attr_dict = {}
		self.attribute = ""
		self.attr_count = 0

	#reading in the Harvard Inquirer Lexicon
	#contains most english words and whether or not they possess "attributes"
   	def get_attributes(self):
		with open('./lexicons/inquirerbasic.csv', 'rU') as csvfile:
			attr_reader = csv.reader(csvfile, dialect = csv.excel_tab)
			for row in attr_reader:
				line = row[0].split(',')
				line_dict = {}
				for i in range(1, len(line)):
					line_dict[line[i]] = True
				
				#the key is a word that has attributes		
				#the attributes are in lineDict
				self.attr_dict[line[0]] = line_dict
			return self.attr_dict
				
	#reading in the corpus, looking for a specific attribute attr
	def get_stats(self, attr):
		self.attribute = attr
        	for article in self.articles:
            		self.parse_string(article)


	def parse_string(self, string):
		word_list = re.split("\W+", string)
		for i in range(0, len(word_list)):
			self.update_dict((word_list[i]).upper())


	def update_dict(self, word):
		if word in self.attr_dict:
		    #if the word in the article has a given attribute
		    if self.attribute in self.attr_dict[word]:
			self.attr_count += 1
			if word in self.word_dict:
				self.word_dict[word].increment_freq()
		    	else:
				self.word_dict[word] = NGram(1, word, 1)
		else:
		    pass


	def print_dict(self):
		sorted_values = sorted(self.word_dict.values(), 
				       key=lambda ngram: ngram.frequency)
		for value in sorted_values:
		    NGram.print_attrib(value)


	def print_stats(self):
		self.print_dict()
		
