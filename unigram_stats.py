import os
import re
import sys
from glob import glob
from ngram import NGram

class UnigramStats(object):

    def __init__(self, argv):
        '''
        Collect relevant stats about unigrams

        Args:
            argv (list): A list of arguments, passed from word_stats
                - argv[0]: 'word_stats.py', typically
                - argv[1]: The name of a directory containing .json
                           articles to be analyzed
                - argv[2]: The name of a stop-word list text file
        '''
        self.corpus_dir = [] #List of string article titles
        self.word_dict = {}
        self.stop_words = []
        self.argv = argv


    def read_from_dir(self):
        arg = str(self.argv[1])
        dir_name = self.clean_arg(arg)
        self.corpus_dir = glob(dir_name + "*")
            
        return self.corpus_dir


    def clean_arg(self, arg):
        end_slash = "/"
        if arg[len(arg) - 1] is '/':
            return arg
        else:
            return (arg + end_slash)

    
    def fill_stop_words(self):
        with open(str(self.argv[2])) as f:
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
