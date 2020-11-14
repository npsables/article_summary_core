from service import enrichment, get_content, google_search_service

def handle(args, code):
    enriched_keys = enrichment.enrichment(args, code)
    print("ennnnn: ", enriched_keys)

    # currrently support only baomoi.com
    # search_url = "https://baomoi.com/tim-kiem/" + "-".join(enriched_keys) + ".epi"
    # urls = get_content.get_latest_article(search_url)
    # content = get_content.get_content(urls)
    # contents = get_content.render_content(content)

    # Call Google api search
    res = google_search_service.search(enriched_keys, 0, None)
    lst_summary = []
    count = 0
    for item in res:
        url = item.get("link")
        # TAKE LEN(URL) > 50 ORTHERWISE SHIT WEBSITE
        if len(url) > 50:
            print(len(url))
            content = get_content.get_selected_content(url)
            summary = enrichment.knn_model(content)
            lst_summary.append((url, summary))
        count = count +1
    return lst_summary
