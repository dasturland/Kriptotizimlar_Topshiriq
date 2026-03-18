# mTLS XAVFSIZLIK STANDARTLARI
# ============================

XAVFSIZLIK DARAJASI: MAKSIMAL
PROTOKOL: TLS 1.2+ (TLS 1.3 tavsiya etiladi)

## SHIFRLASH STANDARTLARI

### Ruxsat etilgan shifrlar (Cipher Suites):
- ECDHE+AESGCM (Eng yuqori xavfsizlik)
- ECDHE+CHACHA20 (Mobil qurilmalar uchun optimal)
- DHE+AESGCM (Meros tizimlar uchun)

### Taqiqlangan shifrlar:
- aNULL (Anonim autentifikatsiya)
- MD5 (Zaif xesh algoritmi)
- DSS (Digital Signature Standard - zaif)

## SERTIFIKAT TALABLARI

### Server Sertifikati:
- Minimal kalit uzunligi: 2048 bit (RSA)
- Tavsiya etilgan: 4096 bit yoki ECC P-256
- Amal qilish muddati: 1 yil
- Imzo algoritmi: SHA-256 yoki SHA-384

### Klient Sertifikati (mTLS):
- Majburiy autentifikatsiya
- CA tomonidan imzolangan bo'lishi kerak
- O'z-o'zidan imzolangan sertifikatlar rad etiladi

### Root CA:
- Ishonchli Certificate Authority
- Zanjir tekshiruvi majburiy
- CRL/OCSP tekshiruvi tavsiya etiladi

## PROTOKOL SOZLAMALARI

### Minimal versiya: TLS 1.2
### Tavsiya etilgan versiya: TLS 1.3

### Xavfsizlik boshliqlari (Headers):
- Strict-Transport-Security: max-age=31536000; includeSubDomains
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Content-Security-Policy: default-src 'self'

## PORT KONFIGURATSIYASI

Standart HTTPS portlari:
- 443 - Standart HTTPS
- 4443 - Alternativ HTTPS (ushbu loyiha)
- 8443 - Development HTTPS

## LOGGING VA MONITORING

Qayd etilishi kerak:
- Barcha ulanish urinishlari
- Muvaffaqiyatsiz autentifikatsiya
- SSL/TLS xatoliklari
- Vaqt stampi va IP manzil

## XAVFSIZLIK TEKSHIRUVLARI

Har kuni tekshirish:
✓ Sertifikat amal qilish muddati
✓ Port ochiqligi
✓ Firewall qoidalari

Har oy tekshirish:
✓ Cipher suite konfiguratsiyasi
✓ Protokol versiyalari
✓ Log fayllari tahlili

## FOYDALANISH QOIDALARI

1. Har doim eng so'nggi TLS versiyasidan foydalaning
2. Zaif protokollarni (SSLv2, SSLv3, TLS 1.0, TLS 1.1) o'chiring
3. Perfect Forward Secrecy (PFS) ni yoqing
4. OCSP Stapling ni faollashtiring
5. HSTS ni majburiy qo'llang

## MUAMMOLARNI HAL QILISH

Agar sertifikat xatosi bo'lsa:
1. Sertifikat zanjirini tekshiring
2. CA sertifikatining amal qilish muddatini tekshiring
3. Port va firewall qoidalarini tasdiqlang
4. Klient sertifikatining haqiqiyligini tekshiring

## YORDAM

Hujjatlar:
- OpenSSL dokumentatsiyasi
- Mozilla SSL Configuration Generator
- OWASP TLS Cheat Sheet

Aloqa:
Administrator: admin@example.com
Texnik yordam: support@example.com
