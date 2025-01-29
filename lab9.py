#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return cleaned_text

input_text = 'Hello, Manasa! Welcome to HYD 500505.'
cleaned_text = clean_text(input_text)
print(cleaned_text)


# In[ ]:




