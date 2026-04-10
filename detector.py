import fasttext
import pandas as pd
import numpy as np
import regex as re
from sklearn.model_selection import train_test_split

data =pd.read_csv("/content/drive/MyDrive/new_data.csv")
data.head()
data.shape

data.dropna(inplace=True)

data['Label']='__label__'+data['Label'].astype(str)

data['decription']=data['Label']+" "+data['Language']
data['decription'][0]

def preprocessing(text):
  text=re.sub(r'[^\w\s]', ' ', text)
  text=re.sub(r' +', ' ', text)
  return text.strip().lower()

data['decription']=data['decription'].map(preprocessing)

train , test =train_test_split(data,test_size=0.2)

train.to_csv("language.train",columns=['decription'],index=False,header=False)
train.to_csv("language.test",columns=['decription'],index=False,header=False)

model=fasttext.train_supervised(input="/content/language.train")

model.test("/content/language.test")

user= input("Enter your text")
user_text= preprocessing(user)
model.predict(user_text)