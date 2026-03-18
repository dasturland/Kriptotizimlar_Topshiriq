import ssl
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

class SecureHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Logga yozish
        log_message = f"[{datetime.now()}] {self.client_address[0]} - {self.command} {self.path}"
        print(log_message)
        
        # Asosiy sahifa
        if self.path == '/':
            self.path = '/index.html'
        
        # Xavfsizlik headerlari
        self.send_response(200)
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        
        return super().do_GET()
    
    def log_message(self, format, *args):
        # Standart logni o'chirish
        pass

def create_secure_server():
    """Xavfsiz SSL server yaratish"""
    server_address = ('localhost', 4443)
    httpd = HTTPServer(server_address, SecureHandler)
    
    # SSL kontekst - eng yuqori xavfsizlik darajasi
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # Zamonaviy protokollar va shifrlash
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.set_ciphers(
        'ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS'
    )
    
    # Sertifikatlar yuklash
    context.load_cert_chain(
        certfile="server.crt",
        keyfile="server.key"
    )
    
    # Klient sertifikatlarini tekshirish (mTLS)
    context.load_verify_locations(cafile="MyRootCA.crt")
    context.verify_mode = ssl.CERT_REQUIRED
    
    # Session yaxshilash
    context.session_stats
    
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    return httpd

if __name__ == "__main__":
    try:
        httpd = create_secure_server()
        print("="*50)
        print("MTLS XAVFSIZ SERVER ISHGA TUSHDI")
        print("="*50)
        print(f"Manzil: https://localhost:4443")
        print(f"Protokol: TLS 1.2+")
        print(f"Klient autentifikatsiyasi: FAOL")
        print("="*50)
        print("Server to'xtatilmoqda... (Ctrl+C)")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer to'xtatildi.")
    except FileNotFoundError as e:
        print(f"XATOLIK: Sertifikat fayli topilmadi - {e}")
    except Exception as e:
        print(f"XATOLIK: {e}")