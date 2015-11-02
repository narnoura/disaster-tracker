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
unigram_stats.get_stats()
unigram_stats.print_stats()

part2 = clock()

print "\n"
print (part1 - start)
print (part2 - part1)
