import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#Converts string into an array
#Will return None type if data is not a string
def convertToArray(data):
    #Check if the data passeed is a string
    if (type(data) == str or type(data) == int):
        data = "{0}".format(data)
        return [data.replace("/n", "")]
    #Check if the data passed is already an array
    elif (type(data) == list):
        return data
    
    return None

#Takes an array and checks it against the bot
def scan(data):
    #If the data passed is not a list
    if (type(data) != list):
        print("Scan was not passed a list data type")
        return None
    
    #Transform the data set
    vectorized_input_data = tfidf_vectorizer.transform(data)
    #Predict on the data set and calculate the accuracy
    prediction = pac.predict(vectorized_input_data)
    #Display and return the prediction
    print(prediction)
    return prediction

#-------TRAIN THE BOT FIRST-------

#Read the data
df=pd.read_csv('news.csv')
#Get shape and head
df.shape
df.head()

#Get the labels
labels=df.label
labels.head()

#Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
#Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

#Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
#Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)

def getScore():
    return float(accuracy_score(y_test,y_pred))

