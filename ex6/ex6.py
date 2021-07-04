import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
from scipy.stats import skew
import seaborn as sns

df = pd.DataFrame([[10,20,30,40], [7,14,21,28],[55,15,8,12],
                    [15,14,1,8],[7,1,1,8],[5,4,9,2]],
                    columns=['Apple','Orange','Banana','Pear'],
                    index=['Basket1','Basket2','Basket3','Basket4','Basket5','Basket6'])

print(df)
print("The Mean is")
print(df.mean())
print("The Median is")
print(df.median())
print("The Mode is")
print(df.mode())
print("The Variance is")
print(df.var())
print("The Standard Deviation is")
print(df.std())
print("The Skew is")
print(df.skew())

for col in df:
    print(col)
    print(df[col])
    
    print(skew(df[col]))
    
    plt.figure()
    sns.distplot(df[col])

    plt.show()
    
for col in df:
    print(col)
    print(df[col])
    
    print(kurtosis(df[col]))
    
    plt.figure()
    sns.distplot(df[col])
    
    plt.show()

print("The Kurtosis is")
print(df.kurtosis())
print("The 0th Moment is")
print(stats.moment(df,moment=0))
print("The 1st Moment is")
print(stats.moment(df,moment=1))
print("The 2nd Moment is")
print(stats.moment(df,moment=2))


df.plot(y='Apple',marker='o')
df.mode().plot()
plt.show()



print('\n\n\n\n\n')

# using  csv 
data=pd.read_csv("country_wise_latest.csv")
df=pd.DataFrame(data)
print("The Mean is")
print(df['Confirmed'].mean())
print("The Median is")
print(df['Confirmed'].median())
print("The Mode is")
print(df['Confirmed'].mode())
print("The Variance is")
print(df['Confirmed'].var())
print("The Standard Deviation is")
print(df['Confirmed'].std())
print("The Skew is")
print(df['Confirmed'].skew())
print("The Kurtosis is")
print(df['Confirmed'].kurtosis())
print("The 0th Moment is")
print(stats.moment(df['Confirmed'],moment=0))
print("The 1st Moment is")
print(stats.moment(df['Confirmed'],moment=1))
print("The 2nd Moment is")
print(stats.moment(df['Confirmed'],moment=2))

