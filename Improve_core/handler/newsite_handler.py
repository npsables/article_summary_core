from service import enrichment, get_content, google_search_service
from util import check_url
def handle(args, code):
    site = input("Enter ur domain: ")
    enriched_keys = enrichment.enrichment(args, code)
    print("ennnnn: ", enriched_keys)

    # Call Google api search
    res = google_search_service.search(enriched_keys, 1, str(site))
    lst_summary = []
    count = 0
    for item in res:
        url = check_url.check_url(item.get("link"))
        if url is not None:
            print(url)
            content = get_content.get_content(url)
            contents = get_content.render_content(content)
            summary = enrichment.knn_model(contents)
            lst_summary.append((url, summary))
            count = count +1
    return lst_summary
