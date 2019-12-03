#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle
news = input("Please enter the news text you want to verify: ")
print("You entered: " + str(news))



def detecting_fake_news(news):    
    load_model = pickle.load(open('final_model_new.sav', 'rb'))
    prediction = load_model.predict([news])
    return (print("The given statement is ",prediction))



if __name__ == '__main__':
    detecting_fake_news(news)


# In[ ]:




