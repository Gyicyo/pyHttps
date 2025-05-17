import socket

from utils import build_http_messages


class HTTPSession:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.version = 'HTTP/1.1'
        self.headers = {'host': host}

    # GET / crl.py
    # HTTP / 1.1
    # Host: 127.0.1:8120
    # Accept - Encoding: identity

    def get(self, path: str, headers=None, params=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        messages = build_http_messages('GET', path, params, self.headers | headers)
        for message in messages:
            self.socket.send(message.encode())
        # Todo: url过长问题？
        return response(self.socket)

    def post(self, path: str, headers=None, params=None, body=None):
        pass

    def close(self):
        self.socket.close()


class response:
    def __init__(self, socket):
        self.socket = socket
        self.status_code = None
        self.headers = None
        self.body = None