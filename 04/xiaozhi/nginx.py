with open("nginx.conf.tpl") as f:
    tpl = f.read()
    with open("nginx.conf", 'w') as fhandler:
        fhandler.write(tpl.format(user="root",
                                        worker_processes=8,
                                        error_log = "/data/log/error_log",
                                        access_log="/data/log//access_log",
                                        pid=102456,
                                        worker_connections=1024,
                                        listen=80,
                                        server_name="www.test.com",
                                        proxy_pass="127.0.0.1"))