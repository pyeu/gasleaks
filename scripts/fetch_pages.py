from os.path import basename, join
from settings import DATA_DIR
from bs4 import BeautifulSoup
import requests
import re


HOME_PAGE_URL = 'http://web.stanford.edu/group/SUDPS/crime-alert.shtml'

resp = requests.get(HOME_PAGE_URL)
soup = BeautifulSoup(resp.text, 'lxml')

for atag in soup.select('#udm a'):
    href = atag['href']
    if re.search(r'crime-alert\d+\.shtml$', href):
        print(href)
        resp = requests.get(href)
        fname = join(DATA_DIR, basename(href))
        with open(fname, 'w') as wf:
            wf.write(resp.text)
