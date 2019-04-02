# =============================================	# =============================================
# 		                    Data Visualization & Machine Learning
# =============================================	# =============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import seaborn as sns

# =============================================
# 1. Read CSV		# DONE
# =============================================
# Import CSV
df = pd.read_csv('1_A2_immigrants_emigrants_by_age_ML.csv')
# df = df.drop(['Unnamed: 0'], axis=1)
# print(df.head())

# =============================================
# 2. Machine Learning		# DONE
# =============================================
model = LinearRegression()
# model = LinearRegression()

X_train = df.columns[2:].values.reshape(-1, 1)
# print(X_train)			# 15 sampai 17
# print(X_train.shape)        # (3, 1)
y_train = np.transpose(df.iloc[:,2:].values)
# print(y_train)
# print(y_train.shape)        # (3, 42)
model.fit(X_train, y_train)

X_test = np.arange(2018, 2021, 1).reshape(-1, 1)
# print(X_test)				# 18 sampai 20
# print(X_test.shape)         # (3, 1)
y_pred = model.predict(X_test).round(2)
# print(y_pred)
# print(y_pred.shape)         # # (3, 42)
f=lambda a: (abs(a)+a)/2
y_pred = f(y_pred)

print('Model Score: ', model.score(X_train, y_train) * 100, '%')

# =============================================
# 3. Export to csv, excel, json
# =============================================
# Combining two DataFrames
y_pred_tp = np.transpose(y_pred)
df_pred = pd.DataFrame(y_pred_tp, columns=np.arange(2018, 2021, 1))
# print(df_pred)
df_concat = pd.concat([df, df_pred], axis=1)
df_concat.Age = df_concat.Age.str.replace('Range' , '')
# print(df_concat.head())

# df_concat = df_concat.set_index('Regions')

# df_concat.to_csv('2_A2_immigrants_emigrants_by_age_ML_regr.csv', sep=',')
# df_concat.to_excel('2_A2_immigrants_emigrants_by_age_ML_regr.xlsx')

# df_js = np.transpose(df)
# df_js.to_json('2_A2_immigrants_emigrants_by_age_ML_regr.json')

# =============================================
# 4. Prepare Prediction Data for easier plotting
# =============================================

df_2018 = df_concat.pivot_table(
	[2018],
	['Age'],
	['Transmigration Type'],
)
df_2018 = df_2018.sort_index(ascending=False)
df_2018['Year'] = 2018

df_2019 = df_concat.pivot_table(
	[2019],
	['Age'],
	['Transmigration Type'],
)
df_2019 = df_2019.sort_index(ascending=False)
df_2019['Year'] = 2019

df_2020 = df_concat.pivot_table(
	[2020],
	['Age'],
	['Transmigration Type'],
)
df_2020 = df_2020.sort_index(ascending=False)
df_2020['Year'] = 2020

# =============================================
# 5. Export Prediction Data to CSV
# =============================================

# df_2018.to_csv(
# 	'A2_3_pred_2018.csv', sep=',',
# 	header=['Emigrants', 'Immigrants', 'Year']
# )
# df_2019.to_csv(
# 	'A2_3_pred_2019.csv', sep=',',
# 	header=['Emigrants', 'Immigrants', 'Year']
# )
# df_2020.to_csv(
# 	'A2_3_pred_2020.csv', sep=',',
# 	header=['Emigrants', 'Immigrants', 'Year']
# )