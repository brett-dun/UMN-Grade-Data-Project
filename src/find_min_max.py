
import sys
import math
import pandas as pd
import numpy as np

def main():
	
	df = pd.read_csv(sys.argv[1])

	df2 = df.nsmallest(10, 'GPA')
	#print('Courses with the lowest GPA:')
	#print(df2)
	print('<table>')
	print('\t<tr>\n\t\t<th>Subject</th>\n\t\t<th>Course Number</th>\n\t\t<th>Average GPA</th>\n\t</tr>')
	for index, row in df2.iterrows():
		print('\t<tr>')
		print('\t\t<td>{}</td>\n\t\t<td>{}</td>\n\t\t<td>{:0.2f}</td>'.format(row['SUBJECT'], row['CATALOG_NBR'], row['GPA']))
		print('\t</tr>')
	print('</table>')


	#print('\nCourses with the lowest pass rate:')
	#print()
	df2 = df.nsmallest(12, 'PASS_RATE')

	print('<table>')
	print('\t<tr>\n\t\t<th>Subject</th>\n\t\t<th>Course Number</th>\n\t\t<th>Pass Rate</th>\n\t</tr>')
	for index, row in df2.iterrows():
		print('\t<tr>')
		print('\t\t<td>{}</td>\n\t\t<td>{}</td>\n\t\t<td>{:0.2f}%</td>'.format(row['SUBJECT'], row['CATALOG_NBR'], row['PASS_RATE']*100))
		print('\t</tr>')
	print('</table>')


	#print('\nCourses with the highest withdraw rate:')
	#print(df.nlargest(10, 'W_PERCENT'))
	df2 = df.nlargest(10, 'W_PERCENT')

	print('<table>')
	print('\t<tr>\n\t\t<th>Subject</th>\n\t\t<th>Course Number</th>\n\t\t<th>Withdrawl Percentage</th>\n\t</tr>')
	for index, row in df2.iterrows():
		print('\t<tr>')
		print('\t\t<td>{}</td>\n\t\t<td>{}</td>\n\t\t<td>{:0.2f}%</td>'.format(row['SUBJECT'], row['CATALOG_NBR'], row['W_PERCENT']*100))
		print('\t</tr>')
	print('</table>')

if __name__ == '__main__':
	main()