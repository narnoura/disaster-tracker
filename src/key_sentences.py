import os
import re
from ngram import NGram

class KeySentences(object):

    def __init__(self, corpus_parser):
        '''
        Find key sentences in the corpus. Key sentences have either an extreme sentiment
        value (>2, <-2) or a high number of references to topic words.

        Args:
            corpus_parser: contains 
                a list of articles, 
                a list of stop_words,
                the command-line arguments 'argv', such that 
                    - argv[0]: 'word_stats.py'
                    - argv[1]: path/to/articles 
                    - argv[2]: path/to/stop_words
                    - argv[3]: term (the search term)
        '''
        self.articles = corpus_parser.articles
        self.word_dict = {}
	self.argv = corpus_parser.argv
        self.pos_sentiment = []
        self.neg_sentiment = []
        self.read_pos_sentiment()
        self.read_neg_sentiment()
        self.topic_list = ["prejudice", "racism", "xenophobia", "Muslim", "anti", 
            "foreigner", "government", "assimilate", "integrate", "welcome", 
            "arrive", "border", "borders", "refugee", "migrant", "seeker", 
            "immigrant", "thousands", "hundreds", "millions", "children", "camp"]      


    
    def read_pos_sentiment(self):
        with open("lexicons/positive-words.txt") as p:
            for line in p:
                self.pos_sentiment.append(line.rstrip("\n").decode("utf-8", "ignore"))


    def read_neg_sentiment(self):
        with open("lexicons/negative-words.txt") as n:
            for line in n:
                self.neg_sentiment.append(line.rstrip("\n").decode("utf-8", "ignore"))


    def get_stats(self):
        for article in self.articles:
            mod_article = "." + article + "."
            self.get_sentences(mod_article)



    def get_sentences(self, article):
        starts = [match.start() for match in re.finditer(re.escape(self.argv[3]), article)]
        for val in starts:
            open_period = close_period = val
            while article[open_period] != ".":
                open_period -= 1
            while article[close_period] != ".":
                close_period += 1
            sentence = article[open_period + 1 : close_period + 1]
            self.update_dict(sentence.split())


    def update_dict(self, phrase):
        phrase_str = " ".join(phrase)
        if self.word_dict.has_key(phrase_str):
            self.word_dict[phrase_str].increment_freq()
        else:
            self.word_dict[phrase_str] = NGram( \
                len(phrase),                    \
                phrase_str,                     \
                1,                              \
                self.get_sentiment_val(phrase), \
                self.get_topic_ref_count(phrase_str)
            )


    def get_sentiment_val(self, phrase):
        value = 0
        for word in phrase:
            if word in self.neg_sentiment:
                value -= 1
            elif word in self.pos_sentiment:
                value += 1
        
        return value

    
    def get_topic_ref_count(self, sentence):
        topic_ref_count = 0
        for word in self.topic_list:
            topic_ref_count += len(                      \
                [match.start() for match in re.finditer( \
                    re.escape(word), sentence            \
                )]                                       \
            )
        return topic_ref_count


    def print_dict(self):
        sorted_values = sorted(self.word_dict.values(), 
                               key=lambda ngram: ngram.sentiment_val)
        for value in sorted_values:
            NGram.print_attrib(value)
            


    def print_stats(self):
        for value in self.word_dict.values():
            if value.sentiment_val > 2 or \
            value.sentiment_val < -2 or \
            value.topic_ref_count > 2: 
                NGram.print_attrib(value)
                 

