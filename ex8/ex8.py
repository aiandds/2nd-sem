import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv('FuelConsumption.csv')
fuel = df[["ENGINESIZE","CO2EMISSIONS"]]
#print(fuel)
fuel.plot(x="ENGINESIZE",y="CO2EMISSIONS",color='ForestGreen',kind='scatter')
plt.xlabel("ENGINE SIZE")
plt.ylabel("C02 EMISSIONS")
plt.title('Engine Wise C02 Emission',color = 'Chocolate')
plt.show()

train=fuel[:(int((len(fuel)*0.8)))]
test=fuel[(int((len(fuel)*0.8))):]
regr=LinearRegression()
train_x=np.array(train[["ENGINESIZE"]])
train_y=np.array(train[["CO2EMISSIONS"]])
regr.fit(train_x,train_y)
print ("Slope = ",regr.coef_)
print ("Intercept = ",regr.intercept_)

plt.scatter(train["ENGINESIZE"],train["CO2EMISSIONS"],color='coral')
plt.plot(train_x,regr.coef_*train_x+regr.intercept_,color='purple')
plt.xlabel("ENGINE SIZE")
plt.ylabel("CO2 EMISSIONS")
plt.title('Engine Wise C02 Emission',color = 'Chocolate')
plt.show()



#using heart.csv
df = pd.read_csv('Heart.csv')

chol = df[["Age","Chol"]]


chol.plot(x="Age",y ="Chol",color='ForestGreen',kind='scatter')
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.title('Cholesterol Level',color = 'Chocolate')
plt.show()


train=chol[:(int((len(chol)*0.8)))]
test=chol[(int((len(chol)*0.8))):]
regr=LinearRegression()
train_x=np.array(train[["Age"]])
train_y=np.array(train[["Chol"]])

regr.fit(train_x,train_y)
print ("Slope = ",regr.coef_)
print ("Intercept = ",regr.intercept_)

plt.scatter(train["Age"],train["Chol"],color='coral')
plt.plot(train_x,regr.coef_*train_x+regr.intercept_, color='purple')
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.title('Cholesterol Level',color = 'Chocolate')
plt.show()




