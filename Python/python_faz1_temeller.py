# ==============================================================================
#
#          🐍 PYTHON FAZ 1 — TEMELLER
#          Sıfırdan başlayanlar için eksiksiz rehber
#
#          İçindekiler:
#          1. Variables & Data Types
#          2. Conditionals (if / elif / else)
#          3. Loops (for / while)
#          4. Functions
#          5. String Methods
#          6. Error Handling (try / except)
#
# ==============================================================================


# ==============================================================================
# 1️⃣  VARIABLES & DATA TYPES — Değişkenler ve Veri Tipleri
# ==============================================================================
# Değişken nedir?
# Bellekte bir kutu gibi düşün. İçine bir değer koyarsın, ona bir isim verirsin.
# O isimle istediğin zaman o değere ulaşırsın.
#
# Python'da değişken oluştururken tip belirtmene GEREK YOK.
# Python tipi otomatik anlar. Buna "dynamically typed" denir.
# ==============================================================================

# --- 📦 TEMEL VERİ TİPLERİ ---

# INTEGER (int) → Tam sayılar. Nokta içermez.
yas         = 25
dogum_yili  = 1999
sicaklik    = -5         # negatif sayılar da int'tir
nufus       = 8_000_000  # büyük sayılarda _ kullanabilirsin, okunması için (8000000 ile aynı)

# FLOAT → Ondalıklı sayılar. Nokta içerir.
boy       = 1.75
kilo      = 68.5
pi        = 3.14159
sicaklik2 = -2.8

# STRING (str) → Metin. Tırnak içinde yazılır. Tek veya çift tırnak fark etmez.
isim      = "Benn"
sehir     = 'Istanbul'
meslek    = "Software Developer"
bos_metin = ""           # boş string, geçerli

# Çok satırlı string — üç tırnak kullan
aciklama = """
Bu bir
çok satırlı
string örneğidir.
"""

# BOOLEAN (bool) → Sadece True ya da False. (Büyük harfle başlar!)
aktif_mi    = True
deleted_mi  = False
# Boolean aslında arka planda sayıdır: True = 1, False = 0
print(True + True)   # 2
print(True * 5)      # 5

# NONE → "Hiçbir şey yok" demek. Boşluk değil, hiç yokluk.
telefon_numarasi = None  # henüz girilmemiş
sonuc            = None  # henüz hesaplanmamış

# --- type() fonksiyonu → değişkenin tipini öğrenmek için ---
print(type(yas))        # <class 'int'>
print(type(boy))        # <class 'float'>
print(type(isim))       # <class 'str'>
print(type(aktif_mi))   # <class 'bool'>
print(type(None))       # <class 'NoneType'>

# --- TİP DÖNÜŞÜMÜ (Type Casting) ---
# Bir veri tipini başka bir tipe çevirebilirsin.

sayi_str  = "42"             # bu bir string: "42"
sayi_int  = int(sayi_str)    # string → int: 42
sayi_flt  = float(sayi_str)  # string → float: 42.0

fiyat     = 9.99
tam_sayi  = int(fiyat)       # float → int: 9 (ondalık kısmı ATAR, yuvarlamaz!)

sayi      = 100
metin     = str(sayi)        # int → string: "100"

# ⚠️ Dikkat! Her dönüşüm mümkün değildir:
# int("merhaba")  →  ValueError! "merhaba" sayıya çevrilemez.
# int("3.14")     →  ValueError! "3.14" önce float'a çevrilmeli: int(float("3.14"))

# --- DEĞİŞKEN KURALLARI ---
# ✅ Geçerli isimler:
kullanici_adi   = "benn"
_gizli_degisken = "gizli"
sayi2           = 2
SABIT_DEGER     = 100   # büyük harf = sabit olduğunu gösterir (kural değil, gelenek)

# ❌ Geçersiz isimler:
# 2sayi    = 5    → SyntaxError: Rakamla başlayamaz
# kullanici-adi = 5 → SyntaxError: Tire(-) kullanılamaz
# class    = "a"  → SyntaxError: Python'un kendi kelimeleri kullanılamaz

# --- ÇOKLU ATAMA ---
x = y = z = 0      # üçü de 0 oldu
a, b, c = 1, 2, 3  # a=1, b=2, c=3 aynı anda

# Swap (yer değiştirme) — Python'da çok kolay!
a, b = b, a        # a=2, b=1 (tek satırda!)

