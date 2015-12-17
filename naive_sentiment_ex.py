import sys
from corpus_parser import CorpusParser
from naive_sentiment import NaiveSentiment

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

# Get stats for the particular corpus
naive_sentiment = NaiveSentiment(corpus_parser)

# Parse articles for content words and print their frequencies

naive_sentiment.get_stats()

naive_sentiment.print_stats()


