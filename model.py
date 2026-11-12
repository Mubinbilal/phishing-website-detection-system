# coding: utf-8
df = pd.read_csv('dataset .csv/')
#import basic liberaries

import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('dataset/phishing_site_urls.csv')
df.head()
df.shape()
df.shape
df.info
df.info()
df.isnull()
df.isnull().sum()
df.Label.value_counts()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[A-Za-z]+')
df.URL[0]
tokenizer.tokenize(df.URL[0])
df['text_tokenized'] = df.URL.map(lambda t: tokenizer.tokenize(t))
df.head()
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
df['text_stemmed'] = df['text_tokenized'].map(lambda l: [stemmer.stem(word) for word in l])
df.head()
df['text'] = df['text_stemmed'].map(lambda l: ' '.join(l))
df.head()
good_sites = df[df.label == 'good'] 
bad_sites = df[df.label == 'bad']
good_sites = df[df.Label == 'good'] 
bad_sites = df[df.Label == 'bad']
good_sites.head()
all_text = ' '.join(good_sites.text.to_list)
all_text = ' '.join(good_sites.['text'].to_list)
all_text = ' '.join(good_sites.['tex'].to_list)
all_text = ' '.join(good_sites['tex'].to_list)
all_text = ' '.join(good_sites['text'].to_list)
all_text = ' '.join(good_sites['text'].to_list())
all_text
get_ipython().system(' pip install wordcloud')
from wordcloud import wordcloud
from wordcloud import wordcloud
wordcloud = wordcloud(width=800 , height=400 , background_color='white').generate(all_text)
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)
from wordcloud import WordCloud
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.inshow(wordcloud, interpolation='bilinear')
plt.axis('off')
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.inshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
all_text = ' '.join(bad_sites['text'].tolist())
wordcloud = WordCloud(width=800 , height=400 , background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
df.head()
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
features = cv.fit_transform(df.text)
features[:5]
features[:5].toarray()
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(features, df.label)
x_train , x_test , y_train , y_test = train_test_split(features, df.label)
x_train , x_test , y_train , y_test = train_test_split(features, df.Label)
x_train , x_test , y_train , y_test = train_test_split(features, df.Label , test_size=0.2)
from sklearn.linear_model import LogisticRegression
l_model = LogisticRegression()
l_model.fit(x_train, y_train)
l_model.score(x_test, y_test)
l_model.score(x_train,y_train)
from sklearn.metrics import classification_report
print('\nCLASSIFICATION REPORT\n')
print(classification_report(l_model(x_test),y_test, target_names=['Bad', 'Good']))
from sklearn.metrics import classification_report
print('\nCLASSIFICATION REPORT\n')
print(classification_report(l_model(x_test),y_test, target_names=['Bad', 'Good']))
print('\nCLASSIFICATION REPORT\n')
print(classification_report(l_model.predict(x_test),y_test, target_names=['Bad', 'Good']))
con_mat = pd.DataFrame(confusion_matrix(l_model.predict(x_test),y_test, target_names=['Bad', 'Good']))
con_mat = pd.DataFrame(confusion_matrix(l_model.predict(x_test), y_test),
                      columns=['Predicted:Bad', 'Predicted:Good']
                      index = ['Actual:Bad', 'Actual:Good'])
con_mat = pd.DataFrame(confusion_matrix(l_model.predict(x_test), y_test),
                      columns=['Predicted:Bad', 'Predicted:Good'],
                      index = ['Actual:Bad', 'Actual:Good'])
from sklearn.metrics import confusion_matrix
con_mat = pd.DataFrame(confusion_matrix(l_model.predict(x_test), y_test),
                      columns=['Predicted:Bad', 'Predicted:Good'],
                      index = ['Actual:Bad', 'Actual:Good'])
print('\nCONFUSION MATRIX')
plt.figure(figsize=(6,4))
sns.heatmap(con_mat, annot = True , fmt='d' , cmap= "YlGnBu")
import seaborn as sns
print('\nCONFUSION MATRIX')
plt.figure(figsize=(6,4))
sns.heatmap(con_mat, annot = True , fmt='d' , cmap= "YlGnBu")
from sklearn.naive_bayes import MultinomialNB 
mnb = MultinomialNB()
mnb.fit(x_train, y_train)
mnb.fit(x_train, y_train)
mnb.score(x_test, y_test)
