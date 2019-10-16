import numpy
import csv
import random
import pandas as pd

# Making the Dataset

problems = ["ram", "battery", "temperature", "disk"]
ram = ["change your ram", "upgrade your ram", "buy new laptop", "remove cookies", "reinstall os", "empty cache"]
battery = ["replace battery", "replace charger", "buy new laptop", "reinstall os"]
temperature = ["replace fan", "replace coolant", "buy cooler", "buy new laptop", "reinstall os", "empty disk"]
disk = ["Empty the recycle bin", "Delete temperory files", "Remove Unwanted Programs", "Delete recorded TV programs", "Defragment the hard drive", "Adjust system Restore Settings", "Reinstall Windows"]

#numpy.random.choice(numpy.arange(0, 26), p=[0.1, 0.09, 0.085, 0.082, 0.071, 0.062, 0.057, 0.054, 0.041, 0.039, 0.036, 0.034, 0.032, 0.031, 0.024, 0.023, 0.021, 0.017, 0.015, 0.014, 0.013, 0.012, 0.01175, 0.01175, 0.01175, 0.01175])
#numpy.random.choice(numpy.arange(0, 26), p=[0.0504, 0.0594, 0.0484, 0.0474, 0.0464, 0.0454, 0.0444, 0.0434, 0.0424, 0.0414, 0.0404, 0.0394, 0.0384, 0.0374, 0.0364, 0.0354, 0.0344, 0.0337, 0.0334, 0.0327, 0.0324, 0.0314, 0.0304, 0.0294, 0.0284, 0.0175])

list1 = []

#Ram(0-2000)
for i in range(0,2000):
    temp = []
    temp.append(problems[0])
    n1 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    n2 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    while(n1==n2):
        n2 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    temp.append(ram[n1])
    temp.append(ram[n2])
    list1.append(temp)
    
#Battery(2000-4000)
for i in range(2000,4000):
    temp = []
    temp.append(problems[1])
    n1 = numpy.random.choice(numpy.arange(0, 4), p=[0.3, 0.27, 0.23, 0.2])
    n2 = numpy.random.choice(numpy.arange(0, 4), p=[0.3, 0.27, 0.23, 0.2])
    while(n1==n2):
        n2 = numpy.random.choice(numpy.arange(0, 4), p=[0.3, 0.27, 0.23, 0.2])
    temp.append(battery[n1])
    temp.append(battery[n2])
    list1.append(temp)
    
#Temperature(4000-6000)
for i in range(4000, 6000):
    temp = []
    temp.append(problems[2])
    n1 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    n2 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    while(n1==n2):
        n2 = numpy.random.choice(numpy.arange(0, 6), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
    temp.append(temperature[n1])
    temp.append(temperature[n2])
    list1.append(temp)
    
#Disk(6000-8000)
for i in range(6000,8000):
    temp = []
    temp.append(problems[3])
    n1 = numpy.random.choice(numpy.arange(0, 7), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.03, 0.02])
    n2 = numpy.random.choice(numpy.arange(0, 7), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.03, 0.02])
    while(n1==n2):
        n2 = numpy.random.choice(numpy.arange(0, 7), p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.03, 0.02])
    temp.append(disk[n1])
    temp.append(disk[n2])
    list1.append(temp)

# Applying apriori
from apyori import apriori
rules = apriori(list1, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

list2 = sorted(results,key=lambda l:l[1], reverse=True)

list3 = []
for i in range(64):
    list3.append(list2[i][0])
    
list4 = [list(x) for x in list3]

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list4)


