import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# =============================================
# 1. Read CSV		# DONE
# =============================================
df = pd.read_csv('1_A2_immigrants_emigrants_by_age.csv')

df.Age = df.Age.str.replace('Range ' , '')

df_melt = pd.melt(df,
	id_vars=['Year', 'Age'], 
	value_vars=['Immigrants', 'Emigrants'],
	var_name='Transmigration Type',
	value_name='Number'
	)

# print(df.head())
# print(df_melt.head())

# =============================================
# 2. # Write to csv, excel	# DONE
# =============================================

# df_melt.to_csv('1_A2_immigrants_emigrants_by_age_process.csv', sep=',')
# df_melt.to_excel('1_A2_immigrants_emigrants_by_age_process.xlsx')

# =============================================
# 3. Plotting
# =============================================
# EDA
sns.pairplot(df, hue="Year")

# Violin Plot
fig2 = plt.subplots(ncols=1)
sns.set(style="whitegrid", palette="pastel", color_codes=True)

sns.violinplot(
    x="Year",
	y="Number",
	hue="Transmigration Type",
    split=True, inner="quart",
	data=df_melt,
)

sns.despine(left=True)

plt.show()
plt.clf()