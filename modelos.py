
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.info()

#repressão linear simples
# x = total_bill
# y = tip
x = df["total_bill"]
y = df["tip"]

#adicionar o intercepto

x = sm.add_constant(x)
modelo = sm.OLS(y, x).fit()
print(modelo.summary)