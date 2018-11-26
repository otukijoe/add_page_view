# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     add_page_view
   Author:        JOE
   date:          2018/10/24
-------------------------------------------------
"""

import requests
import config
import get_useragent
import get_ip_proxy
from time import sleep
count = 0

def get_html(good_proxies, rate):
    global count
    useragent = get_useragent.get_user_agent()
    header = {
        'User-Agent': useragent,
        'Host': config.host,
        'Referer': config.referer,
        'Cookie': config.cookie,
    }
    print 'The current user-agent is: ', useragent
    proxies = get_ip_proxy.get_random_ip(good_proxies)
    print 'The current proxy IP is: ', proxies
    res = requests.get(config.url, headers=header, proxies=proxies)
    # res = requests.get(config.url, headers=header)
    if res is not None and res.status_code == 200:
        # print res.content
        count = count + 1
        print 'visit successful {c} times!'.format(c=count)
        print '\n'
        sleep(rate)

if __name__ == '__main__':
   #访问频率：秒
    rate = input('please input the rate of visit(unit:second):')
    print 'start:'
    sleep(1)
    for i in range(3, 0, -1):
        print i
        sleep(1)
    good_proxies = get_ip_proxy.get_proxies()
    while True:
        try:
            get_html(good_proxies, rate)
        except Exception as e:
            print e
