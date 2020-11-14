import re
import requests
import const
import newspaper
import html2text
from service.get_news_content import dan_tri, lao_dong, nhan_dan, thanh_nien, tuoi_tre, vnexpress
def get_content(url):
    redirect_page = requests.get(url)
    for resp in redirect_page.history:
        print(resp.status_code, resp.url)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, redirect_page.text)[-1][0]
    article = newspaper.Article(url,language='vi')
    article.download()
    article.parse()
    # print(article.text)
    return re.sub('\\n+', '</p><p>', '<p>' + article.text + '</p>')

def get_latest_article(url):
    search_page = requests.get(url)
    cleaned_text = html2text.html2text(search_page.text)
    regex = r"\((/([^ ])+)+\)"
    urls = re.findall(regex, cleaned_text)
    
    for uri in urls:
        if "/r/" not in uri[0]:
            continue
        return "https://baomoi.com" + uri[0]

def render_content(content):
    return html2text.html2text(content)


def get_selected_content(url):
    if "dantri.com.vn" in url:
        return dan_tri.get_page_content(url)
    if "tuoitre.vn" in url:
        return tuoi_tre.get_page_content(url)
    if "thanhnien.vn" in url:
        return thanh_nien.get_page_content(url)
    if "laodong.com.vn" in url:
        return lao_dong.get_page_content(url)
    if "nhandan.com.vn" in url:
        return nhan_dan.get_page_content(url)
    if "vnexpress.net" in url:
        return vnexpress.get_page_content(url)
    print("Something wrong")
    return ""