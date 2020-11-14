from service import enrichment
from service import get_content
from handler import selected_site_handler, newsite_handler
import const

def query_handler(args):
    if args['querynew']:
        if args['chinhtri']:
            return newsite_handler.handle(args['querynew'], const.CHINH_TRI)
        elif args['thethao']:
            return newsite_handler.handle(args['querynew'], const.THE_THAO)
        elif args['giaoduc']:
            return newsite_handler.handle(args['querynew'], const.GIAO_DUC)
        elif args['giaitri']:
            return newsite_handler.handle(args['querynew'], const.GIAI_TRI)
        elif args['congnghe']:
            return newsite_handler.handle(args['querynew'], const.CONG_NGHE)
        elif args['kinhte']:
            return newsite_handler.handle(args['querynew'], const.KINH_TE)
        elif args['phapluat']:
            return newsite_handler.handle(args['querynew'], const.PHAP_LUAT)
        elif args['dienanh']:
            return newsite_handler.handle(args['querynew'], const.DIEN_ANH)
        elif args['covid19']:
            return newsite_handler.handle(args['querynew'], const.COVID_19)
    else:
        if args['chinhtri']:
            return selected_site_handler.handle(args['query'], const.CHINH_TRI)
        elif args['thethao']:
            return selected_site_handler.handle(args['query'], const.THE_THAO)
        elif args['giaoduc']:
            return selected_site_handler.handle(args['query'], const.GIAO_DUC)
        elif args['giaitri']:
            return selected_site_handler.handle(args['query'], const.GIAI_TRI)
        elif args['congnghe']:
            return selected_site_handler.handle(args['query'], const.CONG_NGHE)
        elif args['kinhte']:
            return selected_site_handler.handle(args['query'], const.KINH_TE)
        elif args['phapluat']:
            return selected_site_handler.handle(args['query'], const.PHAP_LUAT)
        elif args['dienanh']:
            return selected_site_handler.handle(args['query'], const.DIEN_ANH)
        elif args['covid19']:
            return selected_site_handler.handle(args['query'], const.COVID_19)
        else:
            return lmpify_handler(args['query'])
    print("Some thing wrong! (query_handler)")
    return None

def lmpify_handler(args):
    enriched_keys = enrichment.old_enrichment(args)
    print(enriched_keys)
    # currrently support only baomoi.com
    search_url = "https://baomoi.com/tim-kiem/" + "-".join(enriched_keys) + ".epi"
    
    url = get_content.get_latest_article(search_url)
    
    content = get_content.get_content(url)
    contents = get_content.render_content(content)
    # print("content here :", contents)
    # print("content type: ", type(contents))
    summary = enrichment.knn_model(contents)
    return summary