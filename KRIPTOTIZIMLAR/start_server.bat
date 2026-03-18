@echo off
REM mTLS Server Ishga Tushirish Skripti
REM Windows uchun

echo ============================================================
echo MLOYIHA: mTLS XAVFSIZ SERVER
echo ============================================================
echo.

REM Python versiyasini tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo [XATOLIK] Python o'rnatilmagan!
    echo Python 3.7+ versiyasi kerak.
    pause
    exit /b 1
)

echo [OK] Python topildi
echo.

REM Sertifikatlarni tekshirish
echo [TEKSHIRISH] Sertifikatlar...

if not exist "server.crt" (
    echo [XATOLIK] server.crt topilmadi!
    goto :error
)

if not exist "server.key" (
    echo [XATOLIK] server.key topilmadi!
    goto :error
)

if not exist "MyRootCA.crt" (
    echo [XATOLIK] MyRootCA.crt topilmadi!
    goto :error
)

if not exist "client.crt" (
    echo [XATOLIK] client.crt topilmadi!
    goto :error
)

echo [OK] Barcha sertifikatlar mavjud
echo.

REM Port bandligini tekshirish
echo [TEKSHIRISH] Port 4443...
netstat -ano | findstr ":4443" >nul 2>&1
if not errorlevel 1 (
    echo [DIQQAT] Port 4443 allaqachon band!
    echo Boshqa jarayonni to'xtating yoki boshqa port ishlating.
    pause
    exit /b 1
)

echo [OK] Port 4443 bo'sh
echo.

echo ============================================================
echo SERVER ISHGA TUSHIRILMOQDA...
echo ============================================================
echo.
echo Quyidagi manzilda oching:
echo https://localhost:4443
echo.
echo To'xtatish uchun: Ctrl+C
echo ============================================================
echo.

REM Serverni ishga tushirish
python server.py

:error
echo.
echo [XATOLIK] Server ishga tushmadi!
echo Sertifikatlarni qayta yarating.
pause
exit /b 1
