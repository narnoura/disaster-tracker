import sys
from unigram_stats import UnigramStats

# Save single-word stats
unigram_stats = UnigramStats(sys.argv)

# Parse articles for content words and print their frequencies
unigram_stats.setup_query()
