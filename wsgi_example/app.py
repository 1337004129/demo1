# coding:utf-8
# todo 访问方法
# def simple_app(environ, start_response):
#     """Simplest possible application object"""
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/html')]
#     # start_response(status, response_headers)
#     # return [b'Hello world! -by the5fire \n']

# todo 访问实例
# class Appclass(object):
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/html')]
#
#     def __call__(self, environ, start_response):
#         print(environ, start_response)
#         start_response(self.status, self.response_headers)
#         return [b'Hello AppClass.__call__\n']
#
#
# application = Appclass()

# todo 访问类
class AppClassIter(object):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response(self.status, self.response_headers)
        yield b'Helloooooooooooooo\n'
