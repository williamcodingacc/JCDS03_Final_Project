# =============================================	# =============================================
# 		Data Transformation CSV to CSV
# =============================================	# =============================================
import numpy as np
import pandas as pd

# =============================================
# 1. Read CSV		# DONE
# =============================================
# Import CSV into DataFrame
df_A3 = pd.read_csv('0_A3_unemployment.csv')
# print(df_A3.columns)
# Index(['Year', 'Month', 'District Code', 'District Name', 'Neighborhood Code',
#        'Neighborhood Name', 'Gender', 'Demand_occupation', 'Number'],
#       dtype='object')

df_A3 = df_A3[['Year', 'District Code', 'District Name', 'Number', 'Gender']]
# print(df_A3.head())

# =============================================
# 2. Manipulate DataFrame	# DONE
# =============================================
# Cleaning, Manipulation
df_A3 = df_A3.fillna(0)

# Pivoting
df_A3 = df_A3.pivot_table(
	['Number'],
	['District Code', 'District Name', 'Gender'],
	['Year'],
	aggfunc='mean',
)
df_A3 = df_A3.round(1)
# print(df_A3.head())

list_Year = np.arange(2013, 2018, 1)
df_A3.columns = list_Year

df_A3 = df_A3.drop([99])

# =============================================
# 3. Write csv, excel		# DONE
# =============================================
# Export DataFrame into CSV, Excel

# df_A3.to_csv('1_A3_unemployments_by_district.csv', sep=',')
# df_A3.to_excel('1_A3_unemployment_by_district.xlsx')