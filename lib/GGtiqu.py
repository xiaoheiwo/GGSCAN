import os
import json
dict={}
result=[]
def tiqu(conf_info):

    filename = conf_info
    f1 = open(filename, "r")
    for i in f1.readlines():
        if i.split()[0] == "open":
            port = i.split()[2]
            ip = i.split()[3]
            # 将提取的内容放在字典dict{}中方便程序调用
            dict.setdefault(str(ip), set()).add(port)
        else:
            pass
    f1.close()
    for key in dict:
        if len(dict[key]) < 50:
            for i in dict[key]:
                a=[key,i]
                result.append([key,i])

        else:
            print ("IP:"+key+"存在防火墙，跳过扫描")
    return result





