import os

rootDir = r'C:\Users\hl\Desktop\test'

if os.path.exists(rootDir) and os.path.isdir(rootDir):  # 判断文件存在并且是文件夹
    fileList = os.listdir(rootDir)  # 列出文件夹下所有的目录与文件
    for item in fileList:
        oldFile = os.path.join(rootDir, item)

        if os.path.isdir(oldFile) is False:  # 判断是文件
            (filename, extension) = os.path.splitext(item)  # 获取文件名和扩展名
            newFile = os.path.join(rootDir, filename + "_new" + extension)
            os.rename(oldFile, newFile)
