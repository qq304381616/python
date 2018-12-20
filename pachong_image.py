
# 网站爬虫 下载图片
# -*- coding:UTF-8 -*-
import requests, json 
from contextlib import closing

class get_photos(object):
    
    def __init__(self):
        self.photo_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=true'
        # page:页号，per_page:数量
        self.target = 'http://unsplash.com/napi/photos?page=1&per_page=3&order_by=latest'

    def getIds(self):
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url=self.target, verify=False)
        html = json.loads(req.text)
        for each in html:
            self.photo_id.append(each['id'])

    def download(self, photo_id, filename):
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(url = target, stream = True, verify = False)) as r:
            with open('%d.jpg' % filename , 'ab+') as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
             
        
if __name__ == '__main__':
    gp = get_photos()
    gp.getIds()
    for i in range(len(gp.photo_id)):
        print('正在下载第 %d 张图片' % (i+1))
        gp.download(gp.photo_id[i], (i+1))