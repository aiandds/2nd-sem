#import dataset
from sklearn import datasets
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

#load dataset from scikit 
wine=datasets.load_wine()

print("Features:",wine.feature_names,"\n")
print("Target name: ", wine.target_names,"\n")

#convert to dataframe
df = pd.DataFrame(wine.data,columns=wine.feature_names)
df['target'] = wine.target

d = df.drop((df.index[-48:]))
print(d)

x = d.drop(['target'], axis='columns')
y = d['target']
#print(x,"\n",y)

#70% train,30% test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=109)

cf=svm.SVC(kernel='linear')
cf.fit(x_train,y_train)
y_pred=cf.predict(x_test)

# print output
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Precision:",metrics.precision_score(y_test,y_pred))
print("Recall:",metrics.recall_score(y_test,y_pred))
