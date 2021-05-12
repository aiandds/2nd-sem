
import pandas as pd
import matplotlib.pyplot as pt

data_set =  {   'cars': ["BENZ", "ROLS", "AUDI"],
                'RS': [1.2, 2.5, .5]
            }
ans = pd.DataFrame(data_set) 
print(ans,'\n')

print("locate specific row\n",ans.loc[[0, 1]],'\n')

ind = pd.DataFrame(data_set, index = ["1998", "1997", "2020"])
print("value to index\n",ind,'\n')

food = pd.read_csv('food.csv')
head = food.head()
print("top record\n",head,'\n')

bot = food.tail()
print("Bottom Record\n",bot,'\n')

print("information about our data\n",ans.info(),'\n')

#data cleaning 

noemp = food.dropna()

print("non empty dataset\n",noemp,'\n')

ad_value = food.fillna(120)
print("add value to empty cell\n",ad_value,'\n')

dt_time = pd.to_datetime(food['Period'])
print("convert to date and time\n",dt_time,'\n')

food.loc[1,'Period']= 77
print("locate and replace\n",food,'\n')

food.drop_duplicates(inplace=True)
print("remove duplicates\n",food,'\n')

co=food.corr()
print("correlation between Period and Data_value\n",co,'\n')


# plotting 

carzz = pd.read_csv('car.csv')

#carzz.plot(x='city-mpg',y='highway-mpg')
carzz['city-mpg'].plot(color = 'r')
carzz['highway-mpg'].plot(color = 'g')
pt.show()
