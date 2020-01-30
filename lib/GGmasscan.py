import os
#调用masscan扫描全端口
def mscan(file,conf_info):
    m_file=conf_info["ip_file"]
    mscan=os.system('masscan -p 1-65535 -iL '+str(file) +'  --rate 2000 -oL '+m_file)


