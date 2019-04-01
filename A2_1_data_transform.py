# =============================================	# =============================================
# 		Data Transformation CSV to CSV
# =============================================	# =============================================
import numpy as np
import pandas as pd
 
# =============================================
# 1. Read CSV		# DONE
# =============================================
# Import CSV into DataFrame
df = pd.read_csv('0_A2_immigrants_emigrants_by_age.csv')
df = df[['Year', 'Age', 'Immigrants', 'Emigrants']]

# print(df.Age[df.Age=='0-4'])

df.Age[df.Age=='0-4'] = '00-04'
df.Age[df.Age=='5-9'] = '05-09'

df.Age = 'Range ' + df.Age

# =============================================
# 2. Manipulate DataFrame	# DONE
# =============================================
# Cleaning, Manipulation

df = df.groupby(['Year', 'Age']).sum()
df = df.reindex(index=df.index[::-1])

print(df.head())
# print(df.info())


# =============================================
# 3. Write csv, excel		# DONE
# =============================================
# Export DataFrame

# df.to_csv('1_A2_immigrants_emigrants_by_age.csv', sep=',')
# df.to_excel('1_A2_immigrants_emigrants_by_age.xlsx')