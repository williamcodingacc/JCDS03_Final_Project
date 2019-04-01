# =============================================	# =============================================
# 		Data Transformation CSV to CSV
# =============================================	# =============================================
import numpy as np
import pandas as pd

# =============================================
# 1. Read CSV		# DONE
# =============================================
# Import CSV into DataFrame
df_A1 = pd.read_csv('0_A1_immigrants_by_nationality.csv')
df_A1 = df_A1[['Year', 'Nationality', 'Number']]

# =============================================
# 2. Manipulate DataFrame	# DONE
# =============================================
# Cleaning, Manipulation

df_A1 = df_A1.groupby(['Nationality', 'Year']).sum()
df_A1 = df_A1.pivot_table('Number', ['Nationality'], 'Year')

list_Nationalities	= df_A1.index.values
list_Year			= df_A1.columns.values
df_A1.index		= list_Nationalities
df_A1.columns	= list_Year

df_A1 = df_A1.fillna(0)
df_A1 = df_A1.sort_values(by=[2017], ascending=False)

print(df_A1.columns.values[0])
print(df_A1.head())
# print(df_A1.shape)
# print(df_A1.info())

# =============================================
# 3. Write CSV, excel		# DONE
# =============================================
# Export DataFrame

# df_A1.to_csv('1_A1_immigrants_by_nationality_tidy.csv', sep=',')
# df_A1.to_excel('1_A1_immigrants_by_nationality_tidy.xlsx')

# =============================================
# 4. Second CSV		# DONE
# =============================================

# Internal Source Dictionaries Load
Regions = pd.read_csv('mod_Regions.csv',
	index_col='Regions',
)
# print(Regions)

# Allocate Regions
Spain		= Regions.loc['Spain']
Europe_West	= Regions.loc['Europe_West']
Europe_East	= Regions.loc['Europe_East']
Latin_Am	= Regions.loc['Latin_America']
Anglofone	= Regions.loc['Anglofone']
Asia_Pacific= Regions.loc['Asia_Pacific']
Asia_West	= Regions.loc['Asia_West']
CAF_Others	= Regions.loc['Africa_Others']

zipped_Regions = zip(Spain, Europe_West, Europe_East, Latin_Am, Anglofone, Asia_Pacific, Asia_West, CAF_Others)
# Region_Labels = ['Spain', 'Europe_West', 'Europe_East', 'Latin_Am', 'Anglofone', 'Asia_Pacific', 'Asia_West', 'CAF_Others']

# Rename Index

df_A1_Regional = df_A1

for esp,a,b,c,d,e,f,g in zipped_Regions:
	df_A1_Regional = df_A1_Regional.rename(
		{
			"{}".format(esp): "0_Spain",
			"{}".format(a): "1_Europe_West",
			"{}".format(b): "2_Europe_East",
			"{}".format(c): "3_Latin_Am",
			"{}".format(d): "4_Anglofone",
			"{}".format(e): "5_Asia_Pacific",
			"{}".format(f): "6_Asia_West",
			"{}".format(g): "7_CAF_Others",
		},
		axis='index',
	)

# print(df_A1_Regional.head(10))

# Grouping by sum
df_A1_Regional = df_A1_Regional.groupby(df_A1_Regional.index).sum()
# print(df_A1_Regional.head(20))

df_A1_Reg_transposed = df_A1_Regional.transpose()
print(df_A1_Reg_transposed)

# =============================================
# 5. Write Second CSV		# DONE
# =============================================

# df_A1_Regional.to_csv('1_A1_immigrants_by_region_tidy.csv', sep=',')
# df_A1_Regional.to_excel('1_A1_immigrants_by_region_tidy.xlsx')

# df_A1_Reg_transposed.to_csv('1_A1_immigrants_by_region_process.csv', sep=',')