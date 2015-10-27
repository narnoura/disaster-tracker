import os
from glob import glob
import re
from ngram import NGram

class BasicQuery(object):

    def __init__(self):
        self.corpus_dir = [] #List of string article titles
        self.word_dict = {}
        self.stop_words = []


    def read_from_dir(self):
        self.corpus_dir = glob("/Users/MichaelPinkham/Desktop/NewsAnalysis/Migrant_crisis/*")
            
        return self.corpus_dir

    
    def fill_stop_words(self):
        with open("/Users/MichaelPinkham/Desktop/NewsAnalysis/stop_words.txt") as f:
            for line in f:
                self.stop_words.append(line.rstrip("\n"))
        
        return self.stop_words

    
    def parse_articles(self):
        for filename in self.corpus_dir:
            with open(filename) as f:
                for line in f:
                    self.parse_line(line)


    def parse_line(self, line):
        word_list = re.split("\W+", line)
        for word in word_list:
            #clean_words = word.split("\n\n")
            #for unigram in clean_words:
             #   clean_unigram = unigram.strip(".,{}():\-!?\n\"")
             #   print clean_unigram
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
        sorted_values = sorted(self.word_dict.values(), key=lambda ngram: ngram.frequency)
        for value in sorted_values:
            NGram.print_attrib(value)

    def setup_query(self):
        self.read_from_dir()
        self.fill_stop_words()
        self.parse_articles()
        self.print_dict()
