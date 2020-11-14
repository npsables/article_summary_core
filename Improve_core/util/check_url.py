def check_url(url):
    print(url)
    if len(url) > 80:
        if "tag" not in url:
            return url
    else: 
        return None