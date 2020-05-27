# -*- coding: utf-8 -*-
#识别title
import requests
import re
import chardet
requests.packages.urllib3.disable_warnings()
from lib.GGlog import LogInfo


def Title(result):
    logger = LogInfo('log/process.log')
    logger.infostring('start Title recognition ...')
    #清理扫描结果
    f1=open("out/http_result.txt","w")
    f1.close()
    final_domains=[]
    urls=[]
    #这里偷懒了 为了更准确的识别所有端口上的web服务，就没有判断端口服务
    for i in result:
        scan_url=i[0]
        scan_port=i[1]

        if "443" in scan_port:
            url="https://"+scan_url+":"+scan_port
            urls.append(url)
        else:
            url="http://"+scan_url+":"+scan_port
            urls.append(url)
    for i in urls:
        try:
            # print(i)
            r = requests.get(i,timeout=3,verify=False)
            #获取网站的页面编码
            r_detectencode = chardet.detect(r.content)
            actual_encode = r_detectencode['encoding']
            response = re.findall(u'<title>(.*?)</title>',r.content.decode('utf-8'),re.S)
            if response == []:
                final_domains.append(i + "\n" )
                final_domains.append(i)
            else:
                #将页面解码为utf-8，获取中文标题
                res = response[0]
                banner = r.headers['server']
                final_domains.append(i + '\t ' + banner + ' \t' + res+"\n")
                print (i + '\t ' + banner + ' \t' + res )
        except Exception as e:
            # print(e)
            pass
    f1=open("out/http_result.txt","a+",encoding="utf8")
    for i in final_domains:
        f1.write(i)
    f1.close()
    logger.infostring('finsh Title recognition ...')
