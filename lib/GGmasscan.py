import os
#调用masscan扫描全端口
def mscan(file,conf_info):
    rate=conf_info["rate"]
    m_file=conf_info["ip_file"]
    mscan=os.system('masscan -p 1-65535 -iL '+str(file) +'  --rate '+str(rate)+' -oL '+m_file)

def mscan2(ip,conf_info):
    rate = conf_info["rate"]
    m_file=conf_info["ip_file"]
    mscan=os.system('masscan -p 1-65535  '+str(ip) +'  --rate '+str(rate)+' -oL '+m_file)