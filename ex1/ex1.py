#enna vaynumo atha import pannanum
import csv
import statistics
import numpy
#variable create pannanum 
li=[]
ans=0
count = 0

#file open panrom
with open("car.csv", "r") as file:

    car = csv.DictReader(file)
    #first row ahh print pandrom
    for row in car:
        print(row["Car"])
        li.append(row["Horsepower"])
        # 3 column ahh add pandrom
        ans += float(row["MPG"]) + float(row["Cylinders"]) + float(row["Horsepower"])
        # mothamaa yathuna row eruku 
        count += 1
# print print
print("Total of three columns 'MPG','Cylinders' and 'Horsepower' = ",ans)

print("Number of rows in a dataset = ",count)

# string ahh in ahh convert pandrom in a 'list'
for i in range(0, len(li)):
    li[i] = int(li[i])
# max and min ahh kandopudikom
maxx = max(li)
minn = min(li)
print("Maximum element in a column = ",maxx)
print("Minimum element in a column = ",minn)

# ethuku approm ella statistics function um pandrom
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
sd = statistics.stdev(li)
print("Standard Deviation = ",sd)
vary = statistics.variance(li)
print("Variance = ",vary)


# ethu 19 and 20 task 
# multimode and second mode kandopudikom 
own1 = statistics.multimode(li)
print("Multimode = ",own1)
rmod = statistics.mode(li)

while (li.count(rmod)):
    li.remove(rmod)

own2 = statistics.mode(li)
print("Second mode in a column = ",own2)

