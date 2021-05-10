import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

article_true = """
Arlene Foster will quit the Democratic Unionist Party (DUP) when she stands down as Northern Ireland's first minister, BBC News NI understands.

Sources close to her said she thinks it is no longer the party she joined and it is moving in a different direction.

Mrs Foster is to resign as DUP leader on 28 May and end her tenure as first minister at the end of June.

On Thursday, Agriculture Minister Edwin Poots declared his intention to stand for the party leadership.

Speaking on Friday, Mrs Foster said she would wait until she stepped down as first minister before making public her decision on whether she will remain in the DUP.

On a visit to a primary school in Cloughey in County Down she added that none of her colleagues who signed a letter of no confidence in her had spoken to her since.

Mrs Foster has led the DUP since December 2015.

The following month she was appointed first minister, becoming the first woman and the youngest person to hold both jobs.
In her resignation statement on Wednesday, Mrs Foster said she was preparing to leave the political stage.

BBC News NI understands that means not only quitting as a Stormont assembly member but severing her ties with the party she has led since December 2015.

On Thursday she informed her constituency association in Fermanagh and South Tyrone of her decision.

Quizzed on Friday whether she would go to the House of Lords, she said that was a matter for others.
Asked about her party's future, she wished her successor and the party well.

She also said not all her colleagues had signed the motion of no confidence and said some "good friends" did not.
Mrs Foster announced her resignation after about 80% of the DUP's Stormont and Westminster ranks signed a letter of no confidence in her leadership.
She has endured several major challenges at the helm of the party, including division among members on social issues and significant recent pressure resulting from the fallout from Brexit, which the party supported.
He has secured the backing of senior assembly member Christopher Stalford, who said his friend had the "experience and talents to take our country and our party forward".
Securing the support of a majority of the party's 27 members of the legislative assembly (MLAs) will be crucial to his hopes of replacing Mrs Foster.
Only a small number of the DUP's membership - its MLAs and MPs - will get to vote in a leadership contest.
"""

article_false = """
The Pacific Northwest tree octopus (Octopus paxarbolis) can be found in the temperate rainforests of the Olympic Peninsula on the west coast of North America. Their habitat lies on the Eastern side of the Olympic mountain range, adjacent to Hood Canal. These solitary cephalopods reach an average size (measured from arm-tip to mantle-tip,) of 30-33 cm. Unlike most other cephalopods, tree octopuses are amphibious, spending only their early life and the period of their mating season in their ancestral aquatic environment. Because of the moistness of the rainforests and specialized skin adaptations, they are able to keep from becoming desiccated for prolonged periods of time, but given the chance they would prefer resting in pooled water.

An intelligent and inquisitive being (it has the largest brain-to-body ratio for any mollusk), the tree octopus explores its arboreal world by both touch and sight. Adaptations its ancestors originally evolved in the three dimensional environment of the sea have been put to good use in the spatially complex maze of the coniferous Olympic rainforests. The challenges and richness of this environment (and the intimate way in which it interacts with it,) may account for the tree octopus's advanced behavioral development. (Some evolutionary theorists suppose that "arboreal adaptation" is what laid the groundwork in primates for the evolution of the human mind.)

Reaching out with one of her eight arms, each covered in sensitive suckers, a tree octopus might grab a branch to pull herself along in a form of locomotion called tentaculation; or she might be preparing to strike at an insect or small vertebrate, such as a frog or rodent, or steal an egg from a bird's nest; or she might even be examining some object that caught her fancy, instinctively desiring to manipulate it with her dexterous limbs (really deserving the title "sensory organs" more than mere "limbs",) in order to better know it.
"""

#Converts string into an array
#Will return None type if data is not a string
def convertToArray(data):
    #Check if the data passeed is a string
    if (type(data) == str):
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

