import sys
from corpus_parser import CorpusParser
from unigram_stats import UnigramStats
from time import clock

start = clock()

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

part1 = clock()


# Get stats for the particular corpus
unigram_stats = UnigramStats(corpus_parser)

# Parse articles for content words and print their frequencies
gsstart = clock()
unigram_stats.get_stats()
gsstop = clock()

unigram_stats.print_stats()

part2 = clock()

print "\n"
print "corpus_parser time: " + str(part1 - start)
print "unigram_stats time: " + str(part2 - part1)
print "get stats (in unigram_stats) time: " + str(gsstop - gsstart)
