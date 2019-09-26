
import os

rootdir = 'C:/rj/nginx-1.17.0/html/1'

list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
	path = os.path.join(rootdir,list[i])
	newPath = os.path.join(rootdir,list[i].split("-")[0] + ".mp3")
	print(newPath)
	
	# 重命名，两个都是绝对路径 "c:/path/a.txt"
	os.rename(path, newPath)
