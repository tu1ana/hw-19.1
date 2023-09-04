from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from pathlib import Path

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        filepath = Path.cwd() / 'hw19_1.html'
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
        return content

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped')
