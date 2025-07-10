import spacy
from collections import Counter
nlp= spacy.load('en')
docx=nlp(open("luke6.txt").read())
docx
nouns=[token.text for token in docx if token.is_stop!=True and token.is_punct !=True and token.pos_=='Noun' ]
nouns
word_freq= Counter(nouns)
common_nouns= word_freq.most_common(10)
print(common_nouns)
verbs = [ token.text for token in docx if token.is_punct !=True and token.pos_ == 'VERB']
print(Counter(verbs).most_common(10))
verbs_with_stopwords= [token.text for token in docx if token.is_stop !=True and token.is_punc !=True and token.pos_=='VERb' ]
print(Counter(verbs_with_stopwords).most_common(10))
        