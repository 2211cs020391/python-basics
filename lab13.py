#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy
nlp = spacy.load('en_core_web_sm')

sentence = 'NLP is amazing and fun to learn.'

# Process the sentence
doc = nlp(sentence)

# Perform part-of-speech tagging and print the results
for token in doc:
    print(f'{token.text}: {token.pos_}')


# In[ ]:




