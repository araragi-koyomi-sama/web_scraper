# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:08:41 2019

@author: MSI
"""
from ccommon import config
from main import _news_scraper
import requests
import bs4
class Scraper(object):
    def __init__(self,new_link_uid):
        self._config=config()['news_sites'][new_link_uid] #esto retorna la llave del periodico
        self.__url=config()['news_sites'][new_link_uid]['url']
        self.__queries=config()['news_sites'][new_link_uid]['queries']
        self.parser()
        pass
    def parser(self):
        response=requests.get(self.__url)
        print(self.__url)
        soup=bs4.BeautifulSoup(response.text,'html.parser')
        print(self.__queries['homepage_article_links'])
        list_link=soup.select(self.__queries['homepage_article_links'])
        self.__news_links=set(new_link['href'] for new_link in list_link)
        pass
    def show_scraped(self):
        return self.__news_links
    pass
colombiano=Scraper('elcolombiano')
for a in colombiano.show_scraped():
    print('*****************inicio noticia*******************')
    print(a)
    print('*****************fin noticia*******************')


