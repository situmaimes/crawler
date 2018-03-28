import requests

def search(keyword):
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Host":"weixin.sogou.com",
        "Referer":"http://weixin.sogou.com/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }
    cookies={
        "SUID":"BF81C1704F18910A000000005A05BA0C",
        "ABTEST":"0|1510324748|v1",
        "IPLOC":"CN5101",
        "SUV":"0092175470C181BF5A05BA0C58843511",
        "weixinIndexVisited":"1"
    }
    params={
        "type":"1",
        "query":"交大有思",
        "ie":"utf8",
        "s_from":"input",
        "_sug_":"n",
        "_sug_type_":""
    }
    headers2={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Host":"mp.weixin.qq.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }
    s=requests.session()
    response=s.get("http://weixin.sogou.com/weixin",params=params,cookies=cookies,headers=headers)
    print(response.status_code)

    response=s.get("https://mp.weixin.qq.com/profile?src=3&timestamp=1510324780&ver=1&signature=99FeHLDwNvlGUQge333xOO*bdMermsSRrfAXyVnKib*MdB646vVw00y66h3i55szTYWUJve27RpJZkCGhGHLmw==",headers=headers2)
    print(response.status_code)
    print(response.text)
if __name__=="__main__":
    search("")
    "/s?timestamp=1510325403&src=3&ver=1&signature=*Ry41-ZLL6*9MrKKix*kVLZAsTYTLWKCptey3RnaupViDOr8n1vX8AnLLCb6EyUM8*RQqdnsqLk*M*uX5BJHjRpJHpAzx38Ch7*BNxKh0pM1iaAo-PpYoes4SxXQbpgQZwOuEkupOI2sfAN8O5-ayyrCaDHUAA53zRBQwiuCXWs="