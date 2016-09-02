# -*- coding: utf-8 -*-

import re
from cgi import escape


def index(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return ['''Hello World Application
	           This is the hello world application:
	           `continue <hello/>`_
	        ''']


def hello(environ, start_response):
	args = environ['myapp.url_args']
	if args:
		subject = escape(args[0])
	else:
		subject = 'World'
	start_response('200 OK', [('Content-Type', 'text/html')])

	return ['''Hello %(subject)s
	           Hello %(subject)s!
	           ''' % {'subject': subject}]


def not_found(environ, start_response):
	start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
	return ['NOT FOUND']


# url到函数的映射
urls = [
	(r'^$', index),
	(r'hello/?$', hello),
	(r'hello/(.+)$', hello)
]


def application(environ, start_response):
	"""将当前请求的路径分发给不同的函数"""
	path = environ.get('PATH_INFO', '').lstrip('/')
	for regex, callback in urls:
		match = re.search(regex, path)
		if match is not None:
			environ['myapp.url_args'] = match.groups()
			return callback(environ, start_response)
	return not_found(environ, start_response)

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()