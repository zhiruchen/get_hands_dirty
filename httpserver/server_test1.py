from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8080

if __name__ == '__main__':
    httpd = TCPServer(("", PORT), SimpleHTTPRequestHandler)
    print("servering at: ", PORT)
    httpd.serve_forever()

