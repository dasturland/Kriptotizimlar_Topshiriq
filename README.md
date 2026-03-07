# 🛡️ Kriptotizimlar: TLS Sertifikatlash va Xavfsiz Veb-Tizim

Ushbu loyiha lokal tarmoqda HTTPS xavfsiz aloqa protokoli ostida ishlovchi veb-tizimni joriy etish, shaxsiy Sertifikatlash Markazi (Root CA) ni tashkil qilish va ma'lumotlarni zamonaviy kriptografik algoritmlar bilan himoyalashga bag'ishlangan.

---

## 👨‍🎓 Talaba Ma'lumotlari
* **F.I.SH:** SADULLAYEV Jaxongir M.
* **Guruh:** 172-23
* **Fan:** Kriptotizimlar

---

## 🎯 Loyiha Maqsadi
Loyiha doirasida quyidagi strategik vazifalar amalga oshirildi:

1.  **Lokal Infratuzilma:** Lokal tarmoqda xavfsiz ishlovchi veb-serverni sozlash.
2.  **PKI (Root CA):** Shaxsiy sertifikatlash markazini yaratish va server uchun SSL/TLS sertifikatlarini imzolash.
3.  **Ishonchli Sertifikatlar:** Yaratilgan sertifikatlarni operatsion tizimning **"Trusted Root Certification Authorities"** omboriga integratsiya qilish.
4.  **Autentifikatsiya va RBAC:** Foydalanuvchilarni login/parol va rollar asosida identifikatsiya qilish tizimi.
5.  **Kriptografik Himoya:** * Parollarni **Argon2id** algoritmi yordamida xavfsiz saqlash.
    * Ma'lumotlar almashinuvini **AES-256-GCM** rejimida shifrlash.
    * **TLS 1.3** zamonaviy usulda umumiy kalit hosil qilish.

---

## 🛠 Texnologik Stek

| Vazifa | Amaldagi Texnologiya / Algoritm |
| :--- | :--- |
| **Sertifikatlash** | OpenSSL (X.509 standart) |
| **Shifrlash** | AES-256-GCM (Simmetrik) |
| **Xeshlash** | Argon2id |
| **Protokol** | TLS 1.3 / HTTPS |
| **Kirish Nazorati** | RBAC (Role-Based Access Control) |

---

## 🚀 Jarayonning Bosqichma-bosqich Tavsifi

### 1. Sertifikatlash Jarayoni
O'zimizning **Root CA** markazimizni yaratib, u orqali serverimiz uchun sertifikat so'rovini (CSR) tasdiqladik. Bu brauzerda "Xavfsiz ulanish" (Secure Connection) belgisini ta'minlaydi.


### 2. Tizim Xavfsizligini Ta'minlash
* **Parol xavfsizligi:** Foydalanuvchi parollari oddiy matn ko'rinishida emas, balki Argon2id algoritmi bilan xeshlanadi. Bu parollarni brute-force hujumlaridan himoya qiladi.
* **Ma'lumotlar himoyasi:** Mijoz va server o'rtasidagi har bir paket AES-256-GCM shifrlash usuli bilan himoyalangan.

### 3. Hujjatlashtirish
Barcha bosqichlar, jumladan sertifikat yaratish buyruqlari, tizimga qo'shish va veb-interfeysdagi natijalar skrinshotlar orqali tasdiqlangan.

---

## 📂 Loyiha Strukturasi
```text
├── certs/          # Root CA va Server sertifikatlari
├── src/            # Veb-tizim (Frontend/Backend) kodi
├── docs/           # Loyiha bo'yicha hisobot va skrinshotlar
└── README.md       # Asosiy tanishtiruv fayli
