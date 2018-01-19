#enconding:utf-8
fhandler = open('nginx.conf.tpl','r')
tpl = fhandler.read()
fhandler.close()
fhandler = open('nginx.conf','w')
fhandler.write(tpl.format(
                          user = 'nobody',
                          worker_processes = 1,
                          error_log = 'logs/error_log',
                          access_log = 'logs/access_log',
                          pid = 'logs/pid',
                          worker_connections = 1024,
                          listen = 80,
                          server_name = 'localhost',
                          proxy_pass = 'http://locahost:9001'))
fhandler.close()
