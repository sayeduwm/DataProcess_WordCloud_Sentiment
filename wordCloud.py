'''
Created on Sep 9, 2021

@author: 12563
'''
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
stopwords = set(STOPWORDS)
stopwords.update(["delta", "variant"])

# Function to generate word cloud with basic contour
def generate_better_wordcloud(data, title, mask=None):
    cloud = WordCloud(scale=3,
                      max_words=150,
                      colormap='RdYlGn',
                      mask=mask,
                      background_color='white',
                      stopwords=stopwords,
                      collocations=True,
                      contour_color='black',
                      contour_width=1).generate(data)
    plt.figure(figsize=(10,8))
    plt.imshow(cloud)
    plt.axis('off')
    plt.title(title)
    plt.show()
    
# Use function to generate wordcloud
df=pd.read_csv('Final_merge_city_state_country_listed_tweettext_news_tweetplace_sentiment_all.csv')
df['clean_text_Tweet'].fillna('').apply(str)
print(df.clean_text_Tweet[5:])
generate_better_wordcloud(df.clean_text_Tweet[5:], 'tst')