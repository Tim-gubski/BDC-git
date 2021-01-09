import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

df = pd.read_csv(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombined2.csv")

#fit simple linear regression model
model = ols('GraduationRate ~ GrossAgriculture', data=df).fit()

#view model summary
print(model.summary())

fig = plt.figure(figsize=(12,8))

#produce regression plots
fig = sm.graphics.plot_regress_exog(model, 'GrossAgriculture', fig=fig)


plt.show()