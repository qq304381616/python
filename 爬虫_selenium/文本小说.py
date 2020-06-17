"""下载整部小说到文件。大概12M，运行时间长"""
# -*- coding:UTF-8 -*-
from selenium import webdriver


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 增加无界面选项
    options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
    browser = webdriver.Chrome(options=options)
    browser.get("http://www.biqukan.com/1_1094/")

    # print(f"browser text = {browser.page_source}")  # 输出页面内容

    names = browser.find_elements_by_xpath("//dl//dd//a")

    books = {}
    print("开始解析所有章节")
    for i in names:
        books[i.get_attribute("href")] = i.text
    print("结束解析所有章节")

    f = open('a.txt', 'a', encoding='utf-8')
    for item in books:  # 遍历
        print(item, books[item])
        browser.get(item)
        try:
            info = browser.find_element_by_xpath("//*[@id='content']")
            f.write(books[item])
            f.write("\n\n")
            f.write(info.text)
            f.write("\n" + "*" * 100 + "\n\n")
        except BaseException as err:
            print(err)
    f.close()
    browser.quit()


if __name__ == "__main__":
    main()