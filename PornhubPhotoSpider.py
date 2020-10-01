import requests
from bs4 import BeautifulSoup
import bs4
import os
import re

proxies = {
  "http": "http://127.0.0.1:10809",
  "https": "http://127.0.0.1:10809",
}

host = "https://www.pornhub.com"

def getHTMLText(url):
    try:
        r = requests.get(url, timeout =30, proxies = proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError:
        print(r.status_code)
        exit(0)
    except:
        print("代理异常或者超时")
        exit(0)

def GetUsername(soup):
    div = soup.find(name='div', attrs={"class":"float-left subHeaderOverrite"})
    name = div.a.string
    username = name.strip()
    username =  "./"+username
    return username

def GetPageAlbums(ainfo, soup): #获得当前分页上的所有album
    ul = soup.find(name='ul', attrs={"class":"photosAlbumsListing"})
    for li in ul.children:
        if isinstance(li, bs4.element.Tag):
            if li.a !=  None and li.a.div.div != None:
                url = li.a.attrs['href']        #判断是不是vip
                name = li.a.div.div.div.string
                ainfo.append([name,host+url])

def GetAlbumsAndUrls(ainfo, soup):
    AlbumUrls = []
    for Album in soup.find_all(name='a', attrs={"class":"seeAllButton greyButton float-right"}):  #所有列表中的See all
        AlbumUrls.append(host+Album.attrs['href'])
    for AlbumUrl in AlbumUrls:
        i = 0
        while True:                             #用与取所有分页
            i = i+1
            u = AlbumUrl+ "?page=" +str(i)
            html = getHTMLText(u)
            soup  =  BeautifulSoup(html, "html.parser")
            GetPageAlbums(ainfo, soup)
            haveNext = soup.find(name='li', attrs={"class":"page_next"})
            if haveNext == None:
                break
            

def GetPhotoesNameAndUrl(pinfo, soup):
    ul = soup.find(name='ul', attrs={"class":"photosAlbumsListing albumViews preloadImage"})
    for li in ul.children:
        if isinstance(li, bs4.element.Tag):
            name = li.attrs['id']
            url = li.a.attrs['href']
            pinfo.append([name,host+url])

def DownloadPhoto(url, albumName):
    html = getHTMLText(url)
    soup  =  BeautifulSoup(html, "html.parser")
    x = soup.find(name='img', attrs={"alt":albumName})
    try:
        u = x.attrs['src']
    except:
        return None
    try:
        r = requests.get(u, timeout =30, proxies = proxies)
        r.raise_for_status()
        return r
    except:
        print(url+"失败")
        print(r.request.headers)
        print(r.status_code)
        return None

def SavePhoto(path, photo):
    if  not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(photo)
            f.close()
            print(path+"文件保存成功")
    else:
        print(path+"文件已经存在")

def DownloadAlbum(name, url, path):
    pinfo = []
    url = url + "?page="
    i = 0
    while True:                             #用与取所有分页
        i = i+1
        u = url+str(i)
        html = getHTMLText(u)
        soup  =  BeautifulSoup(html, "html.parser")
        GetPhotoesNameAndUrl(pinfo, soup)
        haveNext = soup.find(name='li', attrs={"class":"page_next"})
        if haveNext == None:
            break
    for photo in pinfo:
        photoPathName = path+'/'+photo[0]+".jpg"
        if  not os.path.exists(photoPathName):
            p = DownloadPhoto(photo[1], name)
            if p != None:
                SavePhoto(photoPathName, p.content)

def DownloadAlbums(ainfo,name):
    for album in ainfo:
        path = name+"/"+album[0].strip()
        if not os.path.exists(path):
            os.makedirs(path)
        DownloadAlbum(album[0],album[1], path)

def main():
    ainfo = []
    str1 = ""
    str1 = input("网址：")
    url = host + '/model/xiao-e/photos'
    if re.match(r'https?:\/\/www\.pornhub\.com',str1) != None:
        url = str1
    print("开始")
    html = getHTMLText(url)
    soup  =  BeautifulSoup(html, "html.parser")
    username = GetUsername(soup)
    GetAlbumsAndUrls(ainfo, soup) 
    DownloadAlbums(ainfo, username)

main()
