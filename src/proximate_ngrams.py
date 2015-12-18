import os
import re
from ngram import NGram

class ProximateNGrams(object):

    def __init__(self, corpus_parser):
        '''
        Find frequent n-grams within 'offset' number of
        words of a search 'term' 

        Args:
            corpus_parser: contains 
                a list of articles, 
                a list of stop_words,
                the command-line arguments 'argv', such that 
                    - argv[0]: 'word_stats.py'
                    - argv[1]: path/to/articles 
                    - argv[2]: path/to/stop_words
                    - argv[3]: n (a phrase length)
                    - argv[4]: term (the search term)
                    - argv[5]: offset (int)
        '''
        self.articles = corpus_parser.articles
        self.word_dict = {}
        self.stop_words = corpus_parser.stop_words
	self.argv = corpus_parser.argv


    def get_stats(self):
        for article in self.articles:
            self.parse_string(article)


    def parse_string(self, string):
	distance = int(self.argv[5])
        word_list = re.split("\W+", string)
	for i in range(distance, len(word_list) - distance):
	    if str(word_list[i]) == str(self.argv[4]):
		self.add_phrases(word_list, i)


    def add_phrases(self, word_list, i):
	distance = int(self.argv[5])
	phrase_len = int(self.argv[3])
	for j in range(-distance, distance + 1 - phrase_len):
	    phrase = []
	    for k in range(0, phrase_len):
		phrase.append(word_list[i+j+k])
	    
            self.update_dict(phrase)


    def update_dict(self, phrase):
        #if word.lower() not in self.stop_words:
        phrase_str = " ".join(phrase)
        if self.word_dict.has_key(phrase_str):
            self.word_dict[phrase_str].increment_freq()
        else:
            self.word_dict[phrase_str] = NGram(int(self.argv[3]), phrase_str, 1)


    def print_dict(self):
        sorted_values = sorted(self.word_dict.values(), 
                               key=lambda ngram: ngram.frequency)
        for value in sorted_values:
            NGram.print_attrib(value)


    def print_stats(self):
        self.print_dict()

