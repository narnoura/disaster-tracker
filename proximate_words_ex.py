import sys
sys.path.append('./src/')
from corpus_parser import CorpusParser
from proximate_words import ProximateWords

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
proximate_stats = ProximateWords(corpus_parser)

# Parse articles for content words and print their frequencies
proximate_stats.get_stats()

proximate_stats.print_stats()

