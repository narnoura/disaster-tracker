import os
import re
import sys
import json
from glob import glob

class CorpusParser(object):

    def __init__(self, argv):
        '''
        Parse a corpus of articles, save the articles as strings

        Args:
            argv (list): A list of arguments, passed from word_stats
                - argv[0]: 'word_stats.py', typically
                - argv[1]: The name of a directory containing .json
                           articles to be analyzed
                - argv[2]: The name of a stop-word list text file
        '''
        self.corpus_dir = [] #List of string article titles
        self.articles = []
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
                data = json.load(f)
                file_string = data["title"] + data["body"]
                self.articles.append(file_string)


    def parse(self):
        self.read_from_dir()
        self.fill_stop_words()
        self.parse_articles()
