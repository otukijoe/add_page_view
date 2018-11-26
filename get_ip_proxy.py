# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     get_ip_proxy
   Author:        JOE
   date:          2018/10/25
-------------------------------------------------
"""

from bs4 import BeautifulSoup
import requests
import random
from time import sleep
import get_useragent

useragent = get_useragent.get_user_agent()
header = {'User-Agent': useragent}

def dict2proxy(dic):
    s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {dic['type']: s}

def parse_items(items):
    # 存放ip信息字典的列表
    ips = []
    for item in items:
        tds = item.find_all('td')
        # 从对应位置获取ip，端口，类型
        ip, port, type = tds[1].text, int(tds[2].text), tds[5].text
        ips.append({'ip': ip, 'port': port, 'type': type})
    return ips

def check_ip(ip):
    try:
        proxy = dict2proxy(ip)
        url = 'http://www.ip138.com/'
        r = requests.get(url, headers=header, proxies=proxy, timeout=5)
        r.raise_for_status()
    except:
        return False
    else:
        return True

def get_proxies():
    url = 'http://www.xicidaili.com/nn/'
    r = requests.get(url, headers=header)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    # print r.content
    soup = BeautifulSoup(r.text, 'lxml')
    # 第一个是显示最上方的信息的，需要丢掉
    items = soup.find_all('tr')[1:]
    # print items
    print 'Generating proxy IP pool...'
    sleep(3)
    ips = parse_items(items)
    # print ips
    good_proxies = []
    for ip in ips:
        if check_ip(ip):
            good_proxies.append(dict2proxy(ip))
            print dict2proxy(ip)
    print 'The proxy IP pool has been generated!'
    sleep(3)
    return good_proxies

def get_random_ip(good_proxies):
    return random.choice(good_proxies)

if __name__ == '__main__':
    good_proxies = get_proxies()
    ip = get_random_ip(good_proxies)
    print ip
