#！/usr/bin/env python
# _*_ coding:utf-8 _*
import urllib.request
import urllib.error
import re
class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)
    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib.request.Request(url)
            response=urllib.request.urlopen(request)
            # localFile=open('E:\Pro_py3/tieba.txt','wb+')
            # localFile.write(response.read())
            # localFile.close()
            print(response.read())
            return response
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败，错误原因",e.reason)
            return None
    def getTitle(self):
        page=self.getPage(1)
        pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result=re.search(pattern,page)
        if result:
            print(result.group(1))
            return result.group(1).strip()
        else:
            return None
def main():
    baseURL='http://tieba.baidu.com/p/3138733512'
    bdtb=BDTB(baseURL,1)
    bdtb.getTitle
if __name__ == '__main__':
    main()