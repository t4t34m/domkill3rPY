#!/usr/bin/python3
import re
import requests
import optparse
from random import choice
import configparser
from multiprocessing import Process,Manager
import sys, os
def clz():
    zl="clear"
    os.system(zl)
def headerx():
    clz()
    print(("""
_____   _____  ____    __  __  __  ____  ____    ____    ______  _____   
|     \ /     \|    \  /  ||  |/ / |    ||    |  |    |  |___   ||     |  
|      \|     ||     \/   ||     \ |    ||    |_ |    |_ |___   ||     \  
|______/\_____/|__/\__/|__||__|\__\|____||______||______||______||__|\__\ 
          
    """))

def doScan(url,dex,resx):
    i=0
    while True:
        uri=dex.get()
        if uri=='bye':
            break
        headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "http://127.0.0.1/",
    "Cookie": "xsrf_token=a-mMpF6dwym43afgEibJew;",
    "Connection": "close",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
        try:
            i+=1
            rep=requests.get(url=url+'/'+uri,headers=headers,timeout=1)
            if rep.status_code == 200:
                
                print(f"{i} : \x1b[1;38;5;120mFound\x1b[0m: \x1b[1;38;5;252m{url}\x1b[1;38;5;120m{uri}\x1b[0m")
                file = open("found.txt", "a+")
                file.write(f"{url}{uri}\n")
                file.close()
            else:
                print(f"{i} : \x1b[1;38;5;197mNot found\x1b[0m: {rep.status_code} - {uri}")
                continue
        except:
            pass
def main(url,thradx,dict):
    dex=Manager().Queue()
    resx=Manager().Queue()
    ProcessList=[]
    for i in range(0,int(thradx)):
        p=Process(target=doScan,args=(url,dex,resx))
        ProcessList.append(p)
        p.start()
    with open(dict,encoding='gbk') as f:
        while True:
            uri=f.readline().strip()
            if uri!='':
                dex.put(uri)
            else:
                break
    for p in ProcessList:
        dex.put('bye')
    while True:
        if len(ProcessList)==0:
            break
        for p in ProcessList:
            if not p.is_alive():
                ProcessList.remove(p)
if __name__=="__main__":
    parse=optparse.OptionParser()
    parse.add_option("-u",'--url',dest='url',help='url')
    parse.add_option("-p",'--process',default=2,dest='thradx',help='2')
    parse.add_option("-d",'--dictory',dest='dict',help='dict')
    (opt, argv) = parse.parse_args()
    if opt.url==None  or opt.dict==None:
        headerx()
        print("\x1b[1;38;5;120mUsage:\x1b[0m python3 domkill3rPY.py -d dir.txt -p 1 -u http(s)://target.com/ \n\n\n")
        exit()
    main(opt.url,opt.thradx,opt.dict)
