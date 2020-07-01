#调用接口的方法诶
import json
import requests
from datetime import datetime
from urllib import request
import config


# 调用预约会议室的接口
def book_meeting(meetingEstimateDate, meetingEstimateStime, meetingEstimateEtime, meetingSubject):
    print("调用预约会议室接口")
    url = 'http://jmrs.jd.com/meetingOrder/create'
    post_data = {
        'meetingName': "长城",
        'meetingCode': "2001006986",
        'workplaceCode': "1001000054",
        'districtCode': "13",
        'meetingEstimateDate': meetingEstimateDate,
        'meetingEstimateStime': meetingEstimateStime,
        'meetingEstimateEtime': meetingEstimateEtime,
        'bookJoyMeeting': 0,
        'joyMeetingParam': {'meeting': {'password': ""}},
        'meetingSubject': meetingSubject,
        'lang': "zh"
    }
    data = post_api(url, post_data)
    print("调用发送微信消息使用")

    # if data['resultCode'] == 0:
    #     # 预定失败
    #     book_success_remind(meetingEstimateDate, meetingEstimateStime, meetingEstimateEtime,
    #                               '失败，失败原因：' + data['message'])
    # else:
    #     book_success_remind(meetingEstimateDate, meetingEstimateStime, meetingEstimateEtime, '成功')

    return data

# 调用预约会议室的接口
def book_meeting3(meetingEstimateDate, meetingEstimateStime, meetingEstimateEtime, meetingSubject):
    print("调用预约会议室接口")
    url = 'http://jmrs.jd.com/meetingOrder/create'
    post_data = {
        'meetingName': "什刹海",
        'meetingCode': "2001001776",
        'workplaceCode': "1001000054",
        'districtCode': "13",
        'meetingEstimateDate': meetingEstimateDate,
        'meetingEstimateStime': meetingEstimateStime,
        'meetingEstimateEtime': meetingEstimateEtime,
        'bookJoyMeeting': 0,
        'joyMeetingParam': {'meeting': {'password': ""}},
        'meetingSubject': meetingSubject,
        'lang': "zh"
    }
    data = post_api(url, post_data)
    print("调用发送微信消息使用")
    return data


#已预约的会议室接口
def my_book_list():
    url = 'http://jmrs.jd.com/meetingOrder/queryOrderByUser'
    post_data = {
        "orderStatusList": [1, 3],
        "pageNo": 1,
        "pageSize": 10,
        "lang": "zh"
    }
    data = post_api(url, post_data)
    # print("需确认的会议室"+str(data))
    return data


#post 带有cookie的接口请求，返回返回值
def post_api(url, data):
    cookie_string = config.COOKIE
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'cookie': cookie_string,
    }

    res = requests.post(
        url=url,
        json=data,
        headers=headers
    )
    print('请求' + url)
    return res.json()

# post 没有cookie 的接口请求
def post_api_without_cookie(url, data):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    post_data = json.dumps(data).encode(encoding='utf-8')
    req = request.Request(
        url=url,
        data=post_data,
        headers=headers
    )
    res = request.urlopen(req)
    res_data = json.loads(res.read())
    return res_data


# 调用微信提醒的接口请求
def wx_remind(content):
    # print("开始发送微信消息")
    url = 'http://wxpusher.zjiecode.com/api/send/message'
    post_data = {
        "appToken": "AT_d39rjEPuTGpiBByN6zcOT1EmM54XPdzh",
        "content": content,
        "summary": '预定会议室消息通知',
        "contentType": 1,
        "topicIds": [
            123
        ],
        "uids": [
            "UID_hapkex44c5jlMzaS3rPexngYhD3z",
        ]
    }
    data = post_api_without_cookie(url, post_data)
    return data



# 只是把数据合起来
def book_success_remind(date, start, end, message):
    # print("准备发送微信消息")
    wx_remind('预约 ' + str(date) + ', ' + str(start) + '至' + str(end) + '  ' + message)




def judge_whether_appointment(time_now, time_num):
    # 确定时间是 time_num 往前 29分钟
    time_num_str = str(time_num)
    if time_num >= 1000:
        hour = int(time_num_str[0:2]) * 100
        minute = int(time_num_str[2:4])
    else:
        hour = int(time_num_str[0:1]) * 100
        minute = int(time_num_str[1:3])

    if minute > 0:
        # minute == 30
        the_appoint_time = hour
    else:
        # minute == 0
        # 减去一小时 再加上31分钟
        the_appoint_time = hour - 100 + 30
    print('下一个确认时间：' + str(the_appoint_time))


# 确认会议室后发送消息
def confirm_success_remind(date, message):
    wx_remind('确认 ' + str(date) + ' 会议室 ' + message)


def confirm_meeting(meetingOrderCode):
    url = 'http://jmrs.jd.com/meetingOrder/confirm'
    post_data = {
        "meetingOrderCode": meetingOrderCode,
        "lang": "zh"
    }
    data = post_api(url, post_data)
    if data['resultCode'] == 0:
        # 预定失败
        confirm_success_remind(str(datetime.date.today()),
                                     '失败，失败原因：' + data['message'])
    else:
        confirm_success_remind(str(datetime.date.today()), '成功')
    return data