import sys
from corpus_parser import CorpusParser
from unigram_stats import UnigramStats
from ngram_stats import NgramStats
from proximate_words import ProximateWords
from time import clock

start = clock()

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

part1 = clock()


# Get stats for the particular corpus
#unigram_stats = UnigramStats(corpus_parser)
#ngram_stats = NgramStats(corpus_parser)
proximate_stats = ProximateWords(corpus_parser)

# Parse articles for content words and print their frequencies
gsstart = clock()

#unigram_stats.get_stats()
#ngram_stats.get_stats()
proximate_stats.get_stats()
gsstop = clock()

#unigram_stats.print_stats()
#ngram_stats.print_stats()
proximate_stats.print_stats()

part2 = clock()

print "\n"
print "corpus_parser time: " + str(part1 - start)
print "ngram_stats time: " + str(part2 - part1)
print "get stats (in ngram_stats) time: " + str(gsstop - gsstart)
