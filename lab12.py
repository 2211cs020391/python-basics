#!/usr/bin/env python
# coding: utf-8

# In[15]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = 'data science machine learning artificial intelligence'

wordcloud = WordCloud().generate(text)

# Save the WordCloud image
wordcloud.to_file('wordcloud.png')

# Display the WordCloud image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[ ]:




