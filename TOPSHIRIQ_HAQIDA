# 🔐 TLS Sertifikatlash va Lokal Xavfsiz Veb-Tizim

Ushbu loyiha OpenSSL yordamida shaxsiy sertifikatlash markazini (Root CA) yaratish, lokal tarmoqda TLS protokoli orqali xavfsiz aloqani o'rnatish va zamonaviy kriptografik usullar bilan himoyalangan veb-tizimni joriy etishga bag'ishlangan.

---

## 🎯 Loyiha Maqsadi
* **Infratuzilma:** Lokal tarmoq uchun xavfsiz veb-tizim muhitini yaratish.
* **PKI (Public Key Infrastructure):** Shaxsiy Root CA tashkil etish va server/mijoz kalitlarini boshqarish.
* **Xavfsizlik Standartlari:** Parollarni **Argon2id** algoritmi bilan xeshlash va ma'lumotlarni **AES-256-GCM** rejimida shifrlash.
* **Ishonchli Muhit:** Sertifikatlarni operatsion tizimning **Trusted Root** omboriga muvaffaqiyatli integratsiya qilish.

---

## 🛠 Texnik Imkoniyatlar va Algoritmlar

| Komponent | Tavsif |
| :--- | :--- |
| **Sertifikatlash** | OpenSSL (X.509 standartidagi sertifikatlar) |
| **Shifrlash** | AES-256-GCM (Simmetrik shifrlash) |
| **Parol Xavfsizligi** | Argon2id (Zamonaviy va xavfsiz xeshlash) |
| **Identifikatsiya** | Login/Parol + RBAC (Role-Based Access Control) |
| **Protokol** | TLS 1.3 / HTTPS |



---

## 🚀 Amalga oshirish bosqichlari

### 1. Root CA va Sertifikatlarni yaratish
OpenSSL yordamida quyidagi tartibda kalitlar yaratiladi:
1.  **Root CA Key & Certificate:** O'zimizning ishonchli markazimizni yaratish.
2.  **Server CSR (Certificate Signing Request):** Server uchun sertifikat so'rovi.
3.  **Signing:** Root CA yordamida server sertifikatini imzolash.

### 2. Tizim ishonchini ta'minlash
Yaratilgan `rootCA.crt` faylini operatsion tizimga qo'shish jarayoni:
* **Windows:** `certlm.msc` -> Trusted Root Certification Authorities.
* **Linux (Ubuntu):** `/usr/local/share/ca-certificates/` papkasiga nusxalash.

### 3. Veb-tizim Xavfsizligi
* **RBAC:** Foydalanuvchilarga rollar (Admin, User) biriktirish va ruxsatlarni cheklash.
* **Validation:** Parollarni murakkablik darajasi bo'yicha tekshirish (Regex).
* **Data Integrity:** Server va mijoz o'rtasidagi ma'lumotlar almashinuvini AES-256-GCM yordamida himoyalash.

---

## 📂 Loyiha Strukturasi
```text
├── certs/               # Root CA va Server sertifikatlari
├── src/                 # Veb-tizim manba kodi
├── screenshots/         # Jarayon tasvirlangan rasmlar
└── README.md            # Loyiha hujjatnomasi
