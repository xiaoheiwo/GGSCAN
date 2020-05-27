# coding=utf-8
import nmap
import threading
from lib.GGlog import LogInfo
from queue import Queue
from multiprocessing import Pool as ThreadPool

dict={}
result=[]
final_domains = []
threadLock = threading.Lock()
class Scan(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            scan_ip = self._queue.get()
            try:
                #加入线程锁，解决了程序运行完shell不能执行其他命令的bug
                threadLock.acquire()
                scan(scan_ip)
                threadLock.release()
            except Exception as e:
                print (e)
                pass

#提取目标文件内容，分解成nmap可以识别的参数
def tiqu(t_filename):
    f1=open(t_filename,"r")
    for i in f1.readlines():
        if i.split( )[0] =="open":
            port= i.split( )[2]
            ip= i.split( )[3]
            #将提取的内容放在字典dict{}中方便程序调用
            dict.setdefault(str(ip),set()).add(port)
        else:
            pass
    f1.close()

#使用nmap扫描目标识别服务
def scan(scan_ip):
    try:
        key = scan_ip
        if len(dict[key]) < 50:
            for Port in dict[key]:
                Ip=key
                nm = nmap.PortScanner()
                ret = nm.scan(str(Ip),str(Port),arguments='-Pn -T4 -sV')
                service_name = ret['scan'][str(Ip)]['tcp'][int(Port)]['name']
                version = ret['scan'][str(Ip)]['tcp'][int(Port)]['product'] + \
                          ret['scan'][str(Ip)]['tcp'][int(Port)]['version'] + \
                          ret['scan'][str(Ip)]['tcp'][int(Port)]['extrainfo']
                # print (ret)
                print ('[*]主机 ' + str(Ip) + ' 的 ' + str(Port) + ' 端口服务为：' + service_name +' 版本：'+version)
                result.append([Ip,Port,service_name])
        else:
            print ("IP:"+key+"存在防火墙，跳过扫描")
    except Exception as e:
       print( "nmap端口扫描失败")
       pass

def out():
    f2=open("out/result.txt","w+")
    f1=open("out/domin3.csv","a+")
    f2=open("out/result.txt","a+")
    for i in result:
        f1.write(i[0] + ',' + i[1] + ',' + i[2]+"\n")
        f2.write(i[0]+":"+i[1]+":"+i[2]+"\n")
    f2.close()
    f1.close()

def main(conf_info):
    #输出日志文件
    logger = LogInfo('log/process.log')
    logger.infostring('start nmap scan service...')
    #导入masscan的结果
    t_filename = conf_info["ip_file"]
    t=conf_info["t"]
    #调用函数提取masscan的内容
    tiqu(t_filename)
    queue = Queue()

    #遍历目标调用多线程开始进行nmap扫描
    for key in dict:
        queue.put(key)

    threads=[]
    thread_count=int(t)
    for i in range(thread_count):
        threads.append(Scan(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


    logger.infostring('finsh nmap scan ...')
    logger.infostring('start save result ...')
    #保存结果
    out()
    logger.infostring('finsh save result ...')
    #返回结果方便title识别调用
    return result