# --- SABITLER (Constants) ---
# Python'da gerçek sabit yoktur ama büyük harfle yazılan değişkenler
# "bu değiştirilmemeli" anlamına gelir (gelenek)
MAX_DENEME     = 3
PI             = 3.14159
SITE_URL       = "https://example.com"

# --- ARİTMETİK OPERATÖRLER ---
a = 17
b = 5

print(a + b)   # 22  → toplama
print(a - b)   # 12  → çıkarma
print(a * b)   # 85  → çarpma
print(a / b)   # 3.4 → bölme (her zaman float döner!)
print(a // b)  # 3   → tam bölme (floor division, ondalığı atar)
print(a % b)   # 2   → modulo (bölümden kalan)
print(a ** b)  # 1419857 → üs alma (a'nın b'nci kuvveti)
print(2 ** 10) # 1024

# Modulo ne işe yarar? Çift/tek kontrolü!
print(10 % 2)  # 0 → çift
print(7  % 2)  # 1 → tek
print(15 % 3)  # 0 → 3'e tam bölünür

# --- KARŞILAŞTIRMA OPERATÖRLERI ---
# Sonuç her zaman True veya False döner
print(5 == 5)   # True  → eşit mi?
print(5 != 3)   # True  → eşit değil mi?
print(10 > 5)   # True  → büyük mü?
print(10 < 5)   # False → küçük mü?
print(10 >= 10) # True  → büyük veya eşit mi?
print(5  <= 3)  # False → küçük veya eşit mi?

# ⚠️ = ile == farkı:
# =  → atama: x = 5  (x'e 5 değerini ata)
# == → karşılaştırma: x == 5  (x, 5'e eşit mi?)

# --- MANTIKSAL OPERATÖRLER ---
yas   = 20
gelir = 5000

# and → ikisi de True ise True
print(yas >= 18 and gelir >= 3000)   # True and True → True
print(yas >= 18 and gelir >= 10000)  # True and False → False

# or → en az biri True ise True
print(yas >= 18 or gelir >= 10000)   # True or False → True
print(yas < 18  or gelir >= 10000)   # False or False → False

# not → True'yu False'a, False'u True'ya çevirir
print(not True)   # False
print(not False)  # True
print(not (yas < 18))  # not False → True


# ==============================================================================
# 2️⃣  CONDITIONALS — Koşullar (if / elif / else)
# ==============================================================================
# Koşullar: "Eğer şu durum varsa bunu yap, yoksa şunu yap" mantığı.
# Gerçek hayat: Yağmur varsa şemsiye al, yoksa alma.
# ==============================================================================

# --- TEMEL if/elif/else YAPISI ---
not_ortalamasi = 75

if not_ortalamasi >= 90:
    print("Pekiyi")
elif not_ortalamasi >= 75:
    print("İyi")             # Bu çalışır (75 >= 75 True)
elif not_ortalamasi >= 60:
    print("Orta")
elif not_ortalamasi >= 50:
    print("Geçer")
else:
    print("Kaldı")

# --- GİRİNTİ (INDENTATION) ÇOK ÖNEMLİ! ---
# Python'da blokları süslü parantez {} ile değil, girintilerle belirlersin.
# Her if/elif/else bloğunun altındaki kod 4 boşluk içeriden başlamalı!
# ⚠️ Girintisiz yazmak SyntaxError verir!

# --- İÇ İÇE KOŞULLAR (Nested if) ---
yas           = 22
ogrenci_mi    = True
ehliyet_var_mi = True

if yas >= 18:
    print("Reşit")
    if ogrenci_mi:
        print("Öğrenci indirimi var")
        if ehliyet_var_mi:
            print("Araba kiralayabilirsin")
        else:
            print("Araba kiralayamazsın")
    else:
        print("Tam fiyat ödersin")
else:
    print("Reşit değil")

# --- MANTIKSAL OPERATÖRLER İLE KOŞULLAR ---
kullanici_adi = "admin"
sifre         = "1234"

if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı!")
else:
    print("Hatalı kullanıcı adı veya şifre!")

# --- in / not in → Listede var mı kontrolü ---
izin_verilen = ["alice", "bob", "charlie"]
giris_yapan  = "alice"

if giris_yapan in izin_verilen:
    print(f"{giris_yapan} sisteme girebilir.")
else:
    print("Yetkisiz kullanıcı!")

yasak_kelimeler = ["spam", "reklam", "satılık"]
mesaj = "bu bir spam mesajıdır"

if any(kelime in mesaj for kelime in yasak_kelimeler):
    print("Mesaj engellendi!")
else:
    print("Mesaj gönderildi.")

# --- TERNARY OPERATOR (Tek satır if/else) ---
# Kısa koşullar için tek satırda yazabilirsin
# YAPI: [true_değer] if [koşul] else [false_değer]
yas   = 20
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(durum)  # "Reşit"

# Başka örnekler:
sayi          = 7
cift_mi       = "Çift" if sayi % 2 == 0 else "Tek"
max_sayi      = 10 if 10 > 5 else 5

# --- NONE KONTROLÜ ---
veri = None

if veri is None:
    print("Veri henüz girilmemiş")
else:
    print(f"Veri: {veri}")

# ⚠️ None ile karşılaştırma yaparken == değil, is kullan:
# veri == None  → çalışır ama Python bunu tavsiye etmez
# veri is None  → daha doğru ve Pythonic yol

# --- TRUTHY / FALSY DEĞERLER ---
# Python'da bazı değerler if içinde otomatik False sayılır:
# Falsy: False, 0, 0.0, "", [], {}, set(), None
# Truthy: Geri kalan her şey

isim = ""
if isim:
    print("İsim var:", isim)
else:
    print("İsim boş!")  # Bu çalışır

liste = []
if liste:
    print("Listede eleman var")
else:
    print("Liste boş!")  # Bu çalışır


# ==============================================================================
# 3️⃣  LOOPS — Döngüler (for / while)
# ==============================================================================
# Döngü nedir? Aynı işi tekrar tekrar yapmak yerine,
# "şu kadar kez yap" veya "şu koşul devam ettiği sürece yap" diyebilirsin.
#
# for  → Belirli sayıda veya bir listedeki her eleman için dön
# while → Bir koşul True olduğu sürece dön
# ==============================================================================

# --- FOR DÖNGÜSÜ ---

# Bir listedeki her elemanı gez
meyveler = ["elma", "muz", "kiraz", "üzüm"]
for meyve in meyveler:
    print(meyve)

# Bir string'deki her karakteri gez
for harf in "Python":
    print(harf)   # P, y, t, h, o, n (her biri ayrı satırda)

# --- range() FONKSİYONU ---
# range(son)           → 0'dan son-1'e kadar
# range(bas, son)      → bas'tan son-1'e kadar
# range(bas, son, adim) → adım adım

for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

for i in range(0, 20, 5):
    print(i)   # 0, 5, 10, 15

for i in range(10, 0, -1):
    print(i)   # 10, 9, 8, 7... geri sayım!

# --- enumerate() → index ve değer birlikte ---
for index, meyve in enumerate(meyveler):
    print(f"{index + 1}. {meyve}")  # 1. elma, 2. muz...

# --- zip() → iki listeyi paralel gez ---
isimler = ["Ali", "Veli", "Ayşe"]
notlar  = [85, 92, 78]

for isim, not_ in zip(isimler, notlar):
    print(f"{isim}: {not_}")  # Ali: 85, Veli: 92...

# --- Dictionary döngüsü ---
kisi = {"isim": "Benn", "yas": 25, "sehir": "İstanbul"}

for anahtar in kisi:               # sadece key'ler
    print(anahtar)

for deger in kisi.values():        # sadece değerler
    print(deger)

for anahtar, deger in kisi.items():  # ikisi birden
    print(f"{anahtar}: {deger}")

# --- WHILE DÖNGÜSÜ ---
# Koşul True olduğu sürece devam eder.
# Ne zaman kullanılır? Kaç kez döneceğini önceden bilmiyorsanız.

sayac = 0
while sayac < 5:
    print(f"Sayaç: {sayac}")
    sayac += 1   # ⚠️ Bunu unutursan sonsuz döngü!
# Çıktı: Sayaç: 0, 1, 2, 3, 4

# Kullanıcı "çıkış" yazana kadar devam et
# (Gerçek kullanımda input() kullanılır)
girdi = ""
deneme_sayisi = 0
while girdi != "çıkış" and deneme_sayisi < 3:
    # input() genelde burada olur ama simülasyon için:
    deneme_sayisi += 1
    if deneme_sayisi == 3:
        girdi = "çıkış"

# --- BREAK — Döngüyü anında durdur ---
sayilar = [1, 3, 5, 7, 4, 9, 11]
for sayi in sayilar:
    if sayi % 2 == 0:  # çift sayı bulunca dur
        print(f"İlk çift sayı: {sayi}")
        break  # döngüden çık

# --- CONTINUE — O adımı atla, devam et ---
for i in range(10):
    if i % 2 == 0:  # çift sayıları atla
        continue
    print(i)  # sadece tek sayıları yazdırır: 1, 3, 5, 7, 9

# --- ELSE İLE DÖNGÜ (az bilinen ama güçlü özellik) ---
# Döngü NORMAL biterse (break olmadan) else çalışır.
for sayi in [1, 3, 5, 7, 9]:
    if sayi == 4:
        print("4 bulundu!")
        break
else:
    print("4 bulunamadı.")  # Bu çalışır çünkü break tetiklenmedi

# --- İÇ İÇE DÖNGÜLER ---
for i in range(1, 4):      # satırlar: 1, 2, 3
    for j in range(1, 4):  # sütunlar: 1, 2, 3
        print(f"{i}x{j}={i*j}", end="\t")
    print()  # satır sonu

# --- COMPREHENSION ile döngü (kısa yazım) ---
# Normal döngü:
kareler = []
for x in range(1, 6):
    kareler.append(x ** 2)

# Aynı şey tek satırda (list comprehension):
kareler = [x ** 2 for x in range(1, 6)]    # [1, 4, 9, 16, 25]
ciftler = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8...]


