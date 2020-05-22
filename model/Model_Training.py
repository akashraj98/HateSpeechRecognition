
# coding: utf-8


import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt




train = pd.read_csv(r"C:/users/amanr/desktop/PROJECT/Aman/train_E6oV3lV.csv")
test = pd.read_csv(r"C:/users/amanr/desktop/PROJECT/aman/test_tweets_anuFYb8.csv")



train['label'] = train['label'].astype('category')




from nltk.stem import WordNetLemmatizer
from nltk import tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re



train['text_lem'] = [''.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]',' ',text)) for text in lis]) for lis in train['tweet']]
test['text_lem'] = [''.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]',' ',text)) for text in lis]) for lis in test['tweet']]



#print(train)#['text_lem'])
train['text_lem']
print(train.shape)



#print(test['text_lem'])


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(train['text_lem'],train['label'])



print(y_train)
      



print(X_test.shape)




print(y_train.shape)



#from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score,accuracy_score


# In[45]:



print(X_train)


# In[46]:


vect = TfidfVectorizer(ngram_range = (1,4)).fit(X_train)


# In[47]:


vect_transformed_X_train = vect.transform(X_train)
vect_transformed_X_test = vect.transform(X_test)


# In[48]:


#print(vect.get_feature_names())
print(vect_transformed_X_train.shape)
print(vect_transformed_X_test.shape)
print(y_train.shape)
print(y_test.shape)



modelLR = LogisticRegression().fit(vect_transformed_X_train,y_train)
predictionsLR = modelLR.predict(vect_transformed_X_test)


print(sum(predictionsLR==1),len(y_test),f1_score(y_test,predictionsLR))
print('Accuracy :',accuracy_score(y_test,predictionsLR))
# print(y_test.shape)



print(predictionsLR)



import pickle

 with open('model2','wb') as f:
     pickle.dump(modelLR,f)
    

 with open('vector2','wb') as f:
     pickle.dump(vect,f)
    

