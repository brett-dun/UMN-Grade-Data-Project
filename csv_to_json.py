
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

			subject = line[1]
			number = line[2]
			description = line[3]

			total_students = int(line[5])

			a = int(line[6])
			#print(a)
			b = int(line[7])
			#print(b)
			c = int(line[8])
			#print(c)
			d = int(line[9])
			#print(d)

			f = int(line[-2])
			#print(f)

			if (a+b+c+d+f) == 0:
				continue

			average = (a*4+b*3+c*2+d*1) / (a+b+c+d+f)

			if subject not in data:
				data[subject] = {}

			data[subject][number] = [description, average, total_students]

	with open('fall_2018.json', 'w') as file:

		json.dump(data, file, indent=4)

if __name__ == '__main__':
	main()