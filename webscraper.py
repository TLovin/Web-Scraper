import bs4 as bs
import urllib.request
import time
import grequests

#stacastic training
#gradient descent
#genetic algorithms

######## disables ssl certification. You might be able to remove this part.

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#########



time1 = time.time()

links = ['https://beta.images.theglobeandmail.com/static/interactive/sunshine-list/2015/2015-sunshine-list.csv']


requests = [grequests.get(link) for link in links]  # creates a list of unsent requests
responses = grequests.map(requests)  # send requests without waiting for the previous one to finish

for response in responses:
    soup = bs.BeautifulSoup(response.text, 'lxml')  # parsing text

    for paragraph in soup.find_all('p'):
        scraped_data = open('ScrapedData.txt', 'a') # save to file scraped_data
        try:
            scraped_data.write(paragraph.text)
        except:
            continue
        print(paragraph.text)
    scraped_data.close()
        
#         print(paragraph.text)  #this returns all paragraphs in unicode form
#         print(soup.get_text())  # gets all the text on the page (even in tables)
#
#
# print(soup.title.text)  #finds the title of the article
#
# for url in soup.find_all('a'):
# print(url.get('href'))  # gets all the links without tags


time2 = time.time()
print(time2-time1)
