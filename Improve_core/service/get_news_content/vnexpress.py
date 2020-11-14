import bs4
import requests

def get_page_content(url):
    headers = {'Accept-Language': 'vi-VN'}
    page = requests.get(url, headers = headers)
    soup=  bs4.BeautifulSoup(page.text,"html.parser")
    #remove figcaption
    while soup.find('figcaption') is not None:
        soup.find('figcaption').decompose()

    raw = soup.find_all('p', {"class":"Normal"})
    lst = []
    for x in raw:
        if len(x.getText()) >= 15:
            lst.append(x.getText())

    lst = " ".join(map(str, lst))

    return lst