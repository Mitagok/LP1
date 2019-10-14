import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
dataset = pd.read_csv('tripdata2010.csv')
dataset.head()
dataset.dtypes
dataset.info()
dataset.isnull().any()
dataset = dataset.fillna(method='ffill')
dataset.isnull().any()
dataset.shape
dataset.head()
dataset = dataset.drop('Start date', axis=1)
dataset = dataset.drop('End date', axis =1)
dataset = dataset.drop('Start station', axis=1)
dataset = dataset.drop('End station',axis =1)
dataset.head()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(dataset['Bike number'])
dataset['Bike number'] = le.transform(dataset['Bike number'])
le = LabelEncoder()
le.fit(dataset['Member type'])
dataset['Member type'] = le.transform(dataset['Member type'])
dataset.head()
x = np.array(dataset)[:, :4]
y = np.array(dataset)[:, 4]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

pd.DataFrame(x_train).head()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred, y_test)
print((cm[0][0]+cm[1][1])/(sum(cm[0])+sum(cm[1])))
y_pred_user = gnb.predict(np.array([[1012, 31208, 31108, 614]]))
print(y_pred_user)
