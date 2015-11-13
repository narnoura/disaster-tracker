import os
import re
from ngram import NGram

class ProximateWords(object):

    def __init__(self, corpus_parser):
        '''
        Collect relevant stats about unigrams

        Args:
            corpus_parser: contains a list of articles 
        '''
        self.articles = corpus_parser.articles
        self.word_dict = {}
        self.stop_words = corpus_parser.stop_words
	self.argv = corpus_parser.argv


    def get_stats(self):
        for article in self.articles:
            self.parse_string(article)


    def parse_string(self, string):
	#third argument is distance to check
	distance = int(self.argv[3])
        word_list = re.split("\W+", string)
	for i in range(distance, len(word_list) - distance):
	    if str(word_list[i]) == str(self.argv[4]):
		for j in range(-distance, distance+1):	
		    self.update_dict(word_list[i+j])

    def update_dict(self, word):
        if word.lower() not in self.stop_words:
            if self.word_dict.has_key(word):
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

