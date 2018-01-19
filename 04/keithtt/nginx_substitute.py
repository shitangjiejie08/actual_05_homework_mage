'''
根据模版文件生成信息数据文件
'''

#encoding: utf-8

user='nginx'
worker_processes='1'
error_log='logs/error.log'
access_log='logs/access.log'
pid='logs/pid'
worker_connections=1024
listen=80
server_name='localhost'
proxy_pass='http://localhost:9001'

fhandler=open('nginx.conf.tpl','r')
cxt=fhandler.read()
fhandler.close()

fhandler=open('nginx.conf','w')
fhandler.write(cxt.format(user=user,
                          worker_processes=worker_processes,
                          error_log=error_log,
                          pid=pid,
                          worker_connections=worker_connections,
                          access_log=access_log,
                          listen=listen,
                          server_name=server_name,
                          proxy_pass=proxy_pass))
fhandler.close()