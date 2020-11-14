import bs4
import requests
import re
def get_page_content(url):
    headers = {'Accept-Language': 'vi-VN'}
    page = requests.get(url, headers = headers)
    soup=  bs4.BeautifulSoup(page.text,"html.parser")
    #remove figcaption
    while soup.find('figcaption') is not None:
        soup.find('figcaption').decompose()
    raw = soup.find(id = "abody").getText()

    string  = " ".join(raw.split())
    return string