import numpy as np
import pandas as pd
import io

# filenames = [
# 	"22_23.csv",
# 	"23_24.csv",
# 	"24_25.csv",
# 	"25_26.csv"
# ]

# df22_23 = pd.read_csv("22_23.csv")
# df23_24 = pd.read_csv("23_24.csv")
# df24_25 = pd.read_csv("24_25.csv")
# df25_26 = pd.read_csv("24_25.csv")

# global_df = pd.concat([df22_23, df24_25, df24_25, df25_26],axis=0)
# print(global_df)
# global_df.to_csv('global.csv', index=False)

players = ['Caia','Devin','Jacen','Zoë']
global_df = pd.read_csv('global.csv')
df = global_df.replace('_', np.nan)

print(df.isna().count())

def calc_total_points(value_counts):
	total = 0
	chicken = 0
	for w, c in value_counts.items():
		if w != "0":
			total += int(w) * c
		else:
			chicken += c
	return total, chicken


for p in players:
	print("------",p,"-------")
	print(df[p].value_counts())
	points, chicken = calc_total_points(df[p].value_counts())
	print(f"Total Points: {points}, Chicken hands: {chicken}")
	print('\n')

# print(repr(df['Devin'].mean()))


