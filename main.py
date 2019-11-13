import argparse
from ccommon import config
import logging
logging.basicConfig(level=logging.INFO)
def _news_scraper(news_site):
    host=config()['news_sites'][news_site]['url']
    logging.info('Beginning scraper for {}'.format(host))
    pass
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    news_site_choices=list(config()['news_sites'].keys())
    parser.add_argument('news_site',help='the news site that you want to scrape', type=str, choices=news_site_choices)
    print(news_site_choices)
    input('hola')
    args=parser.parse_args()
    print(type(args))
    _news_scraper(args.news_site) 