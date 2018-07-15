import json

data = [
{
    "entities": {
        "description": {
            "urls": []
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
            "urls": []
        }
    },
    "utc_offset": -10500,
    "id" : 5,
    "name": "Scrapy网络爬虫实战[保存为Json文件及存储到mysql数据库]. 2016年09月18 ... Scrapy 是一个为了爬取网站数据，提取结构性数据而编写的python应用框架。 可以应用在 .... 下一篇Java多线程网络爬虫(时光网为例). 想对作者说点 ...",
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