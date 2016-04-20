from bs4 import BeautifulSoup


fname = 'mydata/crime-alert1415.shtml'


txt = open(fname).read()
soup = BeautifulSoup(txt, 'lxml')

events_list = []


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


for e in events_list:
    print(e)
