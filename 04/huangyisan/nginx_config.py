#!/usr/bin/env python3
user='nginx'
worker_processes='auto'
error_log='/var/log/nginx.log'
pid='/var/log/nginx.pid'
worker_connections='102400'
access_log='/var/log/nginx_access.log'
listen='80'
server_name='www.baidu.com'
proxy_pass='http://127.0.0.1:8080'
nginx_cxt=open('nginx.conf','w')
nginx_tpl_cxt=open('nginx.conf.tpl','r')
for line in nginx_tpl_cxt:
    nginx_cxt.write(line.format(user=user,worker_processes=worker_processes,error_log=error_log,pid=pid,worker_connections=worker_connections,access_log=access_log,listen=listen,server_name=server_name,proxy_pass=proxy_pass))
nginx_cxt.close()
nginx_tpl_cxt.close()
