import sys
from corpus_parser import CorpusParser
from unigram_stats import UnigramStats

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
unigram_stats = UnigramStats(corpus_parser)

# Parse articles for content words and print their frequencies
unigram_stats.get_stats()

unigram_stats.print_stats()

