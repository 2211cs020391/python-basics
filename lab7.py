#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install gensim nltk


# In[6]:


import gensim
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
sample_text = """Use Genism to preprocess data from a sample text file, follow basic procedures like tokenization, stemming, lemmatization etc."""
tokens = word_tokenize(sample_text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Lemmatization using NLTK
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Print results
print("Original Tokens:", tokens[:10])  # Print first 10 tokens
print("Filtered Tokens (no stopwords):", filtered_tokens[:10])
print("Stemmed Tokens:", stemmed_tokens[:10])
print("Lemmatized Tokens:", lemmatized_tokens[:10])


# In[ ]:




