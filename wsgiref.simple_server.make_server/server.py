from wsgiref.simple_server import make_server

from test import application

# 创建一个服务器，访问127.0.0.1:8000。处理函数是application:
httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on 127.0.0.1:8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
