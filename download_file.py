import requests, re, json, sys
from bs4 import BeautifulSoup
from urllib import request


class video_downloader():
    
    def __init__(self):
        pass
        
    def Schedule(self, a, b, c):
        per = 100.0*a*b/c
        if per > 100 :
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per,a*b,c) + '\r')
        sys.stdout.flush()
        
    def download(self, url, filename):
        request.urlretrieve(url=url, filename = filename,reporthook=self.Schedule)

if __name__ == '__main__':
    url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
    vd = video_downloader()
    filename = '下载文件'
    print('%s下载中：' % filename)
    vd.download(url, filename + '.xlsx')
    print('\n下载完成!')