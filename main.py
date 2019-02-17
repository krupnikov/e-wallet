import logging
import json
import socket
from wallet import *

URLS = {
    '/': '/'
}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='service.log')
logging.info("StartApp")

def parse_request(data):
    parsed = data.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def get_body(data):
    parsed = data.split('\r\n\r\n')
    body = json.loads(parsed[1])
    print(body)
    return (body)


def generate_headers(method, url):
    if not method == 'POST':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if url not in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not found</p>'
    return 'OK'


def generate_response(data):
    method, url = parse_request(data)
    body = get_body(data)
    headers, code = generate_headers(method, url)
    main_job(body)
    return headers.encode()


def run_service():
    HOST = ''
    PORT = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            # logging.INFO('Server connected by ' + str(addr))
            data = conn.recv(1024)
            # logging.INFO(data.decode('utf-8'), '\n')
            response = generate_response(data.decode('utf-8'))
            conn.close()


if __name__ == '__main__':
    run_service()
