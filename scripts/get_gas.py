from bs4 import BeautifulSoup
from csv import DictWriter

fname_base = 'mydata/crime-alert'
fname_end = '.shtml'
DATES = [1516, 1415, 1314, 1213, 1112, 1011]
events_list = []

for date in DATES:
    fname = fname_base + str(date) + fname_end
    txt = open(fname).read()
    soup = BeautifulSoup(txt, 'lxml')

    for hedtag in soup.find_all('h3'):
        titletxt = hedtag.text
        if 'gas' in titletxt.lower():
            mydict = {}
            mydict['title'] = titletxt
            mydict['body'] = ""

            for ptag in hedtag.find_next_siblings('p'):
                pd = ptag.attrs.get('id')
                if pd == 'post-date':
                    mydict['post-date'] = ptag.text
                    break
                else:
                    mydict['body'] += ptag.text + "\n"

            events_list.append(mydict)

# write CSV 
wf = open("test.csv", "w")
FIELDNAMES = ['title', 'body', 'post-date']

cfile = DictWriter(wf, fieldnames=FIELDNAMES)
cfile.writeheader()
cfile.writerows(events_list)
wf.close()
