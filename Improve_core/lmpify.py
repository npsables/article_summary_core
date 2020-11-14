import argparse 
from handler import handler

def get_parser():
    parser = argparse.ArgumentParser(description="Process querys")
    parser.add_argument('-q', '--query', metavar='QUERY', type=str, nargs='*', help='the question to answer')
    parser.add_argument('-qn', '--querynew', metavar='QUERY NEW SITE', type=str, nargs='*', help='query on new site')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--chinhtri',  action='store_true', help = 'chinh tri')
    group.add_argument('--thethao',  action='store_true', help = 'the thao')
    group.add_argument('--giaoduc',  action='store_true', help = 'giao duc')
    group.add_argument('--giaitri',  action='store_true', help = 'giai tri')
    group.add_argument('--congnghe',  action='store_true', help = 'cong nghe')
    group.add_argument('--kinhte',  action='store_true', help = 'kinh te')
    group.add_argument('--phapluat',  action='store_true', help = 'phap luat')
    group.add_argument('--dienanh',  action='store_true', help = 'dien anh')
    group.add_argument('--covid19',  action='store_true', help = 'covid19')
    return parser   

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    print(args)
    output = handler.query_handler(args)
    count = 1
    if type(output) is not str:
        for i, x in enumerate(output, start=1):
            print("="*10, "Result ", count, ": ","="*10)
            print("URL:", x[0], "\n")
            print("SUMMARY: ", x[1], "\n")
            count = count + 1
        print("\n\nNOTE: <10 results because of some shit links")
    else:
        print(output)
if __name__ == "__main__":
    command_line_runner()