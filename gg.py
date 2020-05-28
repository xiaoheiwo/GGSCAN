# -*- coding: utf-8 -*-
import configparser
import os
import sys
import datetime
from lib.GGscan import main
from lib.GGtitle import Title
from lib.GGweakpass import Weakpass_Scan
from lib.GGmasscan import mscan
from lib.GGmasscan import mscan2
from lib.GGlog import LogInfo
if __name__ == '__main__':
    print ('----------------------------GGSCAN V1.2')
    print ('----------------------------BY:MELONER')
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

    # conf_info['email_user'] = conf.get("Email", "user").strip()
    # conf_info['email_pass'] = conf.get("Email", "pass").strip()
    # conf_info['target_email'] = conf.get("Email", "target_email").strip()
    # conf_info['smtp_server'] = conf.get("Email", "smtp_server").strip()

    #调用GGscan里面的main函数启动程序，并传递配置
    if str(sys.argv[1]) == "-i" :
        ip=sys.argv[2]
        mscan2(ip,conf_info)
    else:
        mfile=sys.argv[1]
        mscan(mfile,conf_info)
    result=main(conf_info)
    Title(result)
    Weakpass_Scan().run()
    spend_time = (datetime.datetime.now() - start_time).seconds
    print ('程序共运行了： ' + str(spend_time) + '秒')