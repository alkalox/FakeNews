#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import seaborn as sb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

test_filename = 'test.csv'
train_filename = 'train.csv'

train_news = pd.read_csv(train_filename)
test_news = pd.read_csv(test_filename)




#data observation
def data_obs():
    print("training dataset size:")
    print(train_news.shape)
    print(train_news.head(10))

    #below dataset were used for testing and validation purposes
    print(test_news.shape)
    print(test_news.head(10))
    



#distribution of classes for prediction
def create_distribution(dataFile):
    
    return sb.countplot(x='Label', data=dataFile)
    


create_distribution(train_news)



#data integrity check (missing label values)
#none of the datasets contains missing values therefore no cleaning required
def data_qualityCheck():
    
    print("Checking data qualitites...")
    train_news.isnull().sum()
    train_news.info()
        
    print("check finished.")

    #below datasets were used to 
    test_news.isnull().sum()
    test_news.info()






# In[2]:


fake = pd.read_csv('fake.csv')
fake_df = pd.DataFrame(fake)
fake_df.head()
new_df = fake_df[['thread_title']]
new_df.head()
new_df['Label'] = 'False'
new_df.head()
new_df.rename(columns={'thread_title' : 'Statement'} , inplace=True)
new_df.head()


# In[3]:


data_obs()


# In[4]:


data_qualityCheck()


# In[ ]:





# In[5]:


w_tokenized = {}
test_df = pd.DataFrame(test_news)
train_df = pd.DataFrame(train_news)
train_df['Statement'][1]
test_df.append(new_df)
test_df.head(3)


# In[6]:


##This function converts the string into word tokens
def w_token(data , wt):
    for i in range(len(train_df)):
        wt[i] = word_tokenize(train_df['Statement'][i])
        
        
         
w_token(train_df,w_tokenized)
w_tokenized[1]


# In[7]:


import string
print(string.punctuation)
table = string.punctuation


# In[8]:


punctuation = word_tokenize(table)
punctuation


# In[9]:


##this function will filter out all the punctuation
punctuation_filtered = {}
def punc_filter(data , punctuation , punctuation_filtered):
    for i in range(len(data)):
        punctuation_filtered[i] = [w for w in data[i] if not w in punctuation] 
        
       


# In[10]:


punc_filter(w_tokenized, punctuation , punctuation_filtered)


# In[11]:


punctuation_filtered[1]


# In[12]:


ps = PorterStemmer()
sp = SnowballStemmer('english')


# In[13]:


stemm_filter = {}
def stemming(data , stemm_filter):
    for i in range(len(data)):
        test = []
        for w in data[i]:
            test.append(sp.stem(w))
        stemm_filter[i] = test
            
        
    


# In[14]:


stemming(punctuation_filtered , stemm_filter)
stemm_filter[1]


# In[15]:


sia = SentimentIntensityAnalyzer()


# In[16]:


train_polarity = []


# In[17]:


for x in range(len(train_df["Statement"])):
    if sia.polarity_scores(train_df['Statement'][x])['compound'] > 0:
        train_polarity.append('positive')
    else :
        train_polarity.append('negative')


# In[18]:


train_polarity[1]


# In[19]:


len(punctuation_filtered)


# In[20]:


train_df.head(2)


# In[21]:


train_df["Filtered"] = pd.Series(punctuation_filtered) 


# In[22]:


train_df.head(2)


# In[23]:


train_df['Filtered']=train_df['Filtered'].apply(lambda x: " ".join(x) )


# In[24]:


train_df.head(2)


# In[39]:


new_csv = train_df.to_csv(r'C:\Users\rawat\fake news\processed.csv' , index = True)


# In[55]:


countV = CountVectorizer()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import  LogisticRegression
from sklearn import svm
from sklearn.metrics import confusion_matrix


# In[54]:


#building classifier using naive bayes 
nb_pipeline = Pipeline([
        ('NBCV',countV),
        ('nb_clf',MultinomialNB())])

nb_pipeline.fit(train_df['Filtered'],train_df['Label'])
predicted_nb = nb_pipeline.predict(test_news['Statement'])
print(np.mean(predicted_nb == test_news['Label']))


#building classifier using logistic regression
logR_pipeline = Pipeline([
        ('LogRCV',countV),
        ('LogR_clf',LogisticRegression())
        ])

logR_pipeline.fit(train_df['Filtered'],train_df['Label'])
predicted_LogR = logR_pipeline.predict(test_news['Statement'])
print(accuracy_score(predicted_LogR , test_news['Label']))


#building Linear SVM classfier
svm_pipeline = Pipeline([
        ('svmCV',countV),
        ('svm_clf',svm.LinearSVC())
        ])

svm_pipeline.fit(train_df['Filtered'],train_df['Label'])
predicted_svm = svm_pipeline.predict(test_news['Statement'])
print(np.mean(predicted_svm == test_news['Label']))




#random forest
random_forest = Pipeline([
        ('rfCV',countV),
        ('rf_clf',RandomForestClassifier(n_estimators=200,n_jobs=3))
        ])
    
random_forest.fit(train_df['Filtered'],train_df['Label'])
predicted_rf = random_forest.predict(test_news['Statement'])
print(np.mean(predicted_rf == test_news['Label']))



# In[ ]:





# In[52]:


tfidf_ngram = TfidfVectorizer(stop_words='english',ngram_range=(1,4),use_idf=True,smooth_idf=True)


# In[58]:


nb_pipeline_ngram = Pipeline([
        ('nb_tfidf',tfidf_ngram),
        ('nb_clf',MultinomialNB())])

nb_pipeline_ngram.fit(train_df['Statement'],train_df['Label'])
predicted_nb_ngram = nb_pipeline_ngram.predict(test_df['Statement'])
print(np.mean(predicted_nb_ngram == test_df['Label']))


#logistic regression classifier
logR_pipeline_ngram = Pipeline([
        ('LogR_tfidf',tfidf_ngram),
        ('LogR_clf',LogisticRegression())
        ])

logR_pipeline_ngram.fit(train_df['Statement'],train_df['Label'])
predicted_LogR_ngram = logR_pipeline_ngram.predict(test_df['Statement'])
print(np.mean(predicted_LogR_ngram == test_df['Label']))


#linear SVM classifier
svm_pipeline_ngram = Pipeline([
        ('svm_tfidf',tfidf_ngram),
        ('svm_clf',svm.LinearSVC())
        ])

svm_pipeline_ngram.fit(train_df['Statement'],train_df['Label'])
predicted_svm_ngram = svm_pipeline_ngram.predict(test_df['Statement'])
print(np.mean(predicted_svm_ngram == test_df['Label']))



#random forest classifier
random_forest_ngram = Pipeline([
        ('rf_tfidf',tfidf_ngram),
        ('rf_clf',RandomForestClassifier())
        ])
    
random_forest_ngram.fit(train_df['Statement'],train_df['Label'])
predicted_rf_ngram = random_forest_ngram.predict(test_df['Statement'])
print(np.mean(predicted_rf_ngram == test_df['Label']))


# In[45]:


import pickle


# In[46]:


model_file = 'final_model_new.sav'
pickle.dump(svm_pipeline_ngram,open(model_file,'wb'))


# In[47]:


from sklearn.metrics import confusion_matrix


# In[48]:


con = confusion_matrix(test_df['Label'] , predicted_svm_ngram)


# In[56]:


con


# In[50]:




