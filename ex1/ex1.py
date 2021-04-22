import csv

with open("cars.csv", "r") as file:
    car = csv.reader(file)
    next(car)
    for row in car:
        print(row[1])
