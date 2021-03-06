#encoding:utf-8

#生成nginx配置文件

user = 'nginx2'
worker_processes = 1
error_log = '/var/log/nginx/error.log'
pid = '/var/run/nginx/pid'
worker_connections = 1024
access_log = '/var/log/nginx/access.log'
listen = 80
server_name = 'localhost'
proxy_pass = 'http://localhost:9001'

fhandler = open('nginx.conf.tpl', 'r')
tpl = fhandler.read()
fhandler.close()

fhandler = open('nginx.conf', 'w')
fhandler.write(tpl.format(user = user,
                          worker_processes = worker_processes,
                          error_log = error_log,
                          pid = pid,
                          worker_connections = worker_connections,
                          access_log = access_log,
                          listen = listen,
                          server_name = server_name,
                          proxy_pass = proxy_pass))
fhandler.close()