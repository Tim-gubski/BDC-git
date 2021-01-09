import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

grads = []
agr = []

# font = {'family' : 'normal',
#         'weight' : 'bold',
#         'size'   : 15}
#
# plt.rc('font', **font)

with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombined.csv", 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        if row[2] != 'GrossAgriculture':
            grads.append(float(row[3]))
            agr.append(int(row[2]))

df = pd.read_csv(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombined2.csv")

plt.subplots(figsize=(10, 6))
# plt.scatter(df['GrossAgriculture'],df['GraduationRate'],s=10)
plt.scatter(agr,grads,s=10)

m, b = np.polyfit(agr, grads, 1)

plt.plot(agr, m*pd.array(agr) + b, color="red")

plt.xlabel("Gross Agricultural Sales",fontsize=20)
plt.ylabel("Graduation Rate",fontsize=20)

plt.title("Graduation Rate vs Gross Agricultural Sales",fontsize=20)

correlation_matrix = np.corrcoef(agr, grads)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)

plt.show()