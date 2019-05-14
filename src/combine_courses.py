
import sys
#import csv
import pandas
import numpy as np

def main():
	
	#read from csv
	df = pandas.read_csv(sys.argv[1], thousands=',')

	#drop columns we don't care about
	df.drop(columns=['TERM','TERM_DESCR','INSTITUTION','CLASS_SECTION','COMPONENT_MAIN','INSTRUCTOR NAME','UM_JOBCODE_GROUP','JOBCODE','JOBCODE_DESCR'], inplace=True)

	#fill NAN with 0
	df.fillna(0, inplace=True)

	#convert columns from float to int
	cols = df.columns[df.dtypes == np.float64]
	df[cols] = df[cols].astype(np.int16)

	df['COMPLETED HEADCOUNT'] = df['COMPLETED HEADCOUNT'].astype(int)

	print(df[ (df['SUBJECT']=='CSCI') & (df['CATALOG_NBR']=='1133') ])
	print(df[ (df['SUBJECT']=='CSCI') & (df['CATALOG_NBR']=='2011') ])

	df = df.groupby(['SUBJECT','CATALOG_NBR']).agg({'DESCR':'first','COMPLETED HEADCOUNT':'sum','TOTAL HEADCOUNT':'sum','A_COUNT':'sum','B_COUNT':'sum','C_COUNT':'sum','D_COUNT':'sum','S_COUNT':'sum','P_COUNT':'sum','N_COUNT':'sum','F_COUNT':'sum','W_COUNT':'sum'}).reset_index()

	#print(df[ (df['SUBJECT']=='CSCI') & (df['CATALOG_NBR']=='1133') ])
	#print(df[ (df['SUBJECT']=='CSCI') & (df['CATALOG_NBR']=='2011') ])
	print(df.head())

	print(df.dtypes)

	df.to_csv('fall_2018.csv')

if __name__ == '__main__':
	main()