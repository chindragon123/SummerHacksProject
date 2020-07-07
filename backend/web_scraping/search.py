import csv
import sys

#The search method can use by another script to retrieve a list of courses that have a matching keyword in any entry of a row.
#The id of the corresponding syllabus of any particular result is found in the 7th column (the 6th index i.e. row[6]).

def search(input):
	csv_file = csv.reader(open('courses.csv', "r"), delimiter=",")

	results = []
	for row in csv_file:
		for element in row:
			if element.find(input) > -1:
				results.append(row)
	return results

def main():
	keyword = input("Enter a keyword:\n")
	print(search(keyword))

if __name__ == "__main__":
    main()