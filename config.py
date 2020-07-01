
# 此文件为配置文件

# erp账号
ACCOUNT = [{
     'username': 'ccjh1',
     'pwd': 'Cjh202003.',
}]

#用户cookie
COOKIE='sso.jd.com=HK.fbd577775ca446bc81b3b055f101aec0;jd.erp.lang=en_US;RT="z=1&dm=jd.com&si=8e0t86wk50g&ss=kc2q5d8h&sl=0&tt=0";__jda=234025733.15935695228021692808516.1593569523.1593569523.1593569523.1;__jdb=234025733.1.15935695228021692808516|1.1593569523;__jdc=234025733;__jdv=234025733|direct|-|none|-|1593569522806;__jdu=15935695228021692808516'

BASE_DATA = {
    "Monday": [
        {
            "id": "M01",
            "start": 1100,
            "end": 1200,
            "title": "小组会议"
        },
        {
            "id": "M02",
            "start": 1500,
            "end": 1600,
            "title": "小组会议"
        }
    ],
    "Tuesday": [
        {
            "id": "Tu01",
            "start": 1700,
            "end": 1800,
            "title": "小组会议"
        }
    ],
    "Wednesday": [
        {
            "id": "W01",
            "start": 1400,
            "end": 1500,
            "title": "小组会议"
        },
        {
            "id": "W03",
            "start": 1500,
            "end": 1600,
            "title": "部门分享"
        }
    ],
    "Thursday": [
        {
            "id": "Th01",
            "start": 1400,
            "end": 1500,
            "title": "小组会议"
        },
        {
            "id": "Th02",
            "start": 1500,
            "end": 1600,
            "title": "小组会议"
        }
    ],
    "Friday": [
        {
            "id": "F01",
            "start": 1400,
            "end": 1500,
            "title": "部门会议"
        },
        {
            "id": "F03",
            "start": 1500,
            "end": 1600,
            "title": "大部门会议"
        },
        {
            "id": "F03",
            "start": 1600,
            "end": 1700,
            "title": "大部门会议"
        }
    ]
}


SHICHAHAIWORKSPACE={
    "meetingName'": "什刹海",
    "meetingCode": "2001001776"
}

CHANGCHENGWORKSPACE={
    "meetingName'": "长城",
    "meetingCode": "2001006986"
}





# 周一 0   约周二 1
# 周二 1   约周三 2
# 周三 2   约周四 3
# 周四 3   约周五 4
# 周五 4   约周一 0
# 周六 5   约周一 0
# 周日 6   约周一 0
BOOK_TIME_SEQ = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Monday', 'Monday']
