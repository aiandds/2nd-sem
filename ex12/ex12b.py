import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sn
from sklearn.metrics import confusion_matrix

num = datasets.load_digits()

df = pd.DataFrame(num.data)
#print(df)

df['target'] = num.target
print(df)

'''
plt.gray() 
for i in range(4):
    plt.matshow(num.images[i])
    plt.show()
'''

x = df.drop(['target'],axis='columns')
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

rf = RandomForestClassifier(n_estimators=20)
rf.fit(x_train, y_train)
y_pre = rf.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pre))

cm = confusion_matrix(y_test, y_pre)

plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True, cmap='viridis')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()