class HttpContext:
    def __init__(self,
                 method: str,
                 host: str,
                 path: str,
                 version: str = 'HTTP/1.1',
                 headers=None,
                 params=None,
                 body: str = None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        self.method = method
        self.headers = headers
        self.path = path
        self.host = host
        self.params = params
        self.body = body

    def __str__(self):
        from . import build_http_message
        return build_http_message(self.method, self.path, self.params, self.headers, self.body)

