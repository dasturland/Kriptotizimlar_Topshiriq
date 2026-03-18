# MLOYIHA: mTLS Xavfsiz Server
## Kriptotizimlar O'quv Loyihasi

---

## 📋 LOYIHA HAQIDA

Ushbu loyiha **Mutual TLS (mTLS)** autentifikatsiya tizimini amalga oshiradi. 
Ikki tomonlama SSL/TLS sertifikatlar orqali xavfsiz ulanishni ta'minlaydi.

### Asosiy Xususiyatlar:
- ✅ **mTLS (Mutual TLS)** - Ikki tomonlama autentifikatsiya
- 🔒 **TLS 1.2/1.3** - Zamonaviy shifrlash protokollari
- 🛡️ **AES-256-GCM** - Yuqori darajadagi himoya
- 📝 **To'liq logging** - Barcha hodisalarni qayd etish
- 🎯 **Optimal konfiguratsiya** - Xavfsizlik va unumdorlik muvozanati

---

## 📁 FAYLLAR TUZILISHI

```
KRIPTOTIZIMLAR/
├── server.py              # Asosiy HTTPS server (mTLS bilan)
├── index.html             # Xavfsiz veb-sahifa
├── test_server.py         # Test skripti
├── README_SECURITY.md     # Xavfsizlik standartlari
│
├── MyRootCA.crt          # Root CA sertifikati
├── MyRootCA.key          # Root CA kaliti
│
├── server.crt            # Server sertifikati
├── server.key            # Server kaliti
├── server.csr            # Server so'rovi
├── server.ext            # Server kengaytmasi
│
└── client.crt            # Klient sertifikati
    client.key            # Klient kaliti
    client.csr            # Klient so'rovi
    client.ext            # Klient kengaytmasi
```

---

## 🚀 ISHGA TUSHIRISH

### 1. Serverni ishga tushirish:

```bash
python server.py
```

Natija:
```
==================================================
MTLS XAVFSIZ SERVER ISHGA TUSHDI
==================================================
Manzil: https://localhost:4443
Protokol: TLS 1.2+
Klient autentifikatsiyasi: FAOL
==================================================
Server to'xtatilmoqda... (Ctrl+C)
```

### 2. Brauzerda ochish:

```
https://localhost:4443
```

**DIQQAT:** Brauzeringizda klient sertifikatini tanlash oynasi chiqadi. 
`client.crt` sertifikatini tanlang.

### 3. Test qilish:

```bash
python test_server.py
```

---

## 🔧 TEXNIK TAFSILOTLAR

### Server Konfiguratsiyasi:
- **Port:** 4443
- **Host:** localhost (127.0.0.1)
- **Protokol:** HTTPS / TLS 1.2+
- **Autentifikatsiya:** mTLS (majburiy)

### Shifrlash (Cipher Suites):
```
ECDHE+AESGCM
ECDHE+CHACHA20
DHE+AESGCM
DHE+CHACHA20
```

### Xavfsizlik Headerlari:
- `Strict-Transport-Security`: max-age=31536000
- `X-Content-Type-Options`: nosniff
- `X-Frame-Options`: DENY
- `X-XSS-Protection`: 1; mode=block

---

## 📖 QANDAY ISHLAYDI?

### mTLS Jarayoni:

1. **Klient ulanadi** → Serverga HTTPS so'rov yuboradi
2. **Server sertifikat ko'rsatadi** → Klient tekshiradi
3. **Klient sertifikat so'raydi** → Server talab qiladi
4. **Klient sertifikat yuboradi** → Server tekshiradi (CA orqali)
5. **Ulanish o'rnatildi** → Xavfsiz sessiya boshlandi

### Sertifikat Zanjiri:
```
MyRootCA (Root)
    ├── server.crt (Server)
    └── client.crt (Klient)
```

---

## 🔍 MUAMMOLARNI HAL QILISH

### 1. "SSL Certificate Error"

**Sabab:** Sertifikatlar noto'g'ri yoki yo'q

**Yechim:**
```bash
# Barcha sertifikatlar mavjudligini tekshiring
dir *.crt
dir *.key
```

### 2. "Connection Refused"

**Sabab:** Server ishga tushmagan

**Yechim:**
```bash
python server.py
```

### 3. "400 Bad Request - No required SSL certificate"

**Sabab:** Klient sertifikati taqdim etilmagan

**Yechim:**
- Brauzerda sertifikatni tanlang
- Yoki test skriptidan foydalaning

---

## 📊 TEST NATIJALARI

Test skripti quyidagilarni tekshiradi:

✓ Sertifikatlar mavjudligi
✓ Server port ochiqligi  
✓ SSL ulanish muvaffaqiyati
✓ Protokol versiyasi (TLS 1.2+)
✓ Shifrlash algoritmi
✓ Sertifikat zanjiri

---

## 🎓 O'RGANILGAN MAVZULAR

1. **SSL/TLS Protokollari**
   - TLS handshake jarayoni
   - Simmetrik va asimmetrik shifrlash
   
2. **Sertifikatlar**
   - X.509 standarti
   - CA (Certificate Authority)
   - Sertifikat zanjiri
   
3. **mTLS Autentifikatsiya**
   - Bir tomonlama vs Ikki tomonlama
   - Klient autentifikatsiyasi
   
4. **Xavfsizlik**
   - Cipher suites
   - Perfect Forward Secrecy
   - Security headers

---

## 📚 QO'SHIMCHA MANBALAR

- [OpenSSL Hujjatlari](https://www.openssl.org/docs/)
- [Mozilla SSL Config Generator](https://ssl-config.mozilla.org/)
- [OWASP TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)

---

## 👨‍💻 MUALLIF

**Loyiha:** Kriptotizimlar O'quv Dasturi
**Sana:** 2026
**Versiya:** 1.0

---

## ⚠️ DIQQAT

Ushbu loyiha **o'quv maqsadlari** uchun yaratilgan.
Production muhitida qo'shimcha xavfsizlik choralarini ko'ring:
- Haqiqiy CA dan sertifikat oling
- Load balancer ishlating
- DDoS himoyasini yoqing
- Muntazam yangilanib turing

---

## 📞 ALOQA

Savollar uchun:
- Fayl: `README_SECURITY.md`
- Test: `test_server.py`

---

**© 2026 Kriptotizimlar Loyihasi. Barcha huquqlar himoyalangan.**
