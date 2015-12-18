

class NGram(object):

    def __init__(self, n=1, gram="", frequency=0, sentiment_val=0, topic_ref_count = 0, welcome = 0):
        '''
        Represent an n-gram

        Args:
            n (int): The number "-gram" e.g. "unigram", "bigram", or "4-gram"
            gram (str): The gram to record, e.g. "Migrant" or "wind speed"
            frequency (int): The number of times the n-gram appears in the
                             associated text.
            sentiment_val (int): the sum of the sentiment values of the words
                        in the ngram, which are each -1, 0, or +1
            topic_ref_count (int): the number of times an n-gram contains a 
                        topic word
        '''

        self.n = n
        self.gram = gram
        self.frequency = frequency
        self.phrase = gram.split()
        self.sentiment_val = sentiment_val
        self.topic_ref_count = topic_ref_count
        self.welcome = welcome


    def increment_freq(self):
        self.frequency += 1
        return self.frequency


    def print_attrib(self):
        print str(self.n) + "\t" + \
            self.gram + "\t" + \
            str(self.frequency) + "\toccurrence\t" + \
            str(self.sentiment_val) + "\tsentiment\t" + \
            str(self.topic_ref_count) + "\ttopic ref"

            
