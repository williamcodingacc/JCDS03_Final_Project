import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================
# 1. prepare CSV		# DONE
# =============================================
df = pd.read_csv('1_A2_immigrants_emigrants_by_age.csv')
df_melt = pd.melt(df,
	id_vars=['Year', 'Age'], 
	value_vars=['Immigrants', 'Emigrants'],
	var_name='Transmigration Type',
	value_name='Number'
	)
# print(df_melt.head())

df_ML = df_melt.pivot_table('Number', ['Age', 'Transmigration Type'], 'Year')
df_ML = df_ML.sort_index(ascending=False)
# print(df_ML.head())

# =============================================
# 2. write to CSV		# DONE
# =============================================
# df_ML.to_csv('1_A2_immigrants_emigrants_by_age_ML.csv')