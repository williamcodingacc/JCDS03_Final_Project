# =============================================	# =============================================
# 		                    Data Visualization & Machine Learning
# =============================================	# =============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =============================================
# 1. Read CSV		# DONE
# =============================================
# Import CSV
df = pd.read_csv('1_A1_immigrants_by_region_tidy.csv')
df.columns.values[0] = 'Regions'
print(df.head(10))
# print(df.info())
# print(df.index)		# RangeIndex(start=0, stop=8, step=1)	# len(df.index) = 8
# print(df.keys())		# Index(['Unnamed: 0', '2015', '2016', '2017'], dtype='object')

# =============================================
# 2. Machine Learning		# DONE
# =============================================
model = LinearRegression()

X_train = df.columns[1:].values.reshape(-1, 1)
# print(X_train)
# print(X_train.shape)
y_train = np.transpose(df.iloc[:,1:].values)
# print(y_train)
# print(y_train.shape)
model.fit(X_train, y_train)

X_test = np.arange(2015, 2020, 1).reshape(-1, 1)
y_pred = model.predict(X_test).round(2)
# print(y_pred)

print('Model Score: ', model.score(X_train, y_train) * 100, '%')


# =============================================
# 3. Export to csv, excel, json
# =============================================
# Combining two DataFrames
y_pred_tp = np.transpose(y_pred[3:])
df_pred = pd.DataFrame(y_pred_tp, columns=np.arange(2018, 2020, 1))

df_concat = pd.concat([df, df_pred], axis=1)
df_concat.columns.values[0] = 'Regions'
df_concat = df_concat.set_index('Regions')

# df_concat.to_csv('2_A1_immigrants_by_region_regr_tidy.csv', sep=',')
# df_concat.to_excel('2_A1_immigrants_by_region_regr_tidy.xlsx')

df_concat_tp = df_concat.transpose()
# df_concat_tp.to_csv('2_A1_immigrants_by_region_regr_process.csv', sep=',')
# df_concat_tp.to_json('2_A1_immigrants_by_region_regr_process.json')

df_js = np.transpose(df)
# df_js.to_json('1_A1_immigrants_by_region_process.json')

# =============================================
# 4. Visualization
# =============================================
# Prepare X y
X = np.arange(2015, 2018, 1)
# print(X.shape)		# (3,)
y = np.transpose(df.iloc[:,1:])
# print(y.shape)		# (3, 8)

X_concat = np.arange(2015, 2020, 1)
# print(X_concat.shape)	# (5,)
y_concat = np.transpose(df_concat)
# print(y_concat.shape)	# (5, 8)

# Plotting

# plt.figure('A1_2_Immigration_Data')
# plt.style.use('ggplot')

# plt.subplot(121)
# plt.plot(
# 	X,
# 	y,
# 	marker='o',
# 	markersize=4,
# 	linewidth=0.75,
# )
# plt.title('Immigrants by Region')
# plt.xticks(X)

# plt.subplot(122)
# plt.plot(
# 	X_concat,
# 	y_concat,
# 	marker='*',
# 	markersize=4,
# 	linewidth=0.75,
# )
# plt.title('Prediction of Immigrants by Region')
# plt.xticks(X_concat)
# plt.legend(df.Regions, bbox_to_anchor=(1, 1))

# plt.show()


plt.figure('A1_2_Immigration_Data_Area')
plt.style.use('ggplot')

plt.subplot(121)
plt.stackplot(
	X,
	df.iloc[:,1:],
)
plt.title('Immigrants by Region')
plt.xticks(X)
plt.legend(df.Regions, loc='lower left',)

plt.subplot(122)
plt.stackplot(
	X_concat,
	df_concat,
)
plt.title('Prediction of Immigrants by Region')
plt.xticks(X_concat)
plt.legend(df.Regions, loc='lower left',)

plt.show()