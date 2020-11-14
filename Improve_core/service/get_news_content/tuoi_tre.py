import bs4
import requests

def get_page_content(url):
    headers = {'Accept-Language': 'vi-VN'}
    page = requests.get(url, headers = headers)
    soup=  bs4.BeautifulSoup(page.text,"html.parser")
    #remove figcaption
    while soup.find('figcaption') is not None:
        soup.find('figcaption').decompose()
    soup.find('div', {"class":"VCSortableInPreviewMode active"}).decompose() if soup.find('div', {"class":"VCSortableInPreviewMode active"}) is not None else soup.find('div', {"class":"VCSortableInPreviewMode"}).decompose()
    raw = soup.find('div', {"id":"main-detail-body"}).findAll('p')
    lst = []
    for x in raw:
        lst.append(x.getText())

    lst = " ".join(map(str, lst))
    return lst