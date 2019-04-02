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
df = pd.read_csv('1_A3_unemployments_by_district.csv')

# df.columns.values[0] = 'Regions'
# print(df.head(10))
# print(df.info())
# print(df.index)		# RangeIndex(start=0, stop=8, step=1)	# len(df.index) = 8
# print(df.keys())		# Index(['Unnamed: 0', '2015', '2016', '2017'], dtype='object')

# =============================================
# 2. Machine Learning		# DONE
# =============================================
model = LinearRegression()

X_train = df.columns[3:].values.reshape(-1, 1)
# print(X_train)
# print(X_train.shape)		#(5, 1)
y_train = np.transpose(df.iloc[:,3:].values)
# print(y_train)
# print(y_train.shape) 		# (5, 20)

model.fit(X_train, y_train)

X_test = np.arange(2018, 2021, 1).reshape(-1, 1)
y_pred = model.predict(X_test).round(2)

f=lambda a: (abs(a)+a)/2

y_pred = f(y_pred)
# print(y_pred)
# print(y_pred.shape)	# (3, 20)

print('Model Score: ', model.score(X_train, y_train) * 100, '%')

# =============================================
# 3. Export to csv, excel, json
# =============================================
# Combining two DataFrames
y_pred_tp = np.transpose(y_pred)
df_pred = pd.DataFrame(y_pred_tp, columns=np.arange(2018, 2021, 1))
# print(df_pred)

df_js = np.transpose(df)
# df_js.to_json('1_A3_unemployments_by_district_process.json')

df_concat = pd.concat([df, df_pred], axis=1)
# df_concat.to_csv('2_A3_unemployment_by_district_regr.csv', sep=',')
# df_concat.to_excel('2_A3_unemployment_by_district_regr.xlsx')

df_concat_js = np.transpose(df_concat)
# df_concat_js.to_json('2_A3_unemployment_by_district_regr_process.json')

# =============================================
# 4. Visualization
# =============================================

# Prepare X and y
X = np.arange(2013, 2018, 1)
# print(X)
# print(X.shape) 		# (5,)
y = np.transpose(df.iloc[:,3:])
# print(y)
# print(y.shape) 		# (5, 20)

X_concat = np.arange(2013, 2021, 1)
# print(X_concat)
# print('X_concat :', X_concat.shape) 		# (8,)
y_concat = np.transpose(df_concat.iloc[:,3:])
# print(y_concat)
# print('y_concat :', y_concat.shape) 		# (8, 20)

colors = [
	'red', 'red', 'green', 'green', 'blue', 'blue', 'black', 'black', 'brown', 'brown',
	'violet', 'violet', 'navy', 'navy', 'orange', 'orange', 'gold', 'gold', 'purple', 'purple',
]

# Plotting
plt.figure('A3_2_Unemployment Data')
plt.style.use('ggplot')

plt.subplot(121)
for i,c in zip(np.arange(0,20,1), colors):
	plt.plot(
		X,
		y.iloc[:, i],
		marker='o',
		markersize=3,
		linewidth=0.75,
		color=c,
	)
plt.title('Unemployment by District')
plt.xticks(X)

plt.subplot(122)
for i,c in zip(np.arange(0,20,1), colors):
	yd = y_concat.iloc[:, i]
	plt.plot(
		X_concat,
		yd,
		marker='*',
		markersize=3,
		linewidth=0.75,
		color=c
	)
plt.title('Prediction of Unemployment by District')

plt.legend(
	df_concat['District Name'],
	bbox_to_anchor=(1, 1),
)

plt.show()
plt.clf()