import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import time
import csv
DELAY = 0
counter = 1

#Downloads all syllabi iterating through all semesters from the official UT Syllabi Directory(2500+ files).
#Prevents repeat files and can recheck quickly.
#Takes 30 min - 1 hour to run the first time.
#Stores associated course information of syllabi in a data file. Warning: Leading zeroes are cut off.
#Warning: deletes the contents of the data file. 
data = "courses.csv"
f = open(data, "w+")
f.close()

if not path.exists("syllabi"):
	print("Create the syllabi directory or change the path of the output files")

#Parses all semesters available from the options.
base_url = "https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/"
query = "?semester=&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
URL = base_url + query
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
semesters = soup.select("select[name=semester] > option")

#Iterate through courses for all semesters (first result is "Select", which is skipped).
for semester in semesters[1:]:
	s = semester["value"]
	query = "?semester=" + s + "&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
	URL = base_url + query
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	
	#Parses the main table that we are interested in.
	for table in soup.find_all("table",attrs={"border" : "1"}):
		#Ignores the first row, which is the header.
		for row in table.find_all("tr")[1:]:
			row_elements = []
			#Ignores the last column, which is the CIS results for the course.
			for td in row.find_all("td")[:-1]:
				if (len(td.contents) == 1):
					row_elements.append(td.contents[0])
				#Grabs the name of the instructor.
				elif (len(td.contents) == 5):
					for element in td.find_all("a"):
						row_elements.append(element.contents[0])
				#Downloads the syllabus.
				elif (len(td.contents) == 3):
					for link in td.find_all("a", href=True):
						full_link = base_url + link["href"]
						print("Downloading syllabus #%d: %s" % (counter,full_link))
						number = link["href"].split("/")[1]
						name = "syllabi/syllabus_" + number + ".pdf"
						#Skip if the file has been downloaded already, otherwise, download as pdf.
						if path.exists(name):
							print("File already exists")
						else:
							r = requests.get(full_link, allow_redirects=True)
							print("Saving to %s" % name)
							with open(name, "wb") as f:
								f.write(r.content)
						counter = counter + 1
						#time.sleep(DELAY)
						row_elements.append(number)
			#Writes to the data sheet.
			with open(data, "a") as csv_file:
				writer = csv.writer(csv_file)
				writer.writerow(row_elements)