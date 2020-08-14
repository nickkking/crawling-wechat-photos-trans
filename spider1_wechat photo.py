import requests
from bs4 import BeautifulSoup
import re
import os


# 获取网页信息
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 解析网页，获取所有图片url
def getimgURL(html):
    soup = BeautifulSoup(html, "html.parser")
    adlist = []
    for i in soup.find_all("img"):
        try:
            ad = re.findall(r'.*src="(.*?)?" .*', str(i))
            if ad:
                adlist.append(ad)
        except:
            continue
    return adlist


# 新建文件夹pic，下载并保存爬取的图片信息
def download(adlist):
    # 注意更改文件目录
    root = "E:\\spider\photo\\"
    for i in range(len(adlist)):
        path = root + str(i) + "." + 'gif'
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(adlist[i][0])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()


def main():
    url = 'https://mp.weixin.qq.com/s?__biz=MzUzOTUxNDY0OA==&mid=2247484173&idx=3&sn=63bf79a0f3372bb0d132d1a00e1ff2ea&chksm=fac6017acdb1886ce1cc54217d76f02eb42c8a736f59ab01a802ce32ce03d944fa36ca987430&mpshare=1&scene=1&srcid=&sharer_sharetime=1590364233623&sharer_shareid=da8a96ee65e3362c69ab67c563c91679#rd'
    html = getHTMLText(url)
    list = getimgURL(html)
    download(list)


main()
