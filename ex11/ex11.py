import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("apple_products.csv")
df= pd.DataFrame(data) 
#print(df)

plt.xlabel('price')
plt.ylabel('rating')
plt.scatter(df['Sale Price'], df['Number Of Ratings'],color="green")
plt.show()

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Sale Price','Number Of Ratings']])
#print(y_predicted)
df['cluster'] = y_predicted

#print(df)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
#df4 = df[df.cluster==3]

plt.scatter(df1['Sale Price'], df1['Number Of Ratings'],color="green",label='cluster 1')
plt.scatter(df2['Sale Price'],df2['Number Of Ratings'],color='red',label='cluster 2')
plt.scatter(df3['Sale Price'],df3['Number Of Ratings'],color='blue',label='cluster 3')
#plt.scatter(df4['Sale Price'],df4['Number Of Ratings'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='tomato',marker='*',label='centroid')
plt.legend()
plt.xlabel('price')
plt.ylabel('rating')
plt.show()





x = df.drop(['Product URL','Brand', 'Product Name','Upc','Ram','cluster'], axis=1)
print(x.info())
y = km.fit_predict(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=109)
km.fit(x_train,y_train)
pre = km.predict(x_test)

#print(pre,"\n",y_test)
#y_predicted = km.fit(x)
#pre = km.predict(x_test)
print("Accuracy:",metrics.accuracy_score(pre,y_test))
'''
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Sale Price','Number Of Ratings']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
plt.show()
'''
