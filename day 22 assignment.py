#!/usr/bin/env python
# coding: utf-8

# In[8]:


import spacy

nlp = spacy.load("en_core_web_sm")
sentence = "NLP is amazing and fun to learn."
doc = nlp(sentence)

for token in doc:
    print(f"Word: {token.text}, POS: {token.pos_}, Tag: {token.tag_}, Explanation: {spacy.explain(token.tag_)}")


# In[7]:


import spacy.cli
spacy.cli.download("en_core_web_sm")


# In[ ]:




