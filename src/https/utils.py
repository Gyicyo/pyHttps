from .httpContext import HttpContext


def build_http_messages(method: str, path: str, params: dict, headers: dict, body: str = None) -> [str]:
    # Todo: 实现body切片传输，返回多个http消息
    pass


def build_http_message(method: str, path: str, params: dict, headers: dict, body: str = None) -> str:
    if params:
        if '?' not in path:
            path += f"?&{'&'.join([f'{key}={value}' for key, value in params.items()])}"
        else:
            path += f"&{'&'.join([f'{key}={value}' for key, value in params.items()])}"

    message = f"{method.upper()} {path} HTTP/1.1\r\n"

    if not headers:
        return message

    for key, value in headers.items():
        message += f'{key}: {value}\r\n'
    message += '\r\n'

    # Todo: 解决大文件分块传输

    if body:
        message += body

    return message


def parse_header_message(message: str) -> HttpContext:
    # Todo: 解决大文件分块传输
    lines = message.split('\r\n')
    method, path, version = lines[0].split(' ')
    params = {}
    if '?' in path:
        path, params = path.split('?')
        params = dict(v.split('=') for v in params.split('&'))

    headers = {}
    for line in lines[1:]:
        if line == '':
            break
        key, value = [v.strip() for v in line.split(':')]
        headers[key.lower()] = value
    host = headers['host']

    body = None
    if 'content-length' in headers.keys():
        body = message[len(message) - int(headers['content-length']):]

    return HttpContext(method, host, path, version, headers, params, body)
