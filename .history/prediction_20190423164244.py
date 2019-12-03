import pickle
news = input("Please enter the news text you want to verify: ")
print("You entered: " + str(news))



def detecting_fake_news(news):    
    load_model = pickle.load(open('final_model_new.sav', 'rb'))
    prediction = load_model.predict([news])
    result = prediction
    return (print("The given statement is ",result))



if __name__ == '__main__':
    detecting_fake_news(news)





