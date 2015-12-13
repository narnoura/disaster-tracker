import sys
from corpus_parser import CorpusParser
from corpus_attributes import CorpusAttributes
from time import clock

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Create the attributes object
corpus_attributes = CorpusAttributes(corpus_parser)

# Get aggregate statistics on attributes over time
corpus_attributes.get_attributes()
corpus_attributes.get_stats()

# Print them out
corpus_attributes.print_stats()
