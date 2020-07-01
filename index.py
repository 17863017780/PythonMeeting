import _thread
import datetime
import time
import sscLogin
import config
import api

# 调用登录

sscLogin.login()
# cookie 可更新
# print(" 更新后的 cookie is：" + config.COOKIE)

#判断是否运行
RUN_STATUS = True
#需要预约的会议室
BASE_DATA = config.BASE_DATA
# 约哪天的
BOOK_TIME_SEQ = config.BOOK_TIME_SEQ


today = str(datetime.date.today())
tm_wday = time.localtime().tm_wday  # 今天星期几
print('今天星期', tm_wday, type(tm_wday))
# print(BOOK_TIME_SEQ)
today_book_tag = BOOK_TIME_SEQ[tm_wday]  # 今日需要预约序号名称
today_book_list = BASE_DATA[today_book_tag]  # 今日需要预约列表

#今日已确认的数据
already_confirm_list=[]

# 计算今日续约的日期
# 周 1 2 3 4  加 1天
# 周 5  加 3天
if tm_wday < 4:
    today_book_date = datetime.date.today() + datetime.timedelta(1)
else:
    today_book_date = datetime.date.today() + datetime.timedelta(3)


def book_meeting(item):
    # item 为初始化数据 包含 start end title
    print("还没调用接口")
    api.book_meeting3(today_book_date.isoformat(), item['start'], item['end'], item['title'])
    return True

# 找到明天预约的数据
def appoint_meeting():
    #  初始化已经预约的数据
    all_confirm_list = api.my_book_list()['data']['rows']
    # print(str(all_confirm_list))
    for item in all_confirm_list:
        print(item['meetingEstimateDate']+"=="+today_book_date.isoformat())
        if item['meetingEstimateDate'] == today_book_date.isoformat() :
            api.book_success_remind(item['meetingEstimateDate'],item['meetingEstimateStime'],item['meetingEstimateEtime'],"成功")
    # print("发送消息成功")
    return True

#找到今天预约的数据，是否需要确认
def appoint_meeting_today():
    today_confirm_list = api.my_book_list()['data']['rows']
    temp = filter(lambda item: item['meetingEstimateDate'] == today, today_confirm_list)
    today_confirm_list = list(temp)
    print('今日需确认会议室列表：', today_confirm_list)
    return today_confirm_list

def confirm_meeting(meetingOrderCode):
    # 将该确认码 添加至已确认列表
    already_confirm_list.append(meetingOrderCode)
    print('今天已确认', already_confirm_list)
    api.confirm_meeting(meetingOrderCode)
    return True



if __name__ == '__main__':
    #  该逻辑为预定逻辑
    #  9：00 将执行
    #  周六日 不执行
    if tm_wday < 5:
        while RUN_STATUS:
            now = time.localtime()
            cur_time_number = int(time.strftime('%H%M', now))
            if cur_time_number >= 900:
                print('开始预约：1')
                for item in today_book_list:
                    book_meeting(item)
                #这里加一步，去根据预约信息，发送短信
                appoint_meeting()
                break
            else:
                print(str(cur_time_number) + ',还未到上午9点')
            time.sleep(1)
        print("执行完毕，应该会发送两条消息")
        today_confirm_list = appoint_meeting_today()

        while RUN_STATUS:
            #  该逻辑为确认逻辑
            #  到达确认时间需要执行
            now = time.localtime()
            cur_time_number = int(time.strftime('%H%M', now))  # 符合平台规范的特殊时间数字  1001 代表10:01
            time.sleep(5)
            for item in today_confirm_list:
                # print(item['meetingOrderCode'])
                # print(item['meetingEstimateStime'])
                status = (item['meetingOrderCode'] not in already_confirm_list) and (
                    api.judge_whether_appointment(cur_time_number, item['meetingEstimateStime'])
                )

                if status:
                    print('执行确认', cur_time_number, status)
                    confirm_meeting(item['meetingOrderCode'])
            if cur_time_number > 1800:
                # 每天六点后 关闭程序
                break


def book_meeting2(startTime, endTime):
    print("还没调用接口")
    api.book_meeting(today_book_date.isoformat(), startTime, endTime,"小组会议")


def a():
    #  该逻辑为预定逻辑
    #  9：00 将执行
    #  周六日 不执行
    if tm_wday < 5:
        while RUN_STATUS:
            now = time.localtime()
            cur_time_number = int(time.strftime('%H%M', now))
            print("当前时间为："+ str(cur_time_number))
            if cur_time_number >= 900:
                print('开始预约：1')
                try:
                    _thread.start_new_thread(book_meeting2,("1900","1930",))
                    _thread.start_new_thread(book_meeting2,("1930", "2000",))
                except:
                    print("Error: 无法启动线程")
                time.sleep(5)
                break
            else:
                print(str(cur_time_number) + ',还未到上午9点')
            time.sleep(1)
    print("执行完毕，应该会发送两条消息")