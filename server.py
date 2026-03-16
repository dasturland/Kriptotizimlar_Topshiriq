import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

class SecureHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Agar foydalanuvchi asosiy sahifaga kelsa, index.html ni ko'rsat
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, SecureHandler)

# SSL Sozlamalari (avvalgi kabi)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.load_verify_locations(cafile="MyRootCA.crt")
context.verify_mode = ssl.CERT_REQUIRED

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Server ishga tushdi: https://localhost:4443")
httpd.serve_forever()