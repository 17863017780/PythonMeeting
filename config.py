
# 此文件为配置文件

# erp账号
ACCOUNT = [{
     'username': '*******',
     'pwd': '*******.'
}]

#用户cookie
COOKIE='3AB9D23F7A4B3C9B=7EUWJYTBWLKCG27QTVOWSIVISJW4V2Y7B5QN5TLEFJJRQJCCGT3UFTEFKAB4ICTH7RC3QRA4S3MUUSRPOM3GHDA27E;erp1.jd.com=FA934C1F4149BD27CB7CF7DD07DFDBA5680D2C5F426C4C9E9AA2F3DDBE6A0187A33AC5CD4D14AA9D435298BF2834FDEF65D05B88A35693973C877141422553DD7CB79F11BABDEC5316081A59DAB4B1E4;sso.jd.com=BJ.14478d54ef45452186705dfbcafdd931;jd.erp.lang=zh_CN;RT="z=1&dm=jd.com&si=ifpphvmime&ss=kdmz8sdh&sl=0&tt=0";__jda=234025733.15969709048011251019402.1596970905.1596970905.1596970905.1;__jdb=234025733.1.15969709048011251019402|1.1596970905;__jdc=234025733;__jdv=234025733|direct|-|none|-|1596970904802;__jdu=15969709048011251019402'

BASE_DATA = {
    "Monday": [
        {
            "id": "M01",
            "start":"1100",
            "end":"1200",
            "title": "小组会议"
        },
        {
            "id": "M02",
            "start":"1500",
            "end":"1600",
            "title": "小组会议"
        },
        {
            "id": "M03",
            "start":"1600",
            "end":"1700",
            "title": "小组会议"
        }
    ],
    "Tuesday": [
        {
            "id": "Tu01",
            "start": "1700",
            "end": "1800",
            "title": "小组会议"
        },{
            "id": "Tu02",
            "start": "1600",
            "end": "1700",
            "title": "小组会议"
        }
    ],
    "Wednesday": [
        {
            "id": "W01",
            "start": "1500",
            "end": "1600",
            "title": "小组会议"
        },
        {
            "id": "W02",
            "start": "1400",
            "end": "1500",
            "title": "部门分享"
        },{
            "id": "W03",
            "start": "1600",
            "end": "1700",
            "title": "部门分享"
        }
    ],
    "Thursday": [
        {
            "id": "Th01",
            "start": "1000",
            "end": "1100",
            "title": "小组会议"
        },
        {
            "id": "Th02",
            "start": "1400",
            "end": "1500",
            "title": "小组会议"
        },
        {
            "id": "Th03",
            "start": "1500",
            "end": "1600",
            "title": "小组会议"
        }
    ],
    "Friday": [
        {
            "id": "Fr01",
            "start": "0930",
            "end": "1030",
            "title": "小组会议"
        },
        {
            "id": "Fr02",
            "start": "1500",
            "end": "1600",
            "title": "小组会议"
        },
        {
            "id": "Fr03",
            "start": "1600",
            "end": "1700",
            "title": "小组会议"
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
