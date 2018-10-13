#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import urllib.request

import sys
url = sys.argv[1]

def get_url_soup(url):

    text = urllib.request.urlopen(url).read()
    soup = bs(text,'html.parser') 
    return soup

def get_super_content(soup):
    children = soup.body.div.children
    children = list(children)
    contents = children[9].find_all('a')
    contents = list(map(lambda x:x.get('href').strip('11_11606/'),contents))

    return contents

def get_sub_content(url):

    soup = get_url_soup(url)
    children = soup.contents
    title = children[2].h1.string
    contents = children[2].find_all(id='content')[0].text
    
    contents = '\n'+title+'\n' + contents
    return contents

if __name__ == "__main__":

    soup = get_url_soup(url)

    contents = get_super_content(soup)

    file = open('fiction.txt','w')

    for content in contents:
        sub_url = url+content
        sub_content = get_sub_content(sub_url)
        file.write(sub_content)
    file.close()
        
        
    


