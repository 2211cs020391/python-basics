#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install requests beautifulsoup4')



# In[14]:


import requests
from bs4 import BeautifulSoup
def fetch_webpage_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            return title
        else:
            return f"Failed to fetch webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"
url = "https://example.com"
title = fetch_webpage_title(url)
print(f"Title of the webpage: {title}")


# In[ ]:




