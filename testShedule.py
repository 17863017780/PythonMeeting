

# 此文件是为了测试一些定时任务等
import json
from urllib import request

if __name__ == '__main__':
    # print("开始发送微信消息")
    url = 'http://wxpusher.zjiecode.com/api/send/message'
    post_data = {
        "appToken": "AT_d39rjEPuTGpiBByN6zcOT1EmM54XPdzh",
        "content": "测试成功",
        "summary": '测试成功',
        "contentType": 1,
        "topicIds": [
            123
        ],
        "uids": [
            "UID_hapkex44c5jlMzaS3rPexngYhD3z",
            "UID_10gjpt960uQLBYnJz87ZwztojsAT"
        ]
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    post_data = json.dumps(post_data).encode(encoding='utf-8')
    req = request.Request(
        url=url,
        data=post_data,
        headers=headers
    )
    res = request.urlopen(req)
