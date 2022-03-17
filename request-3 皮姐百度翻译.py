
#AJAX请求（XHR）：通过XMLHttpRequest可以在不刷新页面的情况下请求特定URL获取数据。这允许网页在不应喜那个用户操作的情况，更新页面的局部内容
import requests
import json

if __name__ == "__main__":      
    post_url = 'https://fanyi.baidu.com/sug'
    #进行UA伪装
    headers ={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    #post请求参数处理
    word = input('enter a word:')
    data = {
        'kw':word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    #获取响应数据:json()方法返回的是obj（如果确认响应数据是json类型，才可以使用）
    dic_obj = response.json()

    #持久化存储
    fileName = word +'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False) #中文不能使用ascii
    print('over!')