# ==============================================================================
# 4️⃣  FUNCTIONS — Fonksiyonlar
# ==============================================================================
# Fonksiyon nedir?
# Tekrar tekrar kullanabileceğin, isimlendirilmiş kod bloğu.
# Bir kez yaz, defalarca kullan.
#
# Gerçek hayat analojisi: Mikrodalga fırın.
# Her ısıtmak istediğinde nasıl ısıtılacağını yeniden öğrenmezsin.
# "Isıt" düğmesine basarsın. Fonksiyon da böyle.
# ==============================================================================

# --- TEMEL FONKSİYON ---
# def anahtar kelimesi ile tanımlanır.
def merhaba_de():
    print("Merhaba, dünya!")

merhaba_de()  # fonksiyonu çağırmak için parantez yaz

# --- PARAMETRELER (Parameters vs Arguments) ---
# Parameter: fonksiyon tanımındaki değişken adı
# Argument:  fonksiyonu çağırırken verdiğin değer

def selamla(isim):            # "isim" = parameter
    print(f"Merhaba, {isim}!")

selamla("Benn")     # "Benn" = argument → Merhaba, Benn!
selamla("Alice")    # "Alice" = argument → Merhaba, Alice!

# --- RETURN → Fonksiyondan değer döndür ---
# print() ekrana yazar ama değeri GERİ VERMez.
# return() hem ekrana yazmaz hem de değeri geri döndürür.
# Döndürülen değeri bir değişkende saklayabilirsin.

def topla(a, b):
    return a + b

sonuc = topla(3, 5)   # sonuc = 8
print(sonuc)          # 8
print(topla(10, 20))  # 30 (direkt print'e verebilirsin)

# ⚠️ return, fonksiyonu ANINDA durdurur. Sonrasındaki kod çalışmaz!
def ilk_cifte_don(sayilar):
    for sayi in sayilar:
        if sayi % 2 == 0:
            return sayi   # bulunca hemen döner
    return None           # bulunamazsa None döner

print(ilk_cifte_don([1, 3, 5, 4, 6]))  # 4

# --- BIRDEN FAZLA DEĞER DÖNDÜRME ---
# Python fonksiyonları birden fazla değer döndürebilir (tuple olarak)
def min_max_bul(sayilar):
    return min(sayilar), max(sayilar)

en_kucuk, en_buyuk = min_max_bul([5, 2, 8, 1, 9])
print(en_kucuk)  # 1
print(en_buyuk)  # 9

# --- DEFAULT PARAMETERS (Varsayılan Parametreler) ---
# Argüman verilmezse kullanılacak değer
def guc_hesapla(taban, us=2):   # us için varsayılan = 2
    return taban ** us

print(guc_hesapla(5))     # 25  (5^2, us belirtilmedi, varsayılan 2 kullanıldı)
print(guc_hesapla(5, 3))  # 125 (5^3)

def yeni_kullanici(isim, rol="kullanıcı", aktif=True):
    return {"isim": isim, "rol": rol, "aktif": aktif}

print(yeni_kullanici("Ali"))                        # rol="kullanıcı", aktif=True
print(yeni_kullanici("Bob", "admin"))               # rol="admin"
print(yeni_kullanici("Carol", aktif=False))         # isim="Carol", rol varsayılan, aktif=False

# ⚠️ Varsayılan parametreler SONDA olmalı!
# def f(a=1, b):  → SyntaxError!
# def f(b, a=1):  → Doğru

# --- KEYWORD ARGUMENTS (İsimli Argümanlar) ---
def profil_olustur(isim, yas, sehir):
    print(f"{isim}, {yas} yaşında, {sehir}'den")

# Pozisyona göre:
profil_olustur("Benn", 25, "İstanbul")

# İsme göre (sıra önemli değil!):
profil_olustur(yas=25, sehir="İstanbul", isim="Benn")

# --- *args → Belirsiz sayıda argüman ---
# Kaç tane argüman geleceğini bilmiyorsun, hepsini tuple olarak alır
def topla_hepsini(*sayilar):
    return sum(sayilar)

print(topla_hepsini(1, 2, 3))         # 6
print(topla_hepsini(1, 2, 3, 4, 5))   # 15
print(topla_hepsini(10))               # 10

# --- **kwargs → Belirsiz sayıda isimli argüman ---
# Key-value çiftlerini dict olarak alır
def kullanici_bilgisi(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"  {anahtar}: {deger}")

kullanici_bilgisi(isim="Benn", yas=25, sehir="İstanbul", meslek="Developer")

# --- SCOPE — Kapsam (Çok önemli kavram!) ---
# Scope = değişkene nereden erişilebileceği
#
# Global scope: Fonksiyon dışında tanımlanan → her yerden görünür
# Local scope:  Fonksiyon içinde tanımlanan → sadece o fonksiyonda görünür

global_degisken = "Ben global'im"  # global

def kapsam_testi():
    local_degisken = "Ben local'im"    # sadece bu fonksiyonda var
    print(global_degisken)             # ✅ global'e erişebilir
    print(local_degisken)              # ✅ local'e erişebilir

kapsam_testi()
print(global_degisken)  # ✅ çalışır
# print(local_degisken) # ❌ NameError! Fonksiyon dışında var olmaz

# global keyword: Fonksiyon içinden global değişkeni değiştirmek için
sayac = 0

def sayaci_artir():
    global sayac   # "global değişkeni kullanacağım" demek
    sayac += 1

sayaci_artir()
sayaci_artir()
print(sayac)  # 2

# ⚠️ global kullanımını mümkün olduğunca azalt. Kodu karmaşıklaştırır.
# Bunun yerine return kullan!

# --- LAMBDA — Anonim Fonksiyonlar ---
# Tek satırlık küçük fonksiyonlar için kullanılır
# YAPI: lambda parametreler: ifade

kare_al  = lambda x: x ** 2
topla    = lambda a, b: a + b
buyuk_mu = lambda x: "Büyük" if x > 10 else "Küçük"

print(kare_al(5))      # 25
print(topla(3, 7))     # 10
print(buyuk_mu(15))    # "Büyük"

# En çok kullanıldığı yer: sort() ile
kisiler = [("Ali", 25), ("Veli", 20), ("Ayşe", 30)]
kisiler.sort(key=lambda kisi: kisi[1])  # yaşa göre sırala
print(kisiler)  # [('Veli', 20), ('Ali', 25), ('Ayşe', 30)]

# --- DOCSTRING — Fonksiyon belgesi ---
# Fonksiyonun ne yaptığını açıklayan metin (üç tırnak içinde)
def daire_alani(yaricap):
    """
    Dairenin alanını hesaplar.
    
    Parametreler:
        yaricap (float): Dairenin yarıçapı
    
    Döndürür:
        float: Dairenin alanı
    """
    return 3.14159 * yaricap ** 2

print(daire_alani(5))         # 78.53975
print(daire_alani.__doc__)    # docstring'i yazdırır


# ==============================================================================
# 5️⃣  STRING METHODS — String Metodları
# ==============================================================================
# String = metin. Python'da en çok kullandığın veri tiplerinden biri.
# Üzerinde onlarca metod var. En önemlilerini öğrenelim.
# ==============================================================================

metin = "  Merhaba, Python Dünyası!  "

# --- TEMİZLEME ---
print(metin.strip())     # "Merhaba, Python Dünyası!"  → her iki yandan boşluk sil
print(metin.lstrip())    # "Merhaba, Python Dünyası!  " → soldan sil
print(metin.rstrip())    # "  Merhaba, Python Dünyası!" → sağdan sil

# --- BÜYÜK/KÜÇÜK HARF ---
s = "hello world"
print(s.upper())        # "HELLO WORLD"
print(s.capitalize())   # "Hello world" → sadece ilk harf büyük
print(s.title())        # "Hello World" → her kelimenin ilk harfi büyük

s2 = "HELLO WORLD"
print(s2.lower())       # "hello world"
print(s2.swapcase())    # "hello world" → büyük→küçük, küçük→büyük

# --- ARAMA ---
cumle = "Python öğrenmek çok eğlenceli, Python harika!"

print(cumle.find("Python"))     # 0    → ilk bulduğu indexi verir, bulamazsa -1
print(cumle.find("Java"))       # -1   → bulunamadı
print(cumle.rfind("Python"))    # 37   → sağdan başlayarak arar (son oluşum)
print(cumle.index("Python"))    # 0    → find gibi ama bulamazsa ValueError!
print(cumle.count("Python"))    # 2    → kaç kez geçiyor?
print(cumle.startswith("Py"))   # True → "Py" ile başlıyor mu?
print(cumle.endswith("ka!"))    # True → "ka!" ile bitiyor mu?
print("Python" in cumle)        # True → içinde var mı? (en sık kullanılan)

# --- DEĞİŞTİRME ---
cumle2 = "elma, muz, kiraz, elma"
print(cumle2.replace("elma", "üzüm"))       # "üzüm, muz, kiraz, üzüm"
print(cumle2.replace("elma", "üzüm", 1))   # "üzüm, muz, kiraz, elma" → sadece 1 kez değiştir

# --- BÖLME (SPLIT) ---
metin2 = "Ali,Veli,Ayşe,Fatma"
liste  = metin2.split(",")        # ["Ali", "Veli", "Ayşe", "Fatma"]
print(liste)

metin3  = "python öğrenmek eğlenceli"
kelimeler = metin3.split()        # boşluğa göre böler: ["python", "öğrenmek", "eğlenceli"]
print(kelimeler)

satirlar = "satir1\nsatir2\nsatir3"
print(satirlar.splitlines())      # ["satir1", "satir2", "satir3"]

# --- BİRLEŞTİRME (JOIN) ---
# split() ile split ettiklerini tekrar birleştirebilirsin
kelimeler2 = ["Python", "çok", "güzel"]
print(" ".join(kelimeler2))      # "Python çok güzel"
print("-".join(kelimeler2))      # "Python-çok-güzel"
print("".join(kelimeler2))       # "Pythonçokgüzel"

# --- FORMAT ---
# f-string (en modern ve önerilen yol)
isim  = "Benn"
yas   = 25
puan  = 98.567

print(f"İsim: {isim}, Yaş: {yas}")          # İsim: Benn, Yaş: 25
print(f"Puan: {puan:.2f}")                   # Puan: 98.57 → 2 ondalık
print(f"Puan: {puan:.0f}")                   # Puan: 99 → yuvarlama
print(f"{'Sol':<15}|")                        # "Sol            |" → sola hizalı, 15 char
print(f"{'Sağ':>15}|")                        # "            Sağ|" → sağa hizalı
print(f"{yas:05d}")                           # "00025" → 5 haneli, başına 0 doldur
print(f"{'=' * 30}")                          # "=============================="
print(f"Hesap: {10 * 20}")                   # İfade hesaplanır: Hesap: 200

# --- KONTROL ---
print("12345".isdigit())     # True  → sadece rakam mı?
print("Hello".isalpha())     # True  → sadece harf mi?
print("Hello5".isalnum())    # True  → harf veya rakam mı?
print("   ".isspace())       # True  → sadece boşluk mu?

# --- DİLİMLEME (Slicing) ---
# Listelerle aynı mantık, stringler için
kelime = "Python"
print(kelime[0])      # "P"
print(kelime[-1])     # "n"
print(kelime[0:3])    # "Pyt"
print(kelime[2:])     # "thon"
print(kelime[:3])     # "Pyt"
print(kelime[::-1])   # "nohtyP" → tersine çevir!


# ==============================================================================
# 6️⃣  ERROR HANDLING — Hata Yönetimi (try / except)
# ==============================================================================
# Hata yönetimi neden önemli?
# Program çalışırken beklenmedik şeyler olabilir:
#   - Kullanıcı yanlış şey girer
#   - Dosya bulunamaz
#   - Sıfıra bölme
#   - Ağ bağlantısı kesilir
#
# Bu hataları yönetmezsen program çöker.
# try/except ile programın çökmesini önleyebilirsin.
# ==============================================================================

# --- TEMEL HATA TİPLERİ ---
# ZeroDivisionError   → sıfıra bölme
# ValueError          → yanlış tip dönüşümü (int("abc"))
# TypeError           → yanlış tip kullanımı (5 + "a")
# IndexError          → liste index sınırı dışı
# KeyError            → dictionary'de olmayan key
# FileNotFoundError   → dosya bulunamadı
# NameError           → tanımlı olmayan değişken kullanımı
# AttributeError      → nesne üzerinde olmayan method

# --- TEMEL try/except ---
try:
    sayi = int("abc")   # bu hata verir!
    print(sayi)
except ValueError:
    print("Geçersiz sayı girdiniz!")   # Bu çalışır

# Program çökmez, devam eder:
print("Program çalışmaya devam ediyor...")

# --- BİRDEN FAZLA HATA YAKALAMAK ---
def bolme_yap(a, b):
    try:
        sonuc = a / b
        return sonuc
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!")
        return None
    except TypeError:
        print("Hata: Sayı girmelisiniz!")
        return None

print(bolme_yap(10, 2))   # 5.0
print(bolme_yap(10, 0))   # "Hata: Sıfıra bölme yapılamaz!" → None
print(bolme_yap(10, "a")) # "Hata: Sayı girmelisiniz!" → None

# --- EXCEPT Exception as e → Hata mesajını görme ---
try:
    liste = [1, 2, 3]
    print(liste[10])      # IndexError!
except IndexError as hata:
    print(f"Hata oluştu: {hata}")   # list index out of range

# --- else → Hata oluşmazsa çalışır ---
try:
    sayi = int("42")
except ValueError:
    print("Dönüştürme hatası!")
else:
    print(f"Başarıyla dönüştürüldü: {sayi}")  # Bu çalışır

# --- finally → Hata olsa da olmasa da MUTLAKA çalışır ---
# Ne zaman kullanılır? Dosya kapatma, bağlantı kesme gibi temizlik işleri için
try:
    dosya_acildi = True
    print("İşlem yapılıyor...")
    # hata_ver()  # Hata olsa bile...
except Exception as e:
    print(f"Hata: {e}")
finally:
    dosya_acildi = False
    print("Temizlik yapıldı!")  # HER DURUMDA çalışır

# --- GERÇEK DÜNYA ÖRNEĞİ: Kullanıcıdan sayı alma ---
def guvenli_sayi_al(metin, min_val=None, max_val=None):
    """Kullanıcıdan güvenli bir şekilde sayı alır."""
    try:
        sayi = float(metin)
        if min_val is not None and sayi < min_val:
            return None, f"Sayı {min_val}'dan küçük olamaz"
        if max_val is not None and sayi > max_val:
            return None, f"Sayı {max_val}'dan büyük olamaz"
        return sayi, None
    except ValueError:
        return None, "Lütfen geçerli bir sayı girin"

sayi, hata = guvenli_sayi_al("25", min_val=0, max_val=100)
if hata:
    print(f"Hata: {hata}")
else:
    print(f"Geçerli sayı: {sayi}")

sayi, hata = guvenli_sayi_al("abc")
if hata:
    print(f"Hata: {hata}")  # Hata: Lütfen geçerli bir sayı girin

# --- RAISE → Kendin hata fırlatmak ---
# Bazen koşullar yanlışsa kendin hata üretmek istersin
def yas_dogrula(yas):
    if not isinstance(yas, int):
        raise TypeError("Yaş bir tam sayı olmalıdır!")
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")
    if yas > 150:
        raise ValueError("Geçersiz yaş değeri!")
    return True

try:
    yas_dogrula(-5)
except ValueError as e:
    print(f"Doğrulama hatası: {e}")  # Yaş negatif olamaz!

try:
    yas_dogrula("otuz")
except TypeError as e:
    print(f"Tip hatası: {e}")   # Yaş bir tam sayı olmalıdır!


# ==============================================================================
# 🏗️  FAZ 1 PROJE — Hepsini Birleştiren Örnek
#     Mini Öğrenci Not Sistemi
# ==============================================================================

import datetime

def not_hesapla(notlar):
    """Verilen notların ortalamasını hesaplar ve harf notu verir."""
    if not notlar:
        return None, None, "Not listesi boş!"
    try:
        ortalama = sum(notlar) / len(notlar)
        if ortalama >= 90:
            harf = "AA"
        elif ortalama >= 80:
            harf = "BA"
        elif ortalama >= 70:
            harf = "BB"
        elif ortalama >= 60:
            harf = "CB"
        elif ortalama >= 50:
            harf = "CC"
        else:
            harf = "FF"
        return ortalama, harf, None
    except TypeError as e:
        return None, None, f"Hata: {e}"


def ogrenci_raporu(ogrenci):
    """Öğrenci sözlüğünden rapor oluşturur."""
    isim    = ogrenci.get("isim", "Bilinmiyor")
    numara  = ogrenci.get("numara", "???")
    notlar  = ogrenci.get("notlar", [])

    ortalama, harf, hata = not_hesapla(notlar)

    print(f"\n{'=' * 40}")
    print(f"  ÖĞRENCİ RAPORU")
    print(f"  Tarih: {datetime.date.today()}")
    print(f"{'=' * 40}")
    print(f"  İsim   : {isim}")
    print(f"  Numara : {numara}")
    print(f"  Notlar : {notlar}")

    if hata:
        print(f"  ⚠️  {hata}")
    else:
        print(f"  Ortalama: {ortalama:.1f}")
        print(f"  Harf Notu: {harf}")
        durum = "✅ GEÇTİ" if ortalama >= 50 else "❌ KALDI"
        print(f"  Durum: {durum}")
    print(f"{'=' * 40}")


# Örnek öğrenciler (tuple → (isim, numara), list → notlar)
ogrenciler = [
    {"isim": "Ali Yılmaz",   "numara": "2021001", "notlar": [85, 90, 78, 92, 88]},
    {"isim": "Ayşe Kaya",    "numara": "2021002", "notlar": [45, 55, 60, 42, 50]},
    {"isim": "Mehmet Demir", "numara": "2021003", "notlar": [95, 98, 100, 97, 99]},
    {"isim": "Zeynep Çelik", "numara": "2021004", "notlar": []},
]

# Tüm öğrencilerin raporunu yazdır
for ogrenci in ogrenciler:
    ogrenci_raporu(ogrenci)

# İstatistikler
tum_ortalamalar = []
for ogrenci in ogrenciler:
    ort, _, hata = not_hesapla(ogrenci["notlar"])
    if not hata:
        tum_ortalamalar.append(ort)

if tum_ortalamalar:
    print(f"\n📊 SINIF İSTATİSTİKLERİ")
    print(f"  En yüksek ortalama : {max(tum_ortalamalar):.1f}")
    print(f"  En düşük ortalama  : {min(tum_ortalamalar):.1f}")
    print(f"  Sınıf ortalaması   : {sum(tum_ortalamalar)/len(tum_ortalamalar):.1f}")
    gecenler = sum(1 for o in tum_ortalamalar if o >= 50)
    print(f"  Geçen öğrenci      : {gecenler}/{len(tum_ortalamalar)}")


# ==============================================================================
#  📋 FAZ 1 ÖZET TABLOSU
# ==============================================================================
#
#  KONU              │  EN ÖNEMLİ KAVRAMLAR
# ───────────────────┼──────────────────────────────────────────────────────────
#  Variables         │  int, float, str, bool, None │ type() │ casting
#  Operators         │  + - * / // % **  │  == != > < and or not
#  Conditionals      │  if / elif / else  │  in  │  is  │  ternary
#  Loops             │  for / while  │  break  │  continue  │  range()
#  Functions         │  def / return  │  *args  │  **kwargs  │  lambda
#  Strings           │  strip/upper/lower  │  split/join  │  replace  │  f-string
#  Error Handling    │  try/except/else/finally  │  raise  │  hata tipleri
# ==============================================================================
