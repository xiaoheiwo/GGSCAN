# -*- coding: utf-8 -*-
import configparser
import os
import sys
import datetime
from lib.GGscan import main
from lib.GGtitle import Title
from lib.GGweakpass import weakpass
from lib.GGmasscan import mscan
from lib.GGmasscan import mscan2
from lib.GGlog import LogInfo
from lib.GGtiqu import tiqu
if __name__ == '__main__':
    print ('\033[1;32m----------------------------GGSCAN V1.4\033[0m')
    print ('\033[1;32m----------------------------BY:MELONER\033[0m')
    result=[]
    #获取运行时间
    start_time = datetime.datetime.now()

    #生成各种输出文件夹
    if not os.path.exists('out'):
        os.mkdir('out')
    if not os.path.exists('log'):
        os.mkdir('log')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    conf_info = {}
    conf = configparser.ConfigParser()
    conf.read("conf/info.conf")
    # 从配置文件读取各种配置并加在进列表中
    conf_info['ip_file'] = conf.get("OPTIONS", "ip_file").strip()
    conf_info['db_user'] = conf.get("OPTIONS", "db_user").strip()
    conf_info['db_pass'] = conf.get("OPTIONS", "db_pass").strip()
    conf_info['t'] = conf.get("OPTIONS","t").strip()
    conf_info['type'] = conf.get("OPTIONS", "type").strip()
    conf_info['rate'] = conf.get("Masscan", "rate").strip()


    #调用GGscan里面的main函数启动程序，并传递配置
    if str(sys.argv[1]) == "-i" :
        ip=sys.argv[2]
        mscan2(ip,conf_info)
    else:
        mfile=sys.argv[1]
        mscan(mfile,conf_info)
    result=tiqu(conf_info["ip_file"])
    Title(result)
    nmap=main(result,conf_info)
    # weakpass("out/result.txt")
    spend_time = (datetime.datetime.now() - start_time).seconds
    print ('程序共运行了： ' + str(spend_time) + '秒')