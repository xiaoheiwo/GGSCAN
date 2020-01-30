# GGSCAN
此工具仅用于安全研究，企业自查，切勿使用本工具对互联网造成破坏，感谢。  
渗透前资产探测工具
目前版本v1.0
## 使用环境

ubuntu
python3
需要安装 nmap,masscan和hydra
例：apt install nmap
安装所需库
`pip3 install -r requirements.txt`

目前仅限linux使用 windows平台环境配置比较复杂

## 使用方法

`python3 gg.py 123.txt `

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
有问题可以提交issues。

微信：zanyryy
欢迎各位老板支持
![Image text](https://raw.githubusercontent.com/xiaoheiwo/GGSCAN/master/img/4.png)
