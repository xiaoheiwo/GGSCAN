import os
import subprocess
import re
def weak(host,port,server):
    f2 = open("out/weakpass.txt", "a+")
    user_file = "conf/user.txt"
    pass_file = "conf/pass.txt"
    supported = ['asterisk', 'cisco', 'cisco-enable', 'ftp', 'ftps', 'http-proxy', 'imap', 'imaps', 'mssql',
                 'mysql', 'pcanywhere', 'vnc', 'pop3', 'pop3s', 'postgres', 'rdp', 'redis', 'rexec', 'rlogin',
                 'rsh', 'smb', 'smtp', 'smtps', 'smtp-enum', 'snmp', 'socks5', 'ssh', 'svn', 'teamspeak', 'telnet',
                 'telnets', 'vmauthd', 'vnc', 'xmpp']
    server_only_pass = ['cisco', 'cisco-enable', 'redis']
    if server not in supported:
        return
    # arg="hydra -L user.txt -P pass.txt -s 21 -f 223.68.3.44 ftp"
    if server not in server_only_pass:
        # arg = "hydra -L " + user_file + " -P " + pass_file + " -s 21 -f 223.68.3.44 ftp"
        arg = "hydra -L " + user_file + " -P " + pass_file + " -s " + port + " -f " + host + " " + server
    else:
        arg = "hydra -P " + pass_file + " -s " + port + " -f " + host + " " + server
    print (arg)
    p = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    # print (p.communicate())

    for line in iter(p.stdout.readline, b''):
        if "[ftp]" in line:
            print (line)
            f2.write(line+"\n")
            return
        elif "finished" in line:
            print ("No weakpass")
            return
    f2.close()
def weakpass(file):
    print ("\033[1;33mFinsh Weak scan\033[0m")
    f2=open("out/weakpass.txt","w")
    t_file=file
    f1=open(t_file,'r')
    for i in f1.readlines():
        value = re.split(':', i.strip())
        weak(value[0],value[1],value[2])

