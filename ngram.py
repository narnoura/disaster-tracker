

class NGram(object):

    def __init__(self, n=1, gram="", frequency=0):
        '''
        Represent an n-gram

        Args:
            n (int): The number "-gram" e.g. "unigram", "bigram", or "4-gram"
            gram (str): The gram to record, e.g. "Migrant" or "wind speed"
            frequency (int): The number of times the n-gram appears in the
                             associated text.
        '''

        self.n = n
        self.gram = gram
        self.frequency = frequency
        self.phrase = gram.split() 


    def increment_freq(self):
        self.frequency += 1
        return self.frequency


    def print_attrib(self):
        print self.n, self.gram, self.frequency
