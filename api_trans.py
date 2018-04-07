#！/usr/bin/env python
# _*_ coding:utf-8 _*_
'''调用百度翻译api'''
'''https://blog.csdn.net/mr_guo_lei/article/details/78617669'''
import requests
import string
import time
import hashlib
import json

# init
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = 20180402000142237
cyber = 'TvOtNt7JXELnrYuD5LES'
# lower_case = list(string.ascii_lowercase)


def requests_for_dst(word):
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    # 区别en,zh构造请求参数
    # if list(word)[0] in lower_case:
    paramas = {
        'q': word,
        'from': 'en',
        'to': 'zh',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    # else:
    #     paramas = {
    #         'q': word,
    #         'from': 'en',
    #         'to': 'zh',
    #         'appid': '%s' % my_appid,
    #         'salt': '%s' % salt,
    #         'sign': '%s' % final_sign
    #     }
    #     my_url = api_url + '?appid=' + str(
    #         my_appid) + '&q=' + word + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']
    print(json_reads['trans_result'][0]['dst'])


# while True:
#     word = input("输入你想翻译的内容: ")
#     requests_for_dst(word)

if __name__ == "__main__":
    # f = open(r'E:\研二\接活/ch.txt', 'w')
    with open(r'E:\研二\接活/en.txt', 'r') as tmp1:
        for tmp in tmp1:
            tmp = requests_for_dst(tmp)
            print(tmp)
            # f.write(tmp + '\n')
    # f.close()