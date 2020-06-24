# coding=utf-8
import nmap
import threading
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
            aa = self._queue.get()
            ip=aa[0]
            port=aa[1]
            try:
                #加入线程锁，解决了程序运行完shell不能执行其他命令的bug
                threadLock.acquire()
                scan(ip,port)
                threadLock.release()
            except Exception as e:
                print (e)
                pass


#使用nmap扫描目标识别服务
def scan(scan_ip,port):
    # try:
        Ip=scan_ip
        Port=port
        nm = nmap.PortScanner()
        ret = nm.scan(str(Ip),str(Port),arguments='-Pn -T4 -sV')
        service_name = ret['scan'][str(Ip)]['tcp'][int(Port)]['name']
        version = ret['scan'][str(Ip)]['tcp'][int(Port)]['product'] + \
                  ret['scan'][str(Ip)]['tcp'][int(Port)]['version'] + \
                  ret['scan'][str(Ip)]['tcp'][int(Port)]['extrainfo']
        # print (ret)

        print ('\033[1;32m[*Nmap]\033[0m  主机 ' + str(Ip) + ' 的 ' + str(Port) + ' 端口服务为：' + service_name +' 版本：'+version)

        result.append([Ip,Port,service_name])
    #
    # except Exception as e:
    #    print( "nmap端口扫描失败")
    #    pass

def out():
    f2=open("out/result.txt","w+")
    f1=open("out/domin3.csv","a+")
    f2=open("out/result.txt","a+")
    for i in result:
        f1.write(i[0] + ',' + i[1] + ',' + i[2]+"\n")
        f2.write(i[0]+":"+i[1]+":"+i[2]+"\n")
    f2.close()
    f1.close()

def main(result,conf_info):
    #输出日志文件
    print ("\033[1;33m[*INFO]Start nmap scan service...\033[0m")
    #导入masscan的结果
    t=conf_info["t"]
    #调用函数提取masscan的内容
    queue = Queue()


    for i in result:
        queue.put(i)

    threads=[]
    thread_count=int(t)
    for i in range(thread_count):
        threads.append(Scan(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print ("\033[1;33m[*INFO]Finsh nmap scan ...\033[0m")
    print ("\033[1;33m[*INFO]Start save result ...\033[0m")
    out()
    print ("\033[1;33m[*INFO]Finsh save result ...\033[0m")
    # logger.infostring('finsh save result ...')
    #返回结果方便title识别调用
    return result
