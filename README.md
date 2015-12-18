# disaster-tracker
Study print media rhetoric relating to the Syrian refugee crisis. Run one of the _ex.py files to get started.  

Corpus Parser: Saves JSON articles in a specified directory as Strings.

* Unigram Stats: Counts the number of appearances of each word in a corpus.
    * unigram_stats_ex.py path/to/archive/ path/to/stop-word-list  

*N-gram Stats: Counts the number of appearances of any phrase in a corpus.

Proximate Unigrams: Lists the words near a given word in a corpus.
    #$ proximate_words_ex.py path/to/archive/ path/to/stop-word-list (offset distance) (word to look for)  

Proximate N-grams: List the phrases near a given word in a corpus in order of frequency.
    #$ proximate_ngrams_ex.py path/to/archive/ path/to/stop-word-list (n-gram length) (word to look for) (offset)

Naive Sentiment: 

Aggregate Attributes: Lists the number of words with a given attribute in the corpus in order of frequency.
    #$ attribute_agg_ex.py path/to/archive/ path/to/stop-word-list	

Attribute Dictionary: For each attribute, lists the number of words in a corpus with that attribute.
    #$ attribute_agg_ex.py path/to/archive/ path/to/stop-word-list attribute	

A few notes:
-There must be files ./lexicon/positive-words.txt and ./lexicons/negative-words.txt to run Naive Sentiment
-A stop word list must be present. Many such lists are available online.
-The Harvard Inquirer Excel file must be saved as a .csv and be in ./lexicons/inquirerbasic.csv 
