import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import time
DELAY = 0
counter = 1

#Downloads all syllabi iterating through all semesters from the official UT Syllabi Directory(2500+ files).
#Prevents repeat files and can recheck quickly.
#Takes 30 min - 1 hour to run the first time.

if not path.exists('syllabi'):
    print('Create the syllabi directory or change the path of the output files')

#Parses all semesters available from the options.
base_url = "https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/"
query = "?semester=&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
URL = base_url + query
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
semesters = soup.select('select[name=semester] > option')

#Iterate through courses for all semesters (first result is "Select", which is skipped).
for semester in semesters[1:]:
    s = semester['value']
    query = "?semester=" + s + "&department=&course_number=&course_title=&unique=&instructor_first=&instructor_last=&course_type=In%20Residence&search=Search"
    URL = base_url + query
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    #Find all links on the page.
    for links in soup.find_all('a', href=True):
        #For this website, links to syllabi are named "View".
        if "View" in links.contents[0]:
            full_link = base_url + links['href']
            print('Downloading syllabus #%d: %s' % (counter,full_link))
            name = 'syllabi/syllabus_' + links['href'].split('/')[1] + '.pdf'
            #Skip if the file has been downloaded already, otherwise, download as pdf.
            if path.exists(name):
                print('File already exists')
            else:
                r = requests.get(full_link, allow_redirects=True)
                print('Saving to %s' % name)
                with open(name, 'wb') as f:
                    f.write(r.content)
            counter = counter + 1
            #time.sleep(DELAY)