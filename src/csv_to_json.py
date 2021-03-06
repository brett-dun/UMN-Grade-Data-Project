
import sys
import csv
import json

def main():

	data = {}
	
	with open(sys.argv[1]) as csv_file:

		reader = csv.reader(csv_file)

		first_line = True

		for line in reader:

			if first_line:
				first_line = False
				continue

			#print(line)

			subject = line[0]
			number = line[1]
			description = line[2]

			total_students = int(line[4])

			a = int(line[5])
			#print(a)
			b = int(line[6])
			#print(b)
			c = int(line[7])
			#print(c)
			d = int(line[8])
			#print(d)

			f = int(line[12])
			#print(f)

			count = a+b+c+d+f

			if count == 0:
				continue

			average = (a*4+b*3+c*2+d*1) / count

			#implement percentile information
			'''
			grades = ['F']*f + ['D']*d + ['C']*c + ['B']*b + ['A']*a
			ninetieth = grades[int(.9*count)]
			seventy_fifth = grades[int(.75*count)]
			twenty_fifth = grades[int(.25*count)]
			'''

			if subject not in data:
				data[subject] = {}

			data[subject][number] = [description, average, total_students, a/count, b/count, c/count, d/count, f/count]

	with open(sys.argv[2], 'w') as file:

		json.dump(data, file, indent=4)

if __name__ == '__main__':
	main()