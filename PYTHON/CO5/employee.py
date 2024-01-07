import csv
with open('Employee.csv','r')as file1:
	reader = csv.reader(file1)
	for row in reader:
		print(row)
		
