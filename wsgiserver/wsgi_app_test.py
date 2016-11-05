# -*- coding: utf-8 -*-

"""
wsgi 入门
wsgi: web服务器与web应用之间通信的接口
"""


def application(environ, start_response):
    """
    wsgi的应用接口: 一个可调用对象
    :param environ: 由服务器为每一个请求配置的cgi环境变量的字典
    :param start_response: 由server提供的回调函数，参数为http 状态和头部
    :return: 可迭代的
    """

    response_body = 'request method: %s' % environ['REQUEST_METHOD']

    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]

    # 用start_response发送响应状态码，消息和头部给server
    start_response(status, response_headers)

    return [response_body]
