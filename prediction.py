import pickle

def detecting_fake_news(news):    
    load_model = pickle.load(open('final_model_new.sav', 'rb'))
    prediction = load_model.predict([news])
    result = prediction[0]
    return result



if __name__ == '__main__':
    detecting_fake_news(news)





