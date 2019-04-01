import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# =============================================
# 1. Read CSV		# DONE
# =============================================
df = pd.read_csv('1_A2_immigrants_emigrants_by_age.csv')
df.Age = df.Age.str.replace('Range' , '')
df_2017 = df[df.Year==2017]
df_2016 = df[df.Year==2016]
df_2015 = df[df.Year==2015]
# print(df.head())

df_2018 = pd.read_csv('A2_3_pred_2018.csv')
df_2019 = pd.read_csv('A2_3_pred_2019.csv')
df_2020 = pd.read_csv('A2_3_pred_2020.csv')

# =============================================
# 2. Plotting
# =============================================
# Pyramid Plotting
list_df = [df_2015, df_2016, df_2017, df_2018, df_2019, df_2020]
data_range = np.arange(2015, 2021, 1)
axes_range = np.arange(0, 6, 1)

fig1, axes = plt.subplots(ncols=6)
sns.set(style="whitegrid")
sns.set_color_codes("bright")

for i, j, k in zip(list_df, data_range, axes_range):
	sns.barplot(
		x="Immigrants", y="Age", data=i,
		color="navy",
		ax=axes[k],
		alpha=0.55,
		saturation=1.1,
		label='Immigration',
	)
	sns.barplot(
		x="Emigrants", y="Age", data=i,
		color="orange",
		ax=axes[k],
		alpha=0.55,
		saturation=1.1,
		label='Emigration',
	)
	axes[k].set(xlabel='Number', ylabel='Age Range')
	axes[k].legend(loc="upper right", frameon=True)
	axes[k].set_title("Immi/Emi \n ({})".format(j))

sns.despine(left=True, bottom=True)

plt.show()
plt.clf()