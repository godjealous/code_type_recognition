import urllib.request
from bs4 import BeautifulSoup
import os
#languages=['python','java','c','go','php','r','perl','javascript','cpp']
languages=['java','cpp']
for language in languages:
    response = urllib.request.urlopen('https://github.com/topics/'+language)
    page=response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    website="https://github.com"
    clonewebsite=""
    for article in soup("article"):
        #print(website+article.a['href']+".git")
        clonewebsite="git clone "+website+article.a['href']+".git"
        os.system(clonewebsite)


