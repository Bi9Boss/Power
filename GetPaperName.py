import requests
from bs4 import BeautifulSoup
urls = [
    # "https://dblp.uni-trier.de/db/journals/joc/joc33.html",
    # "https://dblp.uni-trier.de/db/journals/joc/joc32.html",
    # "https://dblp.uni-trier.de/db/journals/joc/joc31.html",
    "https://dblp.uni-trier.de/db/journals/tifs/tifs15.html",
    "https://dblp.uni-trier.de/db/journals/tifs/tifs14.html",
    "https://dblp.uni-trier.de/db/journals/tifs/tifs13.html",
    "https://dblp.uni-trier.de/db/journals/tdsc/tdsc17.html",
    "https://dblp.uni-trier.de/db/journals/tdsc/tdsc16.html",
    "https://dblp.uni-trier.de/db/journals/tdsc/tdsc15.html",
    "https://dblp.uni-trier.de/db/conf/ccs/ccs2020.html",  #CSS
    "https://dblp.uni-trier.de/db/conf/ccs/ccs2019.html",
    "https://dblp.uni-trier.de/db/conf/ccs/ccs2018.html",
    "https://dblp.uni-trier.de/db/conf/sp/sp2020.html", #S&P
    "https://dblp.uni-trier.de/db/conf/sp/sp2019.html",
    "https://dblp.uni-trier.de/db/conf/sp/sp2018.html",
    "https://dblp.uni-trier.de/db/conf/uss/uss2020.html", #uss
    "https://dblp.uni-trier.de/db/conf/uss/uss2019.html",
    "https://dblp.uni-trier.de/db/conf/uss/uss2018.html"
]
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError:
        print(r.status_code)
        exit(0)
    except:
        print("代理异常或者超时")
        exit(0)

def textWrite(string):
    with open("test.txt","a",encoding='utf-8') as f:
        f.write(string + "\t"+ years[i]+ "\n") 

def getTitles(soup):
    titles = soup.find_all('span', class_="title")
    for title in titles:
        print(title)
        strN = title.text
        textWrite(strN)

years = ["2020","2019","2018"]
i = 0
for url in urls:
    print("1")
    if i == 3:
        i = 0
    html = getHTMLText(url)
    print(url)
    soup  =  BeautifulSoup(html, "html.parser")
    getTitles(soup)
    i = i+1

print("asd")