import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# =============================================
# 1. Read CSV				# DONE
# =============================================
df = pd.read_csv('1_B1_immigrants_by_nationality_Labeled.csv')

# print(df.head())
df_Spain	= df[df.Region=='0_Spain']
df_EuroWest	= df[df.Region=='1_Europe_West']
df_EuroEast	= df[df.Region=='2_Europe_East']
df_LatAm 	= df[df.Region=='3_Latin_Am']
df_Anglo	= df[df.Region=='4_Anglofone']
df_AsiaPac	= df[df.Region=='5_Asia_Pacific']
df_AsiaWest	= df[df.Region=='6_Asia_West']
df_Africa	= df[df.Region=='7_CAF_Others']


# =============================================
# 2. Visualization of Original Data
# =============================================
list_df			= [df_Spain, df_EuroWest, df_EuroEast, df_LatAm, df_Anglo, df_AsiaPac, df_AsiaWest, df_Africa]
list_figtitle	= ['Spain', 'West Europe', 'East Europe', 'Latin America', 'Anglofone', 'Asia Pacific', 'West Asia', 'Africa']

# for a,b in zip(list_df, list_figtitle) :
# 	X = np.arange(2015, 2018, 1)
# 	# print(X.shape)		# (3,)
# 	y = np.transpose(a.iloc[:,1:-1])
# 	# print(y.shape)		# (3, 8)
# 	legend_ori = a.iloc[:,0]

# 	plt.figure('B1_2_Immigration_Data {}'.format(b))
# 	plt.style.use('ggplot')
# 	plt.plot(
# 		X,
# 		y,
# 		marker='o',
# 		markersize=4,
# 		linewidth=0.75,
# 	)
# 	plt.title('Immigrants by Nationality from {}'.format(b))
# 	plt.xticks(X)
# 	plt.legend(legend_ori, bbox_to_anchor=(1, 1))
# 	plt.show()


# =============================================
# 3. Machine Learning and Visualization (Compile All)
# =============================================
for a,b in zip(list_df, list_figtitle) :
	# Original
	X = np.arange(2015, 2018, 1)
	y = np.transpose(a.iloc[:,1:-1])
	legend_ori = a.iloc[:,0]

	plt.figure('B1_2_2_Immigration_Data_ML {}'.format(b))
	plt.style.use('ggplot')
	plt.plot(
		X,
		y,
		marker='o',
		markersize=4,
		linewidth=0.75,
	)
	plt.title('Immigrants by Nationality from {}'.format(b))

	# Prediction
	model = LinearRegression()

	X_train = a.columns[1:-1].values.reshape(-1, 1)
	y_train = np.transpose(a.iloc[:,1:-1].values)
	model.fit(X_train, y_train)

	X_test = np.arange(2015, 2020, 1).reshape(-1, 1)
	y_pred = model.predict(X_test).round(2)
	y_pred_tp = np.transpose(y_pred)
	df_pred = pd.DataFrame(y_pred_tp, columns=np.arange(2015, 2020, 1))

	X_regr = np.arange(2015, 2020, 1)
	y_regr = np.transpose(df_pred)

	plt.plot(
		X_regr,
		y_regr,
		marker='*',
		markersize=4,
		linewidth=0.75,
	)
	plt.title('Prediction of Immigrants by Nationality from {}'.format(b))
	plt.xticks(X_regr)
	plt.legend(legend_ori, bbox_to_anchor=(1, 1))

	plt.show()