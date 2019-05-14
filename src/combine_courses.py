
import sys
import math
import pandas as pd
import numpy as np

# calculate average gpa among students who took the class for a letter grade
def calculate_gpa(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else (row.A_COUNT*4.+row.B_COUNT*3.+row.C_COUNT*2.+row.D_COUNT) / count

# calculate the percentage of students that passed the class out of the total number of students
def calculate_pass_rate(row):
	return (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.S_COUNT+row.P_COUNT) / row['TOTAL HEADCOUNT']

# calculate the percentage of students that recieved an A out of the number of students who received a letter grade
def calculate_a_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else row['A_COUNT'] / count

# calculate the percentage of students that recieved a B out of the number of students who received a letter grade
def calculate_b_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else row['B_COUNT'] / count

# calculate the percentage of students that recieved a C out of the number of students who received a letter grade
def calculate_c_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else row['C_COUNT'] / count

# calculate the percentage of students that recieved a D out of the number of students who received a letter grade
def calculate_d_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else row['D_COUNT'] / count

# calculate the percentage of students that recieved an F out of the number of students who received a letter grade
def calculate_f_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return math.nan if count == 0 else row['F_COUNT'] / count

# calculate the percentage of students that withdrew from the class out of the total number of students
def calculate_w_percent(row):
	count = (row.A_COUNT+row.B_COUNT+row.C_COUNT+row.D_COUNT+row.F_COUNT)
	return row['W_COUNT'] / row['TOTAL HEADCOUNT']

def main():
	
	#read from csv
	df = pd.read_csv(sys.argv[1], thousands=',')

	#drop columns we don't care about
	df.drop(columns=['TERM','TERM_DESCR','INSTITUTION','CLASS_SECTION','COMPONENT_MAIN','INSTRUCTOR NAME','UM_JOBCODE_GROUP','JOBCODE','JOBCODE_DESCR'], inplace=True)

	#fill NAN with 0
	df.fillna(0, inplace=True)

	#convert columns from float to int
	cols = df.columns[df.dtypes == np.float64]
	df[cols] = df[cols].astype(np.int16)

	df['COMPLETED HEADCOUNT'] = df['COMPLETED HEADCOUNT'].astype(int)

	df = df.groupby(['SUBJECT','CATALOG_NBR']).agg({'DESCR':'first','COMPLETED HEADCOUNT':'sum','TOTAL HEADCOUNT':'sum','A_COUNT':'sum','B_COUNT':'sum','C_COUNT':'sum','D_COUNT':'sum','S_COUNT':'sum','P_COUNT':'sum','N_COUNT':'sum','F_COUNT':'sum','W_COUNT':'sum'}).reset_index()

	print(df.head())

	df['GPA'] = df.apply(calculate_gpa, axis=1)

	df['PASS_RATE'] = df.apply(calculate_pass_rate, axis=1)
	df['W_PERCENT'] = df.apply(calculate_w_percent, axis=1)

	df['A_PERCENT'] = df.apply(calculate_a_percent, axis=1)
	df['B_PERCENT'] = df.apply(calculate_b_percent, axis=1)
	df['C_PERCENT'] = df.apply(calculate_c_percent, axis=1)
	df['D_PERCENT'] = df.apply(calculate_d_percent, axis=1)
	df['F_PERCENT'] = df.apply(calculate_f_percent, axis=1)

	print(df.head())

	print(df.dtypes)

	df.to_csv(sys.argv[2], index=False)

if __name__ == '__main__':
	main()