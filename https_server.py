import http.server
import ssl

server_address = ('127.0.0.1', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./cert.pem', keyfile='./key.pem', server_side=True)

print("Serving on https://127.0.0.1:4443")
httpd.serve_forever()
