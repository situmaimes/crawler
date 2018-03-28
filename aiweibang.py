import requests
import re
import codecs
import json
s=requests.session()
headers={
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Host":"top.aiweibang.com",
        "Origin":"http://top.aiweibang.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/62.0.3202.75 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",

    }
def search(keyword):
    gongzhonghao = {}
    index=1
    url="http://top.aiweibang.com/user/getsearch"
    data={"PageSize":10,"Kw":keyword}
    while index<=10:
        data['PageIndex']=index
        response=s.post(url=url,headers=headers,data=data)
        response=response.json()
        if response['data']['data'] == []:
            break
        else:
            for i in response['data']['data']:
                gongzhonghao[i["Id"]]={
                    'Name':process(i["Name"]),
                    'Alias': i["Alias"],
                    'WechatId': i["WechatId"],
                    'Description': process(i["Description"]),
                    'TopReadNumAvg': i["TopReadNumAvg"],
                    'TopLikeNumAvg': i["TopLikeNumAvg"]}
            index=index+1
    print(len(gongzhonghao))


def getarticls(id,type=0):
    index=1
    url = "http://top.aiweibang.com/article/getarticles"
    data = {"PageIndex": 1,"PageSize": 20,"Type":type,"wechat":id}
    articles = {}
    while index<=10:
        data['PageIndex']=index
        response=s.post(url=url,headers=headers,data=data)
        response=response.json()
        if response['data']['data'] == []:
            break
        else:
            for i in response['data']['data']:
                articles[i["Id"]]={
                    'Title':i["Title"],
                    'LikeNum': i["LikeNum"],
                    'PostTime': i["PostTime"],
                    'ReadNum': i["ReadNum"]}
            index=index+1
    print(len(articles))
    template = "http://top.aiweibang.com/article/url?aid="
    for i in articles:
        articles[i]["url"]=template+i
    with codecs.open("公众号.json",'w',encoding="utf-8") as f:
        f.write(json.dumps(articles,ensure_ascii=False,indent=2))

def process(string):
    return re.sub("<.*?>","",string)
if __name__=="__main__":
    #search("西南交大")
    getarticls(id="LMO9OcOgw6jCsQ~~")
