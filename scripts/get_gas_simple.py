from bs4 import BeautifulSoup
fname = 'mydata/crime-alert1415.shtml'


txt = open(fname).read()
soup = BeautifulSoup(txt, 'lxml')

events_list = []
for hedtag in soup.find_all('h3'):
    title = hedtag.text
    if 'gas' in title.lower():
        eventtxt = title + "\n"
        for ptag in hedtag.find_next_siblings('p'):
            eventtxt += ptag.text
            eventtxt += "\n"
            pid = ptag.attrs.get('id')
            if pid == 'post-date':
                break

        events_list.append(eventtxt)


for e in events_list:
    print(e)
