import requests


def download_pic(url, path):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)  # 下载图片，之后保存到文件
    with open(path, 'wb') as f:
        f.write(r.content)


def main():
    download_pic("https://www.baidu.com/img/bd_logo1.png", "C:\a.png")


if __name__ == '__main__':
    main()
