import re


def main(s):
    """
    正则替换文本，去除富文本html标签。保留纯文本
    :param s:
    :return:
    """
    ss = re.sub('<[^<]*>', '', s)

    print(s)
    print(ss)


if __name__ == '__main__':
    s = '<p>aa<b>bb</b></p>'
    main(s)
