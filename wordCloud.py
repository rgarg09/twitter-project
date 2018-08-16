import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

df = pd.read_csv('convertcsv.csv')

# Combine tweets in a single string
words = ' '.join(df['text'])

# Remove URLs, RTs, and twitter handles
noUrlsNoTags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

cloudMask = imread('twitter_mask.png', flatten=True)
wordcloud = WordCloud(
                      font_path='CENTAUR.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=1800,
                      height=1400,
                      mask=cloudMask
                     ).generate(noUrlsNoTags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('my_twitter_wordcloud_1.png', dpi=300)
plt.show()