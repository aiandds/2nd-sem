import pandas as pd
import numpy as np

df = pd.read_csv('Heart.csv')
df['Sex1'] = df.Sex.replace({1: "Male", 0: "Female"})
var = df.groupby("Sex1").agg({"Chol": [np.mean, np.std, np.size]})
print(var) 

mean_female = 261.75  #mean cholesterol of female
sd = 64.9             #standard deviation for female population
n = 97                #Total number of female
z = 1.96              #z-score from the z table mentioned before
se = sd /np.sqrt(n)   #using standard error for mean

# Construct the Confidence Interval
lcb = mean_female - (z* se)  #lower limit of the CI
ucb = mean_female + (z* se)  #upper limit of the CI
print("lower limit of the CI = ",lcb,"\nupper limit of the CI = ", ucb)



# male version 

df = pd.read_csv('Heart.csv')
df['Sex1'] = df.Sex.replace({1: "Male", 0: "Female"})
var = df.groupby("Sex1").agg({"Chol": [np.mean, np.std, np.size]})
print(var)  

mean_male = 239.6     #mean cholesterol of male
sd = 42.64            #standard deviation for male population
n =  206              #Total number of male
z = 1.96              #z-score from the z table mentioned before
se = sd /np.sqrt(n)   #using standard error for mean 

# Construct the Confidence Interval
lcb = mean_male - (z* se)  #lower limit of the CI
ucb = mean_male + (z* se)  #upper limit of the CI
print("lower limit of the CI = ",lcb,"\nupper limit of the CI = ", ucb)




# AHD

df = pd.read_csv('Heart.csv')
df['Sex1'] = df.Sex.replace({1: "Male", 0: "Female"})
df.groupby("Sex1").agg({"Chol": [np.mean, np.std, np.size]})
var = pd.crosstab(df.AHD, df.Sex1)
print(var)
pp_m = 114/(206)
#pm =103
n = 206	#size of male population
se_male = np.sqrt(pp_m * (1 - pp_m) / n) #using population proportion formula
z_score = 1.96	#for 95% confidence

lcb = pp_m - z_score* se_male #lower limit of the CI
ucb = pp_m + z_score* se_male #upper limit of the CI
print("lower limit of the CI = ",lcb,"\nupper limit of the CI = ", ucb)


#replace
#groupb
#agg
#crosstab
#z_score
'''
import statsmodels.api as sm
r = sm.stats.proportion_confint(n * p_fm, n)
print(r)
'''
