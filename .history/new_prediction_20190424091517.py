#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
news = input("Please enter the news text you want to verify: ")
print("You entered: " + str(news))



def detecting_fake_news(news):    
    load_model = pickle.load(open('final_model_new.sav', 'rb'))
    prediction = load_model.predict([news])

    print("The given statement is ",prediction[0])
    a = sia.polarity_scores(news)
    if a['compound'] < 0:
        print("We advise you not to forward this news as it contains unpleasant element")
    
    



if __name__ == '__main__':
    detecting_fake_news(news)


# In[ ]:




