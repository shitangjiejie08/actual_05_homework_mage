#/bin/env python
#encoding:utf-8

fhandler = open('nginx.conf.tpl','r')
tpl = fhandler.read()
fhandler.close()
fhandler = open('nginx.conf','w')

fhandler.write(tpl.format(
					user='daemon',
					worker_processes = 10,
					error_log = 'logs/error.log',
					access_log = 'logs/access.log',
					pid =  'logs/pid',
					worker_connections = 102400,
					listen = 80,
					server_name = 'www.koch.com',
					proxy_pass = 'http://127.0.0.1:8080'
					)
				)
fhandler.close()