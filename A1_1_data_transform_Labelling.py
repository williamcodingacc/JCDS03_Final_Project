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

# print(df_A1.head())
# print(df_A1.shape)
# print(df_A1.info())

# =============================================
# 3. Second CSV		# DONE
# =============================================

# Internal Source Dictionaries Load
Regions = pd.read_csv('mod_Regions.csv',
	index_col='Regions',
)

# Regions = Regions.fillna('Skip')
print(Regions)

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

# Region Labelling
df_A1['Region'] = df_A1.index.values

for x in df_A1['Region']:
	for y in Spain:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '0_Spain'
	for y in Europe_West:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '1_Europe_West'
	for y in Europe_East:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '2_Europe_East'			
	for y in Latin_Am:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '3_Latin_Am'
	for y in Anglofone:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '4_Anglofone'
	for y in Asia_Pacific:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '5_Asia_Pacific'
	for y in Asia_West:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '6_Asia_West'
	for y in CAF_Others:
		if df_A1['Region'][df_A1['Region']==x].values == y:
			df_A1['Region'][df_A1['Region']==x] = '7_CAF_Others'									
			
print(df_A1.head(15))

# Grouping
df_A1_Regional = df_A1
df_A1_Regional = df_A1_Regional.groupby(df_A1_Regional.Region).sum()
print(df_A1_Regional.head(10))

# =============================================
# 4. Write Second CSV		# DONE
# =============================================

# df_A1.to_csv('1_A1_immigrants_by_nationality_Labeled.csv', sep=',')