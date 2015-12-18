import sys
sys.path.append('./src/')
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
attr_dict = corpus_attributes.attr_dict

for attribute in attr_dict["Entry"]:
	corpus_attributes.get_stats(attribute)
	print attribute +  " " + str(corpus_attributes.attr_count)

#corpus_attributes.print_stats()
