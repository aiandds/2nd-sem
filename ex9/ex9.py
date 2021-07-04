import pandas as pd
import matplotlib.pyplot as plt


ex = pd.read_csv("diet_gym.csv")
#print(ex)
ex['Month'] = pd.to_datetime(ex['Month'])
print(ex.info())
ex.set_index("Month", inplace = True)
print(ex)
ex.plot()
plt.show()
ax = ex['Diet'].plot()
ax.legend(loc='upper right')
#print(Fig)

plt.show()

ax = ex['Diet'].plot()
ax = ex['Diet'].rolling(12).mean().plot()
ax.legend(loc='upper right')
plt.show()


correlation = ex.diff().corr()
print(correlation)
ax = ex['Gym'].rolling(12).mean().plot()
ax = ex['Diet'].rolling(12).mean().plot()
ax.legend(loc='upper right')
plt.show()
