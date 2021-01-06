

BASE_DATA2 = {
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
            "start": "1700",
            "end": "1800",
            "title": "小组会议"
        }
    ]
}

if __name__ == '__main__':
    todaydata=BASE_DATA2["Tuesday"]
    for item in todaydata:
        print("start:" + item["start"] +",end"+item["end"])