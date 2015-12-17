import sys
from corpus_parser import CorpusParser
from proximate_ngrams import ProximateNGrams

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
proximate_ngrams = ProximateNGrams(corpus_parser)

# Parse articles for content words and print their frequencies
proximate_ngrams.get_stats()

proximate_ngrams.print_stats()

