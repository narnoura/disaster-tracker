import sys
from corpus_parser import CorpusParser
from ngram_stats import NGramStats

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
ngram_stats = NGramStats(corpus_parser)

# Parse articles for content words and print their frequencies
ngram_stats.get_stats()

ngram_stats.print_stats()

