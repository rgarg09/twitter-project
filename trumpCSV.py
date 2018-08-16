import pandas as pd
import numpy as np
import matplotlib as plt
import re
#%matplotlib inline

#tweets = pd.DataFrame()
df = pd.read_csv('convertcsv.csv') #Reading the dataset in a dataframe using Pandas
#print(df.head(10))
#print(df['text'].value_counts())

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


#print('Media and News:')
#print(df['text'].apply(lambda tweet: word_in_text('fake news', tweet) or word_in_text('fakenews', tweet) or word_in_text('news', tweet) or word_in_text('media', tweet) or word_in_text('fake media', tweet) or word_in_text('fake media', tweet) or word_in_text('fox', tweet) or word_in_text('cnn', tweet) or word_in_text('nbc', tweet) or word_in_text('abc', tweet) or word_in_text('nypost', tweet) or word_in_text('nytimes', tweet) or word_in_text('washingtonpost', tweet)).value_counts())
'''
print(df['text'].apply(lambda tweet: word_in_text('fake news', tweet) or word_in_text('fakenews', tweet) or word_in_text('news', tweet) or word_in_text('media', tweet) or word_in_text('fake media', tweet) or word_in_text('fake media', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('abc', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('nytimes', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('nypost', tweet)).value_counts())'''

'''
print('Countries:')
print(df['text'].apply(lambda tweet: word_in_text('russia', tweet) or word_in_text('mexico', tweet) or word_in_text('north korea', tweet) or word_in_text('south korea', tweet) or word_in_text('ukraine', tweet) or word_in_text('estonia', tweet) or word_in_text('lithuania', tweet) or word_in_text('syria', tweet) or word_in_text('india', tweet) or word_in_text('china', tweet) or word_in_text('japan', tweet) or word_in_text('pakistan', tweet) or word_in_text('iran', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('russia', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('mexico', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('north korea', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('china', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('iran', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('japan', tweet)).value_counts())'''

print(df['text'].apply(lambda tweet: word_in_text('fat', tweet) or word_in_text('hair', tweet)).value_counts())

'''
print('Economy:')
print(df['text'].apply(lambda tweet: word_in_text('tax', tweet) or word_in_text('stock exchange', tweet) or word_in_text('wall street', tweet) or word_in_text('jobs', tweet) or word_in_text('employment', tweet) or word_in_text('unemployment', tweet) or word_in_text('gdp', tweet) or word_in_text('economy', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('tax', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('stock exchange', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('wall street', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('jobs', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('employment', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('unemployment', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('gdp', tweet)).value_counts())'''

'''
print('Sports:')
print(df['text'].apply(lambda tweet: word_in_text('nfl', tweet) or word_in_text('football', tweet) or word_in_text('sports', tweet) or word_in_text('golf', tweet) or word_in_text('usga', tweet) or word_in_text('cubs', tweet) or word_in_text('nascar', tweet) or word_in_text('pga', tweet) or word_in_text('player', tweet)).value_counts())
'''

'''
print('Immigration:')
print(df['text'].apply(lambda tweet: word_in_text('immigration', tweet) or word_in_text('daca', tweet) or word_in_text('unlawful', tweet) or word_in_text('refugee', tweet) or word_in_text('lottery', tweet) or word_in_text('immigrant', tweet) or word_in_text('travel ban', tweet) or word_in_text('border security', tweet) or word_in_text('visa', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('immigration', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('daca', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('unlawful', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('refugee', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('lottery', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('immigrant', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('travel ban', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('visa', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('border security', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('wall', tweet) and not word_in_text('wall street', tweet)).value_counts())
'''


'''
print('Healthcare:')
print(df['text'].apply(lambda tweet: word_in_text('healthcare', tweet) or word_in_text('obamacare', tweet) or word_in_text('ocare', tweet) or word_in_text('health', tweet) or word_in_text('insurance', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('healthcare', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('obamacare', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('ocare', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('health ', tweet)).value_counts())
print(df['text'].apply(lambda tweet: word_in_text('insurance', tweet)).value_counts())
'''

'''
print('Armed Forces:')
print(df['text'].apply(lambda tweet: word_in_text('usnavy', tweet) or word_in_text('usmc', tweet) or word_in_text('uscg', tweet) or word_in_text('us military', tweet) or word_in_text('navy', tweet) or word_in_text('usarmy', tweet) or word_in_text('us army', tweet) or word_in_text('usairforce', tweet) or word_in_text('us air force', tweet) or word_in_text('air force', tweet) or word_in_text('military', tweet) or word_in_text('army', tweet) or word_in_text('coast guard', tweet) or word_in_text('marine corps', tweet)).value_counts())
'''

