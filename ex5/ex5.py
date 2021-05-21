import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

# using list data
year = [2016,2015,2014,2013,2012,2011,2010,2009]

no_of_car_produced = [72105435,68539516,67782035,65745403,
63081024,59897273,58264852,47772598]

plt.plot(year, no_of_car_produced, color='green', marker='o')
plt.title("No of cars produced per year (cr)", fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('No of cars', fontsize=14)
plt.grid(True)
plt.show()

# using dict
car = {
        'year' : [2016,2015,2014,2013,2012,2011,2010,2009],

        'no_of_car_produced' : [72105435,68539516,67782035,65745403,63081024,59897273,58264852,47772598]
}
car_df= pd.DataFrame(car)
car_df.plot(x = 'year', y = 'no_of_car_produced',color='g',marker='*')
plt.title("No of cars produced per year (cr)", fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('No of cars', fontsize=14)
plt.grid(True)
plt.show()


# pie chart
data = {"percentage of internet users" : [51.8,14.8,12.8,9.5,6.8,3.7,0.6],

        "name of places" :['Asia','Europe', 'Africa' ,'Latin America and the Caribbean', 'North America', 'Middle East','Oceania and Australia'] 
        
        }
cf= pd.DataFrame(data,index=data['name of places'] )
cf.plot(kind='pie',y="percentage of internet users",autopct="%.2f")
plt.ylabel('')
plt.title('percentage of internet users', fontsize=14)
plt.show()


# bar chart
app = {
"app" :['TikTok','WhatsApp','Facebook','Instagram','Zoom','Messenger','Snapchat','Telegram','Google Meet','Netflix'] ,
"downloads" : [850,600,540,503,477,404,281,256,254,223]  }

app_df = pd.DataFrame(app)
app_df.plot(kind='bar',x="app",y="downloads",color='darkgreen')
plt.title('Most downloaded app of 2020 (in Million)', fontsize=14)
plt.show()


# scatter using dict 
trade = {

        'year' :[1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980] ,
        'usa' :[556310752881526,540524531055501,553846033570217,668385043665671,819612190445127,823227910907684,79808926173207,76542900319239,7947060702101,87590690791502,982645547013324]
        }
usa_trade = pd.DataFrame(trade)
usa_trade.plot(kind='scatter',x="year",y="usa",color='Blue')
plt.title('Trade', fontsize=14)
plt.ylabel('Goods', fontsize=14)
plt.show()

# scatter using csv
usa = pd.read_csv('usatrade.csv')

usa.plot(kind='scatter',x="year",y="usa",color='green')
plt.title('Trade', fontsize=14)
plt.ylabel('Goods', fontsize=12)
plt.show()
