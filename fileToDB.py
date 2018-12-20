
# 读取文件内容，更新数据库。

import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='1qaz2wsX', database='sim')
cursor = conn.cursor()

# 打开文件
f = open('1.txt', 'r', encoding='utf8')
logF = open('log.txt', 'a+', encoding='utf8')
s = f.readlines()

qureySql = 'select * from t_member where name = %s'
updateSql = 'UPDATE t_member SET telephone = %s WHERE name = %s'

def printLog(log):
    print(log)
    logF.write(log)
    logF.write('\n')
    

for x in s:
    printLog('------------------------------------------------------------------------')
    printLog('开始-------------' + x.strip())
    y = x.strip().split(' ')
    printLog('姓名：' + y[0])
    printLog('联系方式: ' + y[len(y)-1])

    cursor.execute(qureySql, (y[0],))
    values = cursor.fetchall()
    if(len(values) == 1) :
        cursor.execute(updateSql, (y[len(y)-1],y[0]))
        conn.commit()
        printLog("修改成功")
        
    else :
        printLog('搜索到多条数据，放弃修改')
    printLog('结束-------------')
    
# 关闭资源
f.close()
cursor.close()
conn.close()


    
    
    
    