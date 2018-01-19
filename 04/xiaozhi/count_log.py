counts_data = {}
sorted_list = []


def count_log_(log):
    with open(log) as f:
        for lines in f:
            yield lines


def count_data():
    for line in count_log_("www_access_20140823.log"):
        if line:
            data = line.strip().split(" ")
            if len(data) > 3:
                ip, url, status = data[0], data[6], data[8]
                counts_data[(ip, url, status)] = counts_data.get((ip, url, status), 0) + 1
    for k, v in counts_data.items():
        sorted_list.append((v, k))
    top_ten = (sorted(sorted_list)[-10:])
    return top_ten


def main():
    with open("top_ten_log.log", "w") as f:
        for v, k in count_data():
            f.write("{k}:{v}\n".format(k=k, v=v))

main()
