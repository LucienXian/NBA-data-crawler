import json

data = [
{
    "entities": {
        "description": {
            "urls": 2
        }
    },
    "utc_offset": -10800,
    "id" : 4,
    "name": "Tom",
    "hit_count": 7931,
    "private": False,
    "active_last_month": False,
    "location": "",
    "contacted": False,
    "lang": "en",
}
,
{
    "entities": {
        "description": {
            "urls": 2
        }
    },
    "utc_offset": -10500,
    "id" : 5,
    "name": "中国人",
    "hit_count": 554,
    "private": False,
    "active_last_month": False,
    "location": "",
    "contacted": False,
    "lang": "en",
}
]




with open('testJson', 'w+') as json_file:
    jsoned_data = json.dumps(data, indent=4)
    json_file.write(jsoned_data)


with open('testJson', 'r') as json_file:
    json_data = json.load(json_file)
    for key in json_data:
        print(key["name"])
        print(key["hit_count"])
        print(key["entities"]["description"]["urls"])
