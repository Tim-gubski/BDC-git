import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

df = pd.read_csv(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombined.csv")

# plt.rc('xtick',labelsize=13)
# plt.rc('ytick',labelsize=13)


fig = plt.figure(figsize=(12,8))

# plt.boxplot(df["GraduationRate"])

df.boxplot(column='GraduationRate', by='State', fontsize=13)

plt.show()