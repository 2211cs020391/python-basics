#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
paragraph = """
Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both valuable and meaningful.
"""
sentences = re.split(r'(?<=[.!?]) +', paragraph)
words = re.findall(r'\b\w+\b', paragraph)

# Print results
print("Sentences:")
print(sentences)

print("\nWords:")
print(words)


# In[ ]:




