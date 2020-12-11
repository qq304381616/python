from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# 创建一个服务器，访问127.0.0.1:8000。处理函数是application:
httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on 127.0.0.1:8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
