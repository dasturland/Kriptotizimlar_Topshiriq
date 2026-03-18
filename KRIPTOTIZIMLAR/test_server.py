# mTLS Server Test Skripti
# Foydalanish: python test_server.py

import ssl
import socket
import sys
from datetime import datetime

def test_ssl_connection():
    """SSL ulanishini test qilish"""
    print("="*60)
    print("MTLS SERVER TEST")
    print("="*60)
    
    host = 'localhost'
    port = 4443
    
    try:
        # SSL kontekst yaratish
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(cafile="MyRootCA.crt")
        context.load_cert_chain(certfile="client.crt", keyfile="client.key")
        context.check_hostname = False
        context.verify_mode = ssl.CERT_REQUIRED
        
        print(f"\n[TEST] Serverga ulanish: {host}:{port}")
        
        # Socket yaratish va ulanish
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        wrapped_sock = context.wrap_socket(sock, server_hostname=host)
        
        try:
            wrapped_sock.connect((host, port))
            print("[✓] Ulanish muvaffaqiyatli!")
            
            # SSL ma'lumotlarini olish
            cert = wrapped_sock.getpeercert()
            cipher = wrapped_sock.cipher()
            version = wrapped_sock.version()
            
            print(f"\n[SSL MA'LUMOTLAR]")
            print(f"  Protokol versiyasi: {version}")
            print(f"  Shifrlash: {cipher[0]}")
            print(f"  Kalit uzunligi: {cipher[1]} bit")
            
            if cert:
                print(f"  [✓] Server sertifikati tekshirildi")
                subject = dict(x[0] for x in cert['subject'])
                print(f"  Subject: {subject.get('commonName', 'N/A')}")
            
            # HTTP so'rov yuborish
            request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
            wrapped_sock.sendall(request)
            
            response = wrapped_sock.recv(4096)
            if response:
                print(f"\n[HTTP JAVOB]")
                lines = response.decode('utf-8', errors='ignore').split('\r\n')
                print(f"  Status: {lines[0] if lines else 'N/A'}")
                print(f"  [✓] Server javob berdi")
            
            print("\n" + "="*60)
            print("BARCHA TESTLAR MUVAFFAQIYATLI O'TDI!")
            print("="*60)
            
        except ssl.SSLError as e:
            print(f"[✗] SSL XATOLIK: {e}")
            return False
        except Exception as e:
            print(f"[✗] XATOLIK: {e}")
            return False
        finally:
            wrapped_sock.close()
            
    except FileNotFoundError as e:
        print(f"[✗] Sertifikat fayli topilmadi: {e}")
        print("\nSertifikatlarni tekshiring:")
        print("  - MyRootCA.crt")
        print("  - client.crt")
        print("  - client.key")
        return False
    except ConnectionRefusedError:
        print(f"[✗] Ulanish rad etildi. Server ishga tushmaganmi?")
        print("\nServerni ishga tushiring:")
        print("  python server.py")
        return False
    except Exception as e:
        print(f"[✗] Kutilmagan xatolik: {e}")
        return False
    
    return True

def check_certificates():
    """Sertifikatlarni tekshirish"""
    print("\n[SERTIFIKATLARNI TEKSHIRISH]")
    
    import os
    certs = {
        'MyRootCA.crt': 'Root CA',
        'server.crt': 'Server',
        'server.key': 'Server Kalit',
        'client.crt': 'Klient',
        'client.key': 'Klient Kalit'
    }
    
    all_exist = True
    for cert_file, cert_name in certs.items():
        if os.path.exists(cert_file):
            size = os.path.getsize(cert_file)
            print(f"  ✓ {cert_name}: {cert_file} ({size} bytes)")
        else:
            print(f"  ✗ {cert_name}: {cert_file} - TOPILMADI")
            all_exist = False
    
    return all_exist

def check_server_running():
    """Server ishlab turganini tekshirish"""
    print("\n[SERVER HOLATI]")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('localhost', 4443))
        sock.close()
        
        if result == 0:
            print("  ✓ Server port 4443 ochiq")
            return True
        else:
            print("  ✗ Server port 4443 yopiq")
            return False
    except Exception as e:
        print(f"  ✗ Xatolik: {e}")
        return False

if __name__ == "__main__":
    print(f"\nTest sanasi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Sertifikatlarni tekshirish
    certs_ok = check_certificates()
    
    if not certs_ok:
        print("\n[DIQQAT] Ba'zi sertifikatlar yo'q!")
        print("Avval sertifikatlar yarating.")
        sys.exit(1)
    
    # Server holatini tekshirish
    server_running = check_server_running()
    
    if not server_running:
        print("\n[DIQQAT] Server ishga tushmagan!")
        print("Serverni ishga tushiring: python server.py")
        sys.exit(1)
    
    # SSL ulanish testi
    ssl_ok = test_ssl_connection()
    
    sys.exit(0 if ssl_ok else 1)
