#importing necessary library
import numpy as np
import random 

#computation operations
#creating 2 x 2 array with arange
a = np.arange(5,25,5).reshape(2,2)
b = np.arange(2,-16,-4.5).reshape(2,2)
#printing the array
print("Elements of array a \n",a)
print("Elements of array b \n",b)

#adding a and b array
ad=np.add(a,b)
print("Addition of 'a' and 'b' \n",ad)

#changing the array with power 2
po = np.power(a,2)
print("A square \n",po)

#using floor division in array 'a'
fl = np.floor_divide(a,3)
print("floor division of array 'a' with 3\n",fl)

#finding sin value for array 'a'
sn = np.sin(a*np.pi/180)
print("sin value of 'a'\n",sn)

#getting absolute value for array 'b'
ab = np.abs(b)
print("obsolute value of 'b'\n",ab)

# 7 getting value with exp function
np.set_printoptions(suppress=True)
ex = np.exp2(a)
print("square of array 'a' with exp function\n",ex)

# finding log10 for array 'a'
lo = np.log10(a)
print("log10 of array 'a'\n",lo)

#finding modulus  for array 'a' with 10
modd = np.mod(a,10)
print("modulus for array 'a' with 10\n",modd,'\n')


# aggregation operations
# generating random int
r = np.random.randint(1,9, size=(3,3))
print("Random int\n",r)

#calculating sum
rr = np.sum(r)
print("sum of array 'r'\n",rr)

#finding min in r
minn = np.min(r)
print("min value in array 'r'\n",minn)
#finding max in r
maxx = np.max(r,axis=0)
print("max value in array 'r' with axis '0'\n",maxx)

#finding argmin in r
argminn = np.argmin(r)
print("min value indices in array 'r'\n",argminn)

#finding argmax in r
argmaxx =np.argmax(r)
print(" max value indices in array 'r'\n",argmaxx)

#finding median in r
med = np.median(r)
print("median value in array 'r'\n",med)

#finding mean in r
menn = np.mean(r)
print("mean value in array 'r'\n",menn)

#finding std in r
std = np.std(r)
print("standard deviation in array 'r'\n",std)

#calculating product of r
pod = np.prod(r)
print("product value in array 'r'\n",r)

#calculate variance in r
prcn = np.var(r)
print("variance in array 'r'\n",prcn,"\n\n")

#sorting 
#creating ramdon int
srk = np.random.randint(12,44,size=(2,2))
print("array with Random value \n",srk)
#sorting srk array
s1 = np.sort(srk,axis=None).reshape(2,2)
print("sorted array \n",s1)
#finding indices of shorted array
s2 = np.argsort(srk,axis=None).reshape(2,2)
print("indices value for sorted array\n",s2,"\n\n")

#structured data 
car = ["Benz","bmw","Rols","Bent"]
model = ["amg gt R","i8","ghost","conti"]
rate = [25,20,40,19]


modell = np.zeros(4,dtype={'names': ['col1', 'col2','col3'], 'formats': ['U40', 'U40','i4']})
modell["col1"] = car
modell["col2"] = model
modell["col3"] =rate
print("structured data\n",modell)
