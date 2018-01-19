# encoding: utf-8


user="nginx"
worker_processes="1"
error_log="logs/error.log"
pid="run/nginx.pid"
worker_connections="1024"
access_log="logs/access.log"
listen="80"
server_name="localhost"
proxy_pass="http://localhost:9001"


template_file = open("nginx.conf.tpl","r")
content = template_file.read()
template_file.close()

nginx_conf_file = open("nginx.conf","x")
nginx_conf_file.write(content.format(user=user,
                                    worker_processes=worker_processes,
                                    error_log=error_log,
                                    pid=pid,
                                    worker_connections=worker_connections,
                                    access_log=access_log,
                                    listen=listen,
                                    server_name=server_name,
                                    proxy_pass=proxy_pass
    ))

nginx_conf_file.close()