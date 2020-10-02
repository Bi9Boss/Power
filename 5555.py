import requests
import re
s = {"uid": "你的学号","upw": "你的密码","smbtn": "进入健康状况上报平台","hh28": "354"}
url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
r = requests.post(url,data=s,verify = False)
str1 = r.text
x = re.search('ptopid=\w+',str1)
pid = x.group(0)[7:]
x = re.search('sid=\w+',str1)
sid = x.group(0)[4:]
url1 = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
Formdata1 = {
    "day6":"b",
    "did":"1","door":"",
    "men6":"a",
    "ptopid":pid,
    "sid":sid
    }

requests.post(url1, data=Formdata1, verify=False)

Formdata2 = {
    "myvs_1":"否",
    "myvs_2":"否",
    "myvs_3":"否",
    "myvs_4":"否",
    "myvs_5":"否",
    "myvs_6":"否",
    "myvs_7":"否",
    "myvs_8":"否",
    "myvs_9":"否",
    "myvs_10":"否",
    "myvs_11":"否",
    "myvs_12":"否",
    "myvs_13a":"41", #代表河南省
    "myvs_13b":"4101", #代表郑州市
    "myvs_13c":"地址",
    "myvs_14":"否",
    "myvs_14b":"",
    "myvs_15":"否",
    "myvs_16":"在家办公",
    "myvs_16b":"",
    "myvs_17":"D",
    "myvs_18":"X",
    "did":"2",
    "door":"",
    "day6":"b",
    "men6":"a",
    "sheng6":"",
    "shi6":"",
    "fun3":"",
    "ptopid":pid,
    "sid":sid
    }
requests.post(url1, data=Formdata2, verify=False)
