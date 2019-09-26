

import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='1qaz2wsx', database='db')
cursor = conn.cursor()

# %s代表参数
sql = "select * from user where id = %s;"

# 参数放括号里，1个参数也要加逗号
cursor.execute(sql, (id,))
conn.commit()

# 关闭资源
cursor.close()
conn.close()