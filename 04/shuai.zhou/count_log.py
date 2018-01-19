# encoding: utf-8


"""
读取访问日志解析出IP，url，状态码，并统计出现次数，将出现次数最多的TOP 10数据写入到文件中
每行读取一组数据，写入dict key:ip/url/status

61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"
"""

ip_dict = {}
url_dict = {}
code_dict = {}

log_file = open('test.log', 'tr')
while True:
    line = log_file.readline()
    if line == '':
        break
    # line = line.strip('{}')
    elements = line.split(' ')
    ip = elements[0]
    url = elements[6]
    code = elements[8]
    current_value = ip_dict.get(ip, 0)
    ip_dict[ip] = current_value + 1
    current_value = url_dict.get(url, 0)
    url_dict[url] = current_value + 1
    current_value = code_dict.get(code, 0)
    code_dict[code] = current_value + 1

top_file = open('top_10_file.txt', 'w')
total = 0
for i in range(len(ip_dict)):
    max_count = 0
    max_ip = None
    for ip in ip_dict:
        ip_count = ip_dict[ip]
        if ip_count > max_count:
            max_count = ip_count
            max_ip = ip
    ip_dict.pop(max_ip)
    top_file.write(str(max_count) + '\t' + max_ip + '\n')
    total = total + 1
    if total >= 10:
        break

top_file.write('\n\n')

total = 0
for j in range(len(url_dict)):
    max_count = 0
    max_url = None
    for url in url_dict:
        url_count = url_dict[url]
        if url_count > max_count:
            max_count = url_count
            max_url = url
    url_dict.pop(max_url)
    top_file.write(str(max_count) + '\t' + max_url + '\n')
    total = total + 1
    if total >= 10:
        break

top_file.write('\n\n')

total = 0
for j in range(len(code_dict)):
    max_count = 0
    max_code = None
    for code in code_dict:
        code_count = code_dict[code]
        if code_count > max_count:
            max_count = code_count
            max_code = code
    code_dict.pop(max_code)
    top_file.write(str(max_count) + '\t' + max_code + '\n')
    total = total + 1
    if total >= 10:
        break

top_file.close()


