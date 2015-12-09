import sys
from corpus_parser import CorpusParser
from unigram_stats import UnigramStats
from ngram_stats import NGramStats
from proximate_words import ProximateWords
from proximate_ngrams import ProximateNGrams
from naive_sentiment import NaiveSentiment
from key_sentences import KeySentences
from time import clock

start = clock()

# Pick the corpus to parse
corpus_parser = CorpusParser(sys.argv)

# Parse it 
corpus_parser.parse()

part1 = clock()

# Get stats for the particular corpus
#unigram_stats = UnigramStats(corpus_parser)
#ngram_stats = NGramStats(corpus_parser)
#proximate_stats = ProximateWords(corpus_parser)
#proximate_ngrams = ProximateNGrams(corpus_parser)
#naive_sentiment = NaiveSentiment(corpus_parser)
key_sentences = KeySentences(corpus_parser)

# Parse articles for content words and print their frequencies
gsstart = clock()

#unigram_stats.get_stats()
#ngram_stats.get_stats()
#proximate_stats.get_stats()
#proximate_ngrams.get_stats()
#naive_sentiment.get_stats()
key_sentences.get_stats()
gsstop = clock()

#unigram_stats.print_stats()
#ngram_stats.print_stats()
#proximate_stats.print_stats()
#proximate_ngrams.print_stats()
#naive_sentiment.print_stats()
key_sentences.print_stats()

part2 = clock()

print "\n"
print "corpus_parser time: " + str(part1 - start)
print "sentences time: " + str(part2 - part1)
print "get stats (in sentences) time: " + str(gsstop - gsstart)
