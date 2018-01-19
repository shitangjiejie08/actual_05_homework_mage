
trance = {'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,
           }


def tranc_time(para):
    para1 = para.split("/")
    para2 = para1[-1].split(":", 1)
    para3 = para2[0] + "-" + str(trance[para1[1]]) + "-" + para1[0] + " " + para2[1]
    return para3

path1 = "31/Jul/2017:09:27:34 +0800"
print(tranc_time(path1.split(" ")[0]))