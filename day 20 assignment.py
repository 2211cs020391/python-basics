#!/usr/bin/env python
# coding: utf-8

# In[4]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = 'data science machine learning artificial intelligence'

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()

output_file = 'wordcloud.png'
wordcloud.to_file(output_file)

print(f"WordCloud saved as {output_file}")

plt.show()


# In[ ]:




