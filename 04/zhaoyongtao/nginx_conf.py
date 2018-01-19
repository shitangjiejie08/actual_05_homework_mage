#encoding:utf-8

# nginx配置信息
user='nginx'
worker_processes = 4
error_log='/var/log/nginx/error_log'
access_log='/var/log/nginx/access.log'
pid='/var/run/nginx.pid'
worker_connections=1024
listen=80
server_name='localhost'
proxy_pass='127.0.0.1'

# 读取模板文件
nginx_tpl='./nginx.conf.tpl'
f=open(nginx_tpl,'rt')
text=f.read()
f.close()

# 根据模板信息生成配置文件
nginx_conf=open('./nginx.conf','wt')
nginx_conf.write(text.format(user=user,
				worker_processes=worker_processes,
				error_log=error_log,
				pid=pid,
				worker_connections=worker_connections,
				access_log=access_log,
				listen=listen,
				server_name=server_name,
				proxy_pass=proxy_pass
				))
