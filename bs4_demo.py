
"""
解析器
1， html.parser 系统提供无需安装. 默认参数
2， $ pip install lxml
3， $ pip install html5lib
"""

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# soup = BeautifulSoup(open("index.html")) ＃ 文件方式

# 格式化输出html
print(soup.prettify())

print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# u'title'

print(soup.title.string)
# u'The Dormouse's story'

print(soup.title.parent.name)
# u'head'

print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])
# u'title'

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find(id="link3"))
# <a class="sister" href

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

# 从文档中获取所有文字内容:
print(soup.get_text())

# 子节点
print(soup.head.contents) # [<title>The Dormouse's story</title>]

# 遍历子节点
for child in soup.head.children:
    print(child)

# 递归遍历子节点
for child in soup.head.descendants:
    print(child)

# 没有子节点，可以使用.string
print(soup.title.string) # The Dormouse's story

# 遍历节点字符串
for string in soup.strings: # 使用 stripped_strings。过滤掉空白内容
    print(repr(string))

print("获取父节点")
print(soup.title.parent)

print("遍历所有父节点:")
for parent in soup.title.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("获取兄弟节点：")
print(soup.head.next_sibling)
print(soup.head.previous_sibling)
print("遍历获取兄弟节点：")
for sibling in soup.head.next_siblings:
    print(repr(sibling))
for sibling in soup.head.previous_siblings:
    print(repr(sibling))

print("回退和前进:")
print(soup.find("a", id="link3").next_element)
print(soup.find("a", id="link3").previous_element)
for element in soup.find("a", id="link3").next_elements:
    print(repr(element))

print("搜索文档树:")
print(soup.find_all('b'))

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print(soup.find_all(["a", "b"])) # 包含 a 和 b
#print(soup.find_all(True)) # 所有节点

print("指定方法为查找参数：")
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))
def not_lacie(href):
        return href and not re.compile("lacie").search(href)
print(soup.find_all(href=not_lacie))

print("方法说明： find_all( name , attrs , recursive , string , **kwargs )")
print(soup.find_all("title"))
print(soup.find_all(id="link2"))
print(soup.find_all("p","title")) # P 标签下包含title 
print(soup.find_all(id=True)) # 所有有ID属性的标签
soup.find_all(href=re.compile("elsie"), id='link1') # 两个参数并且的结果
soup.find_all(attrs={"data-foo": "value"}) # 参数不支持搜索的。使用这种方式
soup.find_all("a", class_="sister") # a 标签 指定class的结果
print(soup.find_all(string="Elsie"))
print(soup.find_all("a", limit=2)) # 指定搜索数量
print(soup.html.find_all("title", recursive=False)) # 搜索子节点，不包含子孙节点。 默认true为搜索全部子孙节点


print("方法说明：find( name , attrs , recursive , string , **kwargs )")
print(soup.find('title'))

print("方法说明：find_parents() 和 find_parent()")
print("方法说明：find_next_siblings() 和 find_next_sibling()")
print("方法说明：find_previous_siblings() 和 find_previous_sibling()")
print("方法说明：find_all_next() 和 find_next()")
print("方法说明：find_all_previous() 和 find_previous()")

print("CSS选择器: select()")
print(soup.select("title")) # [<title>The Dormouse's story</title>]
soup.select("p:nth-of-type(3)")
print(soup.select("body a")) # 逐层查找
soup.select("head > title") # 直接子标签
soup.select("p > #link1") # 子标签下指定id
soup.select("#link1 ~ .sister") # 兄弟标签
soup.select("#link1 + .sister") # 兄弟标签
soup.select(".sister") # 类名查找
soup.select("[class~=sister]") # 类名查找
soup.select("#link1") # id 查找
soup.select("a#link2") # 标签下指定id查找
soup.select("#link1,#link2") # 查找多个符合条件的
soup.select('a[href]') # 标签下包含指定属性
soup.select('a[href="http://example.com/elsie"]') # 通过属性的值来查找
soup.select('a[href^="http://example.com/"]') # 通过属性的值来查找
soup.select('a[href$="tillie"]') # 通过属性的值来查找
soup.select('a[href*=".com/el"]') # 通过属性的值来查找
soup.select_one(".sister") # 返回查找到的元素的第一个

print("修改文档树.. 略")