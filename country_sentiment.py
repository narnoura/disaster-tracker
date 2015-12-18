import os
import re
from ngram import NGram

class CountrySentiment(object):

    def __init__(self, corpus_parser):
        '''
        Compute a sentiment value for frequent n-grams within 'offset' number of
        words of a search 'term'. Words in "positive-words.txt" are assigned a 
        sentiment value of +1, words in "negative-words.txt" are assigned a
        sentiment value of -1, and words in neither list are given a value of 0.

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
        self.pos_sentiment = []
        self.neg_sentiment = []
        self.welcome = []
        self.unwelcome = []
        self.read_pos_sentiment()
        self.read_neg_sentiment()
        self.read_welcome()
        self.read_unwelcome()
       


    
    def read_pos_sentiment(self):
        with open("lexicons/positive-words.txt") as p:
            for line in p:
                self.pos_sentiment.append(line.rstrip("\n").decode("utf-8", "ignore"))


    def read_neg_sentiment(self):
        with open("lexicons/negative-words.txt") as n:
            for line in n:
                self.neg_sentiment.append(line.rstrip("\n").decode("utf-8", "ignore"))

    def read_welcome(self):
        with open("lexicons/welcome_list.txt") as w:
            for line in w:
                self.welcome.append(line.rstrip("\n").decode("utf-8", "ignore").lower())

    def read_unwelcome(self):
        with open("lexicons/unwelcome_list.txt") as u:
            for line in u:
                self.unwelcome.append(line.rstrip("\n").decode("utf-8", "ignore").lower())


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
            self.word_dict[phrase_str] = NGram( \
                int(self.argv[3]), \
                phrase_str, \
                1, \
                self.get_sentiment_val(phrase),
                0, #don't care about topic_ref
                self.get_welcome_val(phrase)
            )


    def get_sentiment_val(self, phrase):
        value = 0
        for word in phrase:
            if word in self.neg_sentiment:
                value -= 1
            elif word in self.pos_sentiment:
                value += 1
        
        return value


    def get_welcome_val(self, phrase):
        value = 0
        for word in phrase:
            if word in self.unwelcome:
                value -= 1
            elif word in self.welcome:
                value += 1
        
        return value


    def print_dict(self):
        sorted_values = sorted(self.word_dict.values(), 
                               key=lambda ngram: ngram.frequency)
        for value in sorted_values:
            NGram.print_attrib(value)
            

    def print_welcome_score(self):
        sentiment_avg = self.weighted_avg("sentiment")
        welcome_avg = self.weighted_avg("welcome")
        print str(100 * (sentiment_avg + welcome_avg) / float(2))


    def weighted_avg(self, lexicon):
        avg = 0
        freq = 0
        phrase_weight = 0
        if lexicon == "sentiment":
            for phrase_n in self.word_dict.values():
                freq += phrase_n.frequency
                phrase_weight = phrase_n.frequency * phrase_n.sentiment_val
                avg += phrase_weight    
            
        elif lexicon == "welcome":
            for phrase_n in self.word_dict.values():
                freq += phrase_n.frequency
                phrase_weight = phrase_n.frequency * phrase_n.welcome
                avg += phrase_weight    
            
        #else: break
        print "avg: "+str(avg)+" freq: "+str(freq)
        print "avg/freq: "+str(avg/float(freq))
        return (avg/float(freq))


    def print_stats(self):
        #self.print_dict()
        self.print_welcome_score()
