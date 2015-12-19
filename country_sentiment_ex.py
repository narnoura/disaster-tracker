import sys
sys.path.append('./src/')
from corpus_parser import CorpusParser
from country_sentiment import CountrySentiment

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
country_sentiment = CountrySentiment(corpus_parser)

# Parse articles for content words and print their frequencies

country_sentiment.get_stats()

country_sentiment.print_stats()


