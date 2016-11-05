# -*- coding: utf-8 -*-

"""
输出 CGI 环境变量
"""
from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = [
        '%s: %s' % (k, v) for k, v in sorted(environ.items())
    ]

    response_body = '\n'.join(response_body)
    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]

    # 用start_response发送响应状态码，消息和头部给server
    start_response(status, response_headers)

    return [response_body]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8051, application)
    httpd.handle_request()
