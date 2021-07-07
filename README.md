*免责声明：本工具仅用于安全研究，企业自查，严禁使用本工具对互联网造成破坏，感谢。 
# 更新日志

有个运行完程序之后 再去输入其他命令 就不显示了的bug  一直没解决  所以加了线程锁，但是加了线程锁 速度就很慢，希望有知道怎么解决的老哥给提个issues

扫大量资产的时候建议把线程锁去掉
2020.6.26  
1. 修复title识别输出问题
2. 正式增加弱口令扫描功能（速度较慢，默认关闭，gg.py中消除weakpass注释打开此功能,并且还有一些bug，不建议使用）
3. 优化代码流程
4. 更新高亮  

2020.5.28
1. 修复nmap多线程扫描还是慢的问题
2. 修改默认nmap线程为10，请根据机器内存大小修改线程


2020.5.27  
1. nmap扫描增加参数，更准确的识别服务版本  
2. 增加跳过开放大量端口ip问题 
3. 支持单ip扫描   gg.py -i 127.0.0.1
# GGSCAN
渗透前资产探测工具  
目前版本v1.3

修改masscan扫描线程，在conf/目录下 info.conf 文件中

不需要的模块 如title 和端口爆破模块 可以在gg.py 中注释掉最后的调用即可
## 使用环境

ubuntu
python3
需要安装 nmap,masscan和hydra
例：apt install nmap
安装所需库
`pip3 install -r requirements.txt`

目前仅限linux使用 windows平台环境配置比较复杂

## 使用方法
批量扫描  
`python3 gg.py 123.txt `  
`python3 gg.py -i 127.0.0.1-24 `  
单ip扫描  
`python3 gg.py -i 127.0.0.1`

123.txt 中放ip列表 一个ip一行目前只支持ip

## 原理
调用本地masscan全端口扫描——解析结果发送给nmap识别服务——根据结果进行title识别——根据结果进行调用本地hydra进行简单的服务爆破

## 展示
运行截图
![Image text](https://raw.githubusercontent.com/xiaoheiwo/GGSCAN/master/img/1.jpg)
标题识别结果
![Image text](https://raw.githubusercontent.com/xiaoheiwo/GGSCAN/master/img/2.jpg)
服务识别结果
![Image text](https://raw.githubusercontent.com/xiaoheiwo/GGSCAN/master/img/3.jpg)


## 联系方式
欢迎大家提意见改进

qq群 608852927 麻烦备注一下github 不备注的不加
