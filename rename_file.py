# 批量修改文件夹内文件名，参数为文件夹路径!不能有空格

import os
import sys

def main(dir):
    subdir = os.listdir(dir)
    index = 100
    for i in subdir:
        path = os.path.join(dir, i)
        print(i)
        if os.path.isdir(path) is False:
            (filename,extension) = os.path.splitext(i)
            index = index + 1
            newname = "type_" + str(index) + extension
            os.rename(path, os.path.join(dir, newname))

if __name__ == '__main__':
    main(sys.argv[1])