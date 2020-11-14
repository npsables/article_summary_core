import requests
import const

def search(args, flag, site):
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = const.API_KEY
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = const.SEARCH_ENGINE_ID_SELECTED
    sites = site
    query = args
    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1


    # Tăng start lên trên 10 nếu muốn chuyển trang (tối đa 100)
    if flag == 0:
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date"
    if flag == 1:
        SEARCH_ENGINE_ID = const.SEARCH_ENGINE_ID_INPUT
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&siteSearch={sites}&sort=date"

    print(url)
    data = requests.get(url).json()
    search_items = data.get("items")
    
    # iterate over 10 results found
    for i, search_item in enumerate(search_items, start=1):
        # get the page title
        title = search_item.get("title")
        # page snippet
        snippet = search_item.get("snippet")
        # alternatively, you can get the HTML snippet (bolded keywords)
        html_snippet = search_item.get("htmlSnippet")
        # extract the page url
        link = search_item.get("link")
        # print the results
        print("="*10, f"Result #{i+start-1}", "="*10)
        print("Title:", title)
        print("Description:", snippet)
        print("URL:", link, "\n")
    
    
    return data.get("items")