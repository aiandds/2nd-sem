import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
from sklearn.preprocessing import LabelEncoder


jack = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
jr = pd.read_csv(jack)

#print(jr.info())
jr.fillna(jr.mean(), inplace=True)

le = LabelEncoder()
jr["sex"] = le.fit_transform(jr['Sex'])


inputs_n = jr.drop(['PassengerId','Survived','Name','Ticket','Cabin','Embarked','Sex'],axis='columns')
target = jr['Survived']
#print(inputs_n.info())
x = inputs_n
#print(x)
x_train,x_test, y_train, y_test = train_test_split(x,target,test_size=0.3) 

tre = DecisionTreeClassifier()

tre.fit(x_train,y_train)

pre = tre.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, pre))


fname = ['Pclass','Age','SibSp','Parch','Fare','sex']

dot_data = StringIO()
export_graphviz(tre, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = fname,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('survived.png')
Image(graph.create_png())

