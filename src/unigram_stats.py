import os
import re
from ngram import NGram

class UnigramStats(object):

    def __init__(self, corpus_parser):
        '''
        Collect relevant stats about unigrams

        Args:
            corpus_parser: contains a list of articles 
        '''
        self.articles = corpus_parser.articles
        self.word_dict = {}
        self.stop_words = corpus_parser.stop_words

    
    def get_stats(self):
        for article in self.articles:
            self.parse_string(article)

    def parse_string(self, string):
        word_list = re.split("\W+", string)
        for word in word_list:
            self.update_dict(word)


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

