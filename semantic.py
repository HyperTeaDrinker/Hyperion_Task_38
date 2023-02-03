"""
SE T38 - Semantic Similarity (NLP)
Compulsory Task 1
Thomas Siu - TS22110004677
"""

import spacy

nlp = spacy.load('en_core_web_md')
#nlp = spacy.load('en_core_web_sm')

tokens = nlp('bacon egg milk')
#tokens = nlp('banana monkey cat')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


'''
***********************************************************
Difference bettwen 'en_core_web_sm' and' 'en_core_web_md'
***********************************************************

The differences between the models are statistical. We'd expect larget model (md - medium)
to be in general being more accurate overall as it contains more entities.

In the 'cat', 'monkey', 'banana' case, both models successfully identified similarities among
the 3 words. However, it is worth noting that the medium size model returned with similarities
of higher statistical significance and additional correlations.

For instance, the similarity value between banana and the two animals ran using the two models:

en_core_web_sm
banana | monkey : 0.342621862888336
banana | cat    : 0.342621862888336

en_core_web_md
banana | monkey : 0.404150128364563
banana | cat    : 0.223588258028030

The sm model picks up correlation between Animal and Fruit and returned the same value for both animals.
The md model contains more entities and account for the difference between cat and money, knowing
that banana correlates to monkey more than apple.


***********************************************************
Another example: bacon, egg and milk
***********************************************************
Likewise to the cat, monkey, banana case, the medium model with more entities identify
different results.

en_core_web_sm
bacon | egg      : 0.6716424822807312
milk  | bacon    : 0.20311735570430756
milk  | egg      : 0.22523760795593262

en_core_web_md
bacon | egg      : 0.4960688352584839
milk  | bacon    : 0.4139375686645508
milk  | egg      : 0.5174922347068787

Both models identified correlation bettwen becon and egg.
While both models also identified stronger correlation bettwen milk to egg vs milk to bacon,
the medium size model spotted greater statiscial correlations.
'''