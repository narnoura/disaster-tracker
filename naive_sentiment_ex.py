import sys
from corpus_parser import CorpusParser
from unigram_stats import UnigramStats
from ngram_stats import NGramStats
from proximate_words import ProximateWords
from proximate_ngrams import ProximateNGrams
from naive_sentiment import NaiveSentiment
from time import clock

start = clock()

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

part1 = clock()

# Get stats for the particular corpus
naive_sentiment = NaiveSentiment(corpus_parser)

# Parse articles for content words and print their frequencies
gsstart = clock()

naive_sentiment.get_stats()
gsstop = clock()

naive_sentiment.print_stats()

part2 = clock()

print "\n"
print "corpus_parser time: " + str(part1 - start)
print "naive sentiment time: " + str(part2 - part1)
print "get stats (in naive sentiment) time: " + str(gsstop - gsstart)
