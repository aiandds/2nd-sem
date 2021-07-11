import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

wine = datasets.load_wine()

df = pd.DataFrame(wine.data,columns=wine.feature_names)
print(df.info())

df['target']= wine.target

x = df.drop(['target'],axis='columns')
y = df['target']

scal = StandardScaler()
one = scal.fit_transform(x)

pca = PCA(n_components=2)
fnl_pca = pca.fit_transform(one)

plt.figure(figsize=(8,6))
plt.scatter(fnl_pca[:,0],fnl_pca[:,1],c=y)
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.title("Principal Component Analysis")
plt.show()
