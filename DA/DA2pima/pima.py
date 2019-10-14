import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
dataset = pd.read_csv('diabetes.csv')
dataset.isnull().any()
dataset = dataset.fillna(method='ffill')
dataset.head()
dataset.shape
x = np.array(dataset)[:, :8]
y = np.array(dataset)[:, 8]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
pd.DataFrame(x_train).head()
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

pd.DataFrame(x_test).head()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print((cm[0][0]+cm[1][1])/(sum(cm[0])+sum(cm[1])))
