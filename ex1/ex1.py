#importing necessary library
import csv
import statistics
import numpy
# creating variables and list 
li=[]
ans = 0
count = 0

# open file 
with open("car.csv", "r") as file:

    car = csv.reader(file)
    next(car)
    for row in car:
        # print first row 
        print(row[0])
        
        # adding vale to that list
        if(row[4] != '0' and row[4] != '' ):
            li.append(row[4])
        # adding 3 column 
        ans += float(row[1]) + float(row[2]) + float(row[4])
        # to find tot num of row
        count += 1
# total of 3 column
print("Total of three columns 'MPG','Cylinders' and 'Horsepower' = ",ans)
#print total number of row 
print("Number of rows in a dataset = ",count)

# converting string into int in the list 
for i in range(0, len(li)):
    li[i] = int(li[i])
# find max and min 
maxx = max(li)
minn = min(li)
print("Maximum element in a column = ",maxx)
print("Minimum element in a column = ",minn)

# calculate necessary statistics value and print the value 
meann = statistics.mean(li)
print("Mean = ",meann)

med = statistics.median(li)
print("Median = ", med)

modd = statistics.mode(li)
print("Mode = ",modd)

fm = statistics.fmean(li)
print("fmean = ",fm)

hm = statistics.harmonic_mean(li)
print("Harmonic mean = ",hm)

gm = statistics.geometric_mean(li)
print("Geometric mean = ", gm)

ml = statistics.median_low(li)
print("Median low = ",ml)

mh = statistics.median_high(li)
print("Median high = ",mh)

pt = numpy.percentile(li,100)
print("Percentile = ",pt)

qt = numpy.quantile(li, .25)
print("Quantile = ",qt)

nanme = numpy.nanmean(li)
print("nanmean = ",nanme)

sd = numpy.std(li)
print("Standard Deviation = ",sd)

vary = statistics.variance(li)
print("Variance = ",vary)

# median_grouped and multimode in the column
own1 = statistics.median_grouped(li)
print("Median_grouped = ",own1)

own2 = statistics.multimode(li)
print("Multimode = ",own2)
