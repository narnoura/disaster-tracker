import sys
sys.path.append('./src/')
from corpus_parser import CorpusParser
from key_sentences import KeySentences

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
key_sentences = KeySentences(corpus_parser)

# Parse articles for content words and print their frequencies
key_sentences.get_stats()

key_sentences.print_stats()

