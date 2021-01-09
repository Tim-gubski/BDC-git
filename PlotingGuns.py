import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

grads = []
guns = []

with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombinedGuns.csv", 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        if row[0].lower() == "kansas":
            grads.append(float(row[3]))
            guns.append(int(row[2]))

df = pd.read_csv(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombinedGuns.csv")

plt.subplots(figsize=(10, 6))
# plt.scatter(df['GrossAgriculture'],df['GraduationRate'],s=10)
plt.scatter(guns,grads,s=10)

m, b = np.polyfit(guns, grads, 1)

plt.plot(guns, m*pd.array(guns) + b, color="red")

plt.xlabel("Guns")
plt.ylabel("GradRate")


correlation_matrix = np.corrcoef(guns, grads)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)

plt.show()