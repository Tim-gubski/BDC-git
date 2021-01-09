import csv
import os

dir = "C:/Users/timgu/Downloads/BDC"
data = os.listdir(dir)

data = []
for i in os.listdir(dir):
    for file in os.listdir(dir + '/' + i):
        data.append(dir + '/' + i + '/' + file)


with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\combined.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "County", "Gross Sales in $"])
    for file in data:
        with open(file, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if "COMMODITY TOTALS - SALES, MEASURED IN $" in row:
                    writer.writerow([row[0], row[2], row[7]])


