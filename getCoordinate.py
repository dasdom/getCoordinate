

import requests, bs4, sys

def element_for(url, selection_string):
    print("Fetching", url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # print("selecting", selection_string)
    return soup.select(selection_string)

city = sys.argv[1]

url = 'https://en.wikipedia.org/wiki/' + city
element = element_for(url, 'td > span > a')

url = 'http:' + element[0]['href']
element = element_for(url, 'span > span') 

print("\nCoordinates for", city + ":", element[0].text, element[1].text)
