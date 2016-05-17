# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:21:24 2016

@author: Administrator
"""
import urllib
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    
    print "Downloaded  %.2f%%\r" %per,
dist={"在下坂本有何贵干":"4635354"}
aid=raw_input("请输入番剧名\n")
browser = webdriver.PhantomJS()
browser.get('http://www.bilibili.com/video/av%s/'%dist[aid])
html=browser.page_source
soup = BeautifulSoup(html)
result=soup.find_all(id="v_bgm_list_data")
List=re.findall(r'av(\d+)',str(result[0]))  
for i in xrange(len(List)):
    html=requests.get("http://www.bilibili.com/m/html5?aid=%s&page=1"%List[i])
    s=json.loads(html.content)
    url=s['src']
    print "%s_%d"%(aid,i)
    urllib.urlretrieve(url,'%s.flv'%List[i],Schedule)
browser.close()
