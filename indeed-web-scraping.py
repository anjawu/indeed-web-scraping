# https://realpython.com/beautiful-soup-web-scraper-python/#reader-comments

import requests
from bs4 import BeautifulSoup


URL = 'https://ca.indeed.com/jobs?q=software+developer&l=ontario'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id ='resultsCol')

# .prettify() lets you have easier viewing
#print(results.prettify())

# in comments are how to error check, will return which error you are receiving to help you further breakdown the problem.
def error_checking():
    if title_elem == None:
        print(f'{i+1}) Company: {company_elem.text.strip()}, \nJob title: not specified, \n{location_elem.text.strip()}\n\n, \nRemote: {remote_elem.text.strip()}')
        #print('Title error')
        return 'null'

    if company_elem == None:
        print(f'{i+1}) Company: not listed, \nJob title: {title_elem.text.strip()}, \n{location_elem.text.strip()}, \nRemote: {remote_elem.text.strip()} \n\n')
        #print('Company error')
        return 'null'

    if location_elem == None:
        #print('Location error')
        return 'div_location'

    if remote_elem == None:
        print(f'{i+1}) Company: {company_elem.text.strip()}, \nJob title: {title_elem.text.strip()}, \nLocation: {location_elem.text.strip()}, \nRemote: not specified \n\n')
        #print('Remote error')
        return 'null'


job_elems = results.find_all('div', class_ = 'jobsearch-SerpJobCard')

# tuple variables, first is the index number, second is the item; must put enumerate(list) to call both index and item.
for i, job_elem in enumerate(job_elems):
    title_elem = job_elem.find('h2', class_ = 'title')
    company_elem = job_elem.find('span', class_ = 'company')
    location_elem = job_elem.find('div', class_ = 'location')
    remote_elem = job_elem.find('span', class_ = 'remote')

    error = error_checking()

    if error == 'null':
        continue

# error if both location and remote are None. Since location is checked first the return will always be 'Location error' instead of 'Remote error', check if statment for remote-elem == None
    if error == 'div_location':
        location_elem = job_elem.find('span', class_ = 'location')
        if remote_elem == None:
            print(f'{i+1}) Company: {company_elem.text.strip()}, \nJob title: {title_elem.text.strip()}, \nLocation: {location_elem.text.strip()}, \nRemote: not specified \n\n')
        if remote_elem != None: 
            print(f'{i+1}) Company: {company_elem.text.strip()}, \nJob title: {title_elem.text.strip()}, \nLocation: {location_elem.text.strip()}, \nRemote: {remote_elem.text.strip()}\n\n')
        continue

    # try is to let the program go until you reach a problem. This saves time instead of doing breakpoint because you don't need to step through your whole program, just the broken part
    # try:	
    print(f'{i+1}) Company: {company_elem.text.strip()}, \nJob title: {title_elem.text.strip()}, \nLocation: {location_elem.text.strip()}, \nRemote: {remote_elem.text.strip()}\n\n')
    
    # except is when there becomes a problem with the try. breakpoint(), lets you stop and step through the program to find out what is wrong.
    # in this case breakpoint() allowed us to check each individual variable to see if it was None
    # except:
    #     breakpoint()




# data analysis intro: https://www.youtube.com/watch?v=cXP_i5-nTXg