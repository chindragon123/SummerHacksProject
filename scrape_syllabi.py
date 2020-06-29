import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import time
DELAY = 0
counter = 1

#Run this script in the directory that you would like to dump syllabi in.
#Downloads all syllabi iterating through all semesters from the official UT Syllabi Directory.
#Prevents repeat files and can recheck quickly.
#Takes 30 min - 1 hour to run the first time.

if not path.exists('syllabi'):
	print('Create the syllabi directory or change the path of the output files')

base_url = "https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/"
query = "?semester=&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
URL = base_url + query
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
subject_options = soup.select('select[name=semester] > option')

for semester in subject_options[1:]:
	s = semester['value']
	query = "?semester=" + s + "&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
	URL = base_url + query
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	
	for links in soup.find_all('a', href=True):
		if "View" in links.contents[0]:
			full_link = base_url + links['href']
			print('Downloading syllabus #%d: %s' % (counter,full_link))
			name = 'syllabi/syllabus_' + links['href'].split('/')[1] + '.pdf'
			if path.exists(name):
				print('File already exists')
			else:
				r = requests.get(full_link, allow_redirects=True)
				print('Saving to %s' % name)
				with open(name, 'wb') as f:
					f.write(r.content)
			counter = counter + 1
			#time.sleep(DELAY)