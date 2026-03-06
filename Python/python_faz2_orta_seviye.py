# ==============================================================================
#
#          🐍 PYTHON FAZ 2 — ORTA SEVİYE
#          Junior Developer seviyesine götüren konular
#
#          İçindekiler:
#          1.  List & Dict Comprehension
#          2.  File I/O (Dosya Okuma/Yazma)
#          3.  Modules & Imports
#          4.  pip & Virtual Environments (açıklama)
#          5.  İleri Fonksiyon Teknikleri
#          6.  Iterators & Generators
#          7.  Decorators
#          8.  Context Managers (with)
#          9.  Regular Expressions
#          10. Custom Exceptions
#          11. FAZ 2 Proje — Kişisel Görev Yöneticisi
#
# ==============================================================================


# ==============================================================================
# 1️⃣  LIST & DICT COMPREHENSION — Kısa ve Güçlü Yazım
# ==============================================================================
# Comprehension nedir?
# Döngüyle liste/dict/set oluşturmayı tek satıra sıkıştırır.
# Daha hızlı çalışır, daha az kod yazar, daha okunabilir olur.
#
# KURAL: Eğer comprehension okumayı zorlaştırıyorsa, normal döngü yaz.
# Amaç: kısa ve NET kod. Kısa ama anlaşılmaz kod değil!
# ==============================================================================

# --- LIST COMPREHENSION ---
# YAPI: [ifade  for  eleman  in  iterable  if  koşul]
#            ↑           ↑                      ↑
#       ne yapılacak  neyi gez              filtre (opsiyonel)

# Normal döngü:
kareler = []
for x in range(1, 6):
    kareler.append(x ** 2)
# [1, 4, 9, 16, 25]

# Aynısı comprehension ile:
kareler = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# --- Filtreleme (if koşulu) ---
ciftler        = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

uzun_kelimeler = [k for k in ["elma", "armut", "karpuz", "kiraz"] if len(k) > 4]
# ["armut", "karpuz", "kiraz"]

pozitifler     = [x for x in [-3, -1, 0, 2, 5, -2, 8] if x > 0]
# [2, 5, 8]

# --- İfade dönüşümü ---
buyuk_harfler = [isim.upper() for isim in ["ali", "veli", "ayşe"]]
# ["ALI", "VELI", "AYŞE"]

temizlenmis   = [s.strip() for s in ["  elma  ", " muz ", "  kiraz"]]
# ["elma", "muz", "kiraz"]

# --- if/else comprehension içinde ---
# YAPI: [true_deger if koşul else false_deger  for eleman in iterable]
# ⚠️ if/else kullanınca koşul ÖNE geçer, sona değil!

etiketler  = ["Çift" if x % 2 == 0 else "Tek" for x in range(6)]
# ["Çift", "Tek", "Çift", "Tek", "Çift", "Tek"]

sonuclar   = [x ** 2 if x > 0 else 0 for x in [-2, -1, 0, 3, 5]]
# [0, 0, 0, 9, 25]

# --- İç içe döngü (nested) ---
# İki liste kombinasyonu:
harfler  = ["a", "b"]
sayilar  = [1, 2, 3]
kombine  = [f"{h}{s}" for h in harfler for s in sayilar]
# ["a1", "a2", "a3", "b1", "b2", "b3"]

# Matris düzleştirme:
matris   = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duzluk   = [eleman for satir in matris for eleman in satir]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# --- DICT COMPREHENSION ---
# YAPI: {anahtar: deger  for  eleman  in  iterable  if  koşul}

# Liste → Dictionary
isimler       = ["Ali", "Veli", "Ayşe"]
isim_uzunluk  = {isim: len(isim) for isim in isimler}
# {"Ali": 3, "Veli": 4, "Ayşe": 4}

# Sayıların kareleri sözlük
kareler_dict  = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtreleme:
notlar        = {"Ali": 85, "Veli": 45, "Ayşe": 92, "Fatma": 38}
gecenler      = {isim: not_ for isim, not_ in notlar.items() if not_ >= 50}
# {"Ali": 85, "Ayşe": 92}

# Key-Value tersine çevirme:
orijinal      = {"a": 1, "b": 2, "c": 3}
tersine       = {v: k for k, v in orijinal.items()}
# {1: "a", 2: "b", 3: "c"}


# --- SET COMPREHENSION ---
# Tekrarsız sonuçlar için
cumle         = "python öğrenmek python ile çok eğlenceli"
benzersiz_kel = {kelime for kelime in cumle.split()}
# {'python', 'öğrenmek', 'ile', 'çok', 'eğlenceli'}  → "python" tekrarı yok!

tek_kareler   = {x ** 2 for x in range(-5, 6)}
# {0, 1, 4, 9, 16, 25}  → set sırasız ve tekrarsız


# --- GENERATOR EXPRESSION ---
# Liste yerine () kullanılır. Hemen hesaplamaz, lazım oldukça üretir.
# Büyük veri setlerinde bellek tasarrufu sağlar.
buyuk_liste  = sum(x ** 2 for x in range(1_000_000))  # tüm listeyi bellekte tutmaz!
# list comprehension: [x**2 for x in range(1_000_000)] → tüm liste belleğe yüklenir
# generator: (x**2 for x in range(1_000_000))         → birer birer üretir


# ==============================================================================
# 2️⃣  FILE I/O — Dosya Okuma ve Yazma
# ==============================================================================
# Gerçek dünya programları veriyi dosyalarda saklar.
# .txt, .csv, .json gibi dosyalar okuyup yazabilirsin.
#
# ALTIN KURAL: Dosyayı her zaman with bloğu içinde aç!
# with bloğu, kod bitince dosyayı OTOMATIK kapatır.
# Elle kapatmayı unutursan veri kaybı veya hata olabilir.
# ==============================================================================

import os
import json
import csv

# --- DOSYAYA YAZMA ---

# "w" modu → write: dosyayı oluşturur veya SIFIRDAN yazar (önceki içerik silinir!)
with open("test_dosyasi.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba, Dünya!\n")
    dosya.write("Python ile dosya işlemleri öğreniyorum.\n")
    dosya.write("Bu üçüncü satır.\n")

# "a" modu → append: dosyanın SONUNA ekler, var olanı silmez
with open("test_dosyasi.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Bu satır eklendi.\n")

# writelines → liste olarak satırları yaz
satirlar = ["Elma\n", "Muz\n", "Kiraz\n"]
with open("meyveler.txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(satirlar)

# --- DOSYADAN OKUMA ---

# .read() → tüm dosyayı tek string olarak okur
with open("test_dosyasi.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

# .readline() → bir satır okur (büyük dosyalar için)
with open("test_dosyasi.txt", "r", encoding="utf-8") as dosya:
    ilk_satir = dosya.readline()    # "Merhaba, Dünya!\n"
    ikinci    = dosya.readline()    # "Python ile..."
    print(ilk_satir.strip())

# .readlines() → tüm satırları liste olarak okur
with open("test_dosyasi.txt", "r", encoding="utf-8") as dosya:
    tum_satirlar = dosya.readlines()  # ["\n" dahil her satır bir eleman]

# For döngüsü ile satır satır okuma (en verimli yol, büyük dosyalar için)
with open("test_dosyasi.txt", "r", encoding="utf-8") as dosya:
    for satir_no, satir in enumerate(dosya, start=1):
        print(f"{satir_no}: {satir.strip()}")

# --- DOSYA MODLARI ---
# "r"  → read:   okuma (varsayılan), dosya yoksa FileNotFoundError
# "w"  → write:  yazma, dosya varsa sıfırlar, yoksa oluşturur
# "a"  → append: sonuna ekleme, dosya yoksa oluşturur
# "x"  → create: yeni dosya oluşturur, varsa FileExistsError
# "r+" → okuma ve yazma
# "b"  → binary mod (resim, ses için) → "rb", "wb"

# --- DOSYA VARLIĞINI KONTROL ETME ---
dosya_yolu = "test_dosyasi.txt"

if os.path.exists(dosya_yolu):
    print(f"{dosya_yolu} dosyası mevcut.")
    print(f"Boyut: {os.path.getsize(dosya_yolu)} byte")
else:
    print("Dosya bulunamadı!")

# --- JSON DOSYALARI ---
# JSON: yapılandırılmış veri saklamak için en yaygın format
# Python dict ↔ JSON birbirine çok benzer

kullanici_verisi = {
    "isim":     "Benn",
    "yas":      25,
    "hobiler":  ["coding", "okuma", "müzik"],
    "adres": {
        "sehir": "İstanbul",
        "ilce":  "Kadıköy"
    }
}

# Python dict → JSON dosyası (json.dump)
with open("kullanici.json", "w", encoding="utf-8") as f:
    json.dump(kullanici_verisi, f, ensure_ascii=False, indent=4)
    # ensure_ascii=False → Türkçe karakterler bozulmaz
    # indent=4          → okunabilir formatlama

# JSON dosyası → Python dict (json.load)
with open("kullanici.json", "r", encoding="utf-8") as f:
    okunan_veri = json.load(f)
    print(okunan_veri["isim"])      # "Benn"
    print(okunan_veri["hobiler"])   # ["coding", "okuma", "müzik"]

# String ↔ JSON (dosya olmadan)
json_string = json.dumps(kullanici_verisi, ensure_ascii=False)  # dict → string
tekrar_dict = json.loads(json_string)                            # string → dict

# --- CSV DOSYALARI ---
# CSV: tablo verisi için (Excel, veritabanı export vb.)

# CSV yazma
ogrenciler = [
    ["isim",  "yas", "not"],
    ["Ali",    20,    85],
    ["Ayşe",   22,    92],
    ["Mehmet", 21,    78],
]

with open("ogrenciler.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(ogrenciler)

# CSV okuma
with open("ogrenciler.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for satir in reader:
        print(satir)

# DictReader → her satırı dict olarak okur
with open("ogrenciler.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for satir in reader:
        print(f"{satir['isim']}: {satir['not']}")

# --- HATA YÖNETİMİ İLE DOSYA OKUMA ---
def dosya_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            return f.read(), None
    except FileNotFoundError:
        return None, f"'{dosya_adi}' dosyası bulunamadı!"
    except PermissionError:
        return None, "Dosyaya erişim izni yok!"
    except Exception as e:
        return None, f"Beklenmedik hata: {e}"

icerik, hata = dosya_oku("olmayan_dosya.txt")
if hata:
    print(f"Hata: {hata}")
else:
    print(icerik)

# Temizlik: test dosyalarını sil
for dosya in ["test_dosyasi.txt", "meyveler.txt", "kullanici.json", "ogrenciler.csv"]:
    if os.path.exists(dosya):
        os.remove(dosya)


# ==============================================================================
# 3️⃣  MODULES & IMPORTS — Modüller ve Kütüphaneler
# ==============================================================================
# Modül nedir?
# Python kodu içeren bir .py dosyası. Başkasının yazdığı (veya senin)
# hazır fonksiyonları import edip kullanabilirsin.
#
# 3 tür modül var:
# 1. Built-in (dahili)  → Python ile birlikte gelir, kurulum gerekmez
# 2. Third-party        → pip install ile kurulur (pandas, requests vb.)
# 3. Kendi yazdıkların  → kendi .py dosyaların
# ==============================================================================

# --- IMPORT YOLLARI ---
import math                       # tüm modülü import et
from math import pi, sqrt         # sadece belirli şeyleri import et
from math import pi as PI         # takma isim (alias) ile import et
from math import *                # hepsini import et (⚠️ tavsiye edilmez!)

# math modülü kullanımı
print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
print(math.ceil(3.2))   # 4   → yukarı yuvarla
print(math.floor(3.8))  # 3   → aşağı yuvarla
print(math.log(100, 10))# 2.0 → log10(100)
print(math.factorial(5))# 120 → 5!
print(math.pow(2, 10))  # 1024.0

# --- DATETIME MODÜLÜ ---
import datetime

simdi    = datetime.datetime.now()
bugun    = datetime.date.today()
saat     = datetime.time(14, 30, 0)      # 14:30:00

print(simdi)                              # 2024-01-15 14:30:45
print(bugun)                              # 2024-01-15
print(simdi.strftime("%d %B %Y, %H:%M")) # "15 January 2024, 14:30"

# Tarih farkı hesaplama
dogum      = datetime.date(2000, 6, 15)
bugunki    = datetime.date.today()
fark       = bugunki - dogum
print(f"Kaç günlük: {fark.days}")
print(f"Yaşınız: {bugunki.year - dogum.year}")

# Tarih aritmetiği
from datetime import timedelta
yarin      = bugunki + timedelta(days=1)
bir_hafta  = bugunki + timedelta(weeks=1)
gecen_ay   = bugunki - timedelta(days=30)
print(f"Yarın: {yarin}")

# --- RANDOM MODÜLÜ ---
import random

print(random.randint(1, 10))           # 1-10 arası rastgele tam sayı
print(random.random())                 # 0.0 ile 1.0 arası float
print(random.uniform(1.5, 9.5))       # belirli aralıkta float
print(random.choice(["elma", "muz"])) # listeden rastgele bir eleman
print(random.choices(range(100), k=5))# k tane rastgele eleman (tekrar olabilir)
print(random.sample(range(100), k=5)) # k tane benzersiz rastgele eleman

liste = [1, 2, 3, 4, 5]
random.shuffle(liste)                  # listeyi yerinde karıştırır
print(liste)

random.seed(42)  # tekrarlanabilir sonuçlar için (test amaçlı)
print(random.randint(1, 100))  # seed ile hep aynı sonuç

# --- OS MODÜLÜ ---
import os

print(os.getcwd())                     # mevcut dizin
print(os.listdir("."))                 # dizin içeriği
print(os.path.exists("dosya.txt"))     # var mı?
print(os.path.join("klasor", "dosya.txt"))  # platform bağımsız yol

os.makedirs("test_klasor", exist_ok=True)  # klasör oluştur (varsa hata verme)
# os.rmdir("test_klasor")                  # boş klasör sil

# Ortam değişkenleri (environment variables)
# os.getenv("HOME")   → kullanıcı home dizini
# os.getenv("PATH")   → sistem PATH'i

# --- SYS MODÜLÜ ---
import sys

print(sys.version)         # Python versiyonu
print(sys.platform)        # işletim sistemi: "linux", "win32", "darwin"
# sys.exit(0)              # programı sonlandır (0 = başarılı)
# sys.argv                 # komut satırı argümanları

# --- COLLECTIONS MODÜLÜ (çok işe yarar!) ---
from collections import Counter, defaultdict, OrderedDict, namedtuple

# Counter → elemanların sayısını say
kelimeler  = ["elma", "muz", "elma", "kiraz", "muz", "elma"]
sayim      = Counter(kelimeler)
print(sayim)                   # Counter({'elma': 3, 'muz': 2, 'kiraz': 1})
print(sayim["elma"])           # 3
print(sayim.most_common(2))    # [('elma', 3), ('muz', 2)] → en çok 2

harf_sayim = Counter("mississippi")
print(harf_sayim)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# defaultdict → eksik key için hata vermez, varsayılan değer üretir
normal_dict    = {}
# normal_dict["yok"]  → KeyError!

dd = defaultdict(list)   # eksik key için boş liste oluşturur
dd["meyveler"].append("elma")
dd["meyveler"].append("muz")
dd["sebzeler"].append("domates")
print(dict(dd))  # {"meyveler": ["elma", "muz"], "sebzeler": ["domates"]}

dd_int = defaultdict(int)   # eksik key için 0 döner
dd_int["a"] += 1
dd_int["a"] += 1
dd_int["b"] += 3
print(dict(dd_int))  # {"a": 2, "b": 3}

# namedtuple → isimli alanlara sahip tuple (hafif class gibi)
Nokta   = namedtuple("Nokta", ["x", "y"])
Kisi    = namedtuple("Kisi", ["isim", "yas", "sehir"])

p       = Nokta(3, 4)
kisi1   = Kisi("Benn", 25, "İstanbul")
print(p.x, p.y)             # 3, 4 (index yerine isimle erişim)
print(kisi1.isim)           # "Benn"
print(kisi1._asdict())      # OrderedDict([('isim', 'Benn')...])

# --- İTERTOOLS MODÜLÜ ---
import itertools

# chain → birden fazla iterable'ı birleştir
birlestir  = list(itertools.chain([1,2,3], [4,5], [6,7,8]))
# [1, 2, 3, 4, 5, 6, 7, 8]

# combinations → kombinasyonlar
kombin     = list(itertools.combinations([1,2,3,4], 2))
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# permutations → permütasyonlar
permu      = list(itertools.permutations([1,2,3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# product → kartezyen çarpım
kart       = list(itertools.product([1,2], ["a","b"]))
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# groupby → gruplama
from itertools import groupby
veriler    = sorted([("A", 1), ("B", 2), ("A", 3), ("B", 4)], key=lambda x: x[0])
for anahtar, grup in groupby(veriler, key=lambda x: x[0]):
    print(f"{anahtar}: {list(grup)}")


# ==============================================================================
# 4️⃣  PIP & VIRTUAL ENVIRONMENTS
# ==============================================================================
# Bu bölüm terminalde çalıştırılır, Python kodu değil!
# Yorum satırı olarak açıklanmıştır.
# ==============================================================================

# --- PIP NEDİR? ---
# pip = Python'un paket yöneticisi. Dışarıdan kütüphane kurar.
# Python kurulunca pip otomatik gelir.

# Terminalde şu komutları kullanırsın:
#
#   pip install paket_adi          → kütüphane kur
#   pip install paket_adi==2.1.0   → belirli versiyon kur
#   pip uninstall paket_adi        → kütüphane sil
#   pip list                       → kurulu kütüphaneleri gör
#   pip show paket_adi             → kütüphane hakkında bilgi
#   pip freeze                     → kurulu paketleri requirements formatında listele
#   pip freeze > requirements.txt  → bağımlılıkları dosyaya kaydet
#   pip install -r requirements.txt → requirements.txt'ten toplu kur

# --- VIRTUAL ENVIRONMENT (SANAL ORTAM) NEDİR? ---
# Problem: Her projen için farklı kütüphane versiyonları lazım.
# Proje A: Django 3.2 kullanıyor
# Proje B: Django 4.2 kullanıyor
# İkisini aynı sisteme kursan çakışır!
#
# Çözüm: Her proje için izole bir Python ortamı (virtual environment) oluştur.
# Her venv kendi paketlerini taşır, birbirini etkilemez.

# Terminalde:
#
#   python -m venv venv            → "venv" adında sanal ortam oluştur
#   source venv/bin/activate       → aktifleştir (Mac/Linux)
#   venv\Scripts\activate          → aktifleştir (Windows)
#   pip install ...                → artık sadece bu ortama kurar
#   deactivate                     → sanal ortamdan çık

# --- EN POPÜLER THIRD-PARTY KÜTÜPHANELER ---
#
#   requests    → HTTP istekleri, API çağrıları        pip install requests
#   pandas      → veri analizi, Excel/CSV işleme       pip install pandas
#   numpy       → sayısal hesaplama, matrisler         pip install numpy
#   flask       → web uygulaması geliştirme            pip install flask
#   django      → büyük web uygulamaları               pip install django
#   fastapi     → modern API geliştirme                pip install fastapi
#   sqlalchemy  → veritabanı ORM                       pip install sqlalchemy
#   pytest      → test yazma                           pip install pytest
#   black       → kod formatlama                       pip install black
#   pillow      → görüntü işleme                       pip install pillow


# ==============================================================================
# 5️⃣  İLERİ FONKSİYON TEKNİKLERİ
# ==============================================================================

# --- HIGHER ORDER FUNCTIONS — Fonksiyon alan/döndüren fonksiyonlar ---
# Python'da fonksiyonlar birinci sınıf nesnelerdir.
# Yani değişkenlere atanabilir, argüman olarak geçilebilir, döndürülebilir.

def carp_iki(x):
    return x * 2

def kare_al(x):
    return x ** 2

# Fonksiyonu değişkene ata
islem = carp_iki
print(islem(5))    # 10 → islem şimdi carp_iki'yi işaret ediyor

# Fonksiyonu argüman olarak geç
def listeye_uygula(liste, fonksiyon):
    return [fonksiyon(eleman) for eleman in liste]

sayilar = [1, 2, 3, 4, 5]
print(listeye_uygula(sayilar, carp_iki))   # [2, 4, 6, 8, 10]
print(listeye_uygula(sayilar, kare_al))    # [1, 4, 9, 16, 25]

# --- MAP, FILTER, REDUCE ---

# map(fonksiyon, iterable) → her elemana fonksiyon uygular
sonuclar = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
# [1, 4, 9, 16, 25]

isimler  = ["ali", "veli", "ayşe"]
buyuk    = list(map(str.upper, isimler))
# ["ALI", "VELI", "AYŞE"]

# filter(fonksiyon, iterable) → True döndürenleri tutar
buyukler = list(filter(lambda x: x > 10, [3, 15, 7, 22, 8, 18]))
# [15, 22, 18]

# reduce → listeyi tek değere indirir
from functools import reduce
toplam   = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
# ((((1+2)+3)+4)+5) = 15

carpim   = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
# 120 → faktöriyel gibi

# --- CLOSURE — Fonksiyon içinde fonksiyon ---
# İç fonksiyon, dış fonksiyonun değişkenlerine erişebilir ve hatırlar!

def carpan_olustur(carpan):
    def carp(sayi):                # iç fonksiyon
        return sayi * carpan       # dış fonksiyonun "carpan" değişkenini hatırlar
    return carp                    # fonksiyonu döndür

uc_kat  = carpan_olustur(3)
bes_kat = carpan_olustur(5)

print(uc_kat(10))    # 30 → 10 * 3
print(bes_kat(10))   # 50 → 10 * 5
print(uc_kat(7))     # 21

# Başka closure örneği
def sayac_olustur(baslangic=0):
    sayi = [baslangic]    # liste kullanıyoruz çünkü int immutable
    def artir(miktar=1):
        sayi[0] += miktar
        return sayi[0]
    def sifirla():
        sayi[0] = baslangic
    return artir, sifirla

artir, sifirla = sayac_olustur(10)
print(artir())    # 11
print(artir(5))   # 16
print(artir())    # 17
sifirla()
print(artir())    # 11


# ==============================================================================
# 6️⃣  ITERATORS & GENERATORS
# ==============================================================================
# Iterator nedir?
# Elemanları tek tek verebilen nesne. next() ile bir sonrakini alırsın.
# for döngüsü aslında arka planda iterator kullanır.
#
# Generator nedir?
# Tüm listeyi bellekte tutmak yerine, elemanları birer birer üreten fonksiyon.
# yield anahtar kelimesi ile çalışır.
# Büyük veri setlerinde bellek tasarrufu = büyük avantaj.
# ==============================================================================

# --- ITERATOR ---
liste     = [1, 2, 3]
iterator  = iter(liste)         # listeyi iterator'a çevir

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator)) → StopIteration hatası! Bitti.

# for döngüsü aslında şunu yapıyor:
# iterator = iter(liste)
# while True:
#     try: eleman = next(iterator)
#     except StopIteration: break
#     ...

# --- GENERATOR FONKSİYONU ---
# return yerine yield kullanır.
# yield → değeri döndürür VE fonksiyonu DONDURUR. Bir sonraki next()'te kaldığı yerden devam eder.

def sayac_generator(baslangic, bitis):
    sayi = baslangic
    while sayi <= bitis:
        yield sayi     # değeri ver, bekle
        sayi += 1

gen = sayac_generator(1, 5)
print(next(gen))   # 1
print(next(gen))   # 2
for x in gen:      # kaldığı yerden devam eder: 3, 4, 5
    print(x)

# Büyük veri örneği — 1 milyar sayı:
def buyuk_aralık(n):
    i = 0
    while i < n:
        yield i       # bellekte sadece 1 sayı tutar!
        i += 1

# Liste olsaydı: [0, 1, 2, ..., 999999999] → gigabytes bellek!
# Generator: birer birer üretir, bellek sorunu yok.

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:           # SONSUZ generator!
        yield a
        a, b = b, a + b

fib  = fibonacci()
ilk_10 = [next(fib) for _ in range(10)]
print(ilk_10)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# --- GENERATOR EXPRESSION ---
# list comprehension gibi ama () ile ve lazy (tembel) çalışır
kare_gen = (x ** 2 for x in range(10))
print(sum(kare_gen))    # 285 → bellekte tek seferde hepsini tutmaz


# ==============================================================================
# 7️⃣  DECORATORS — Dekoratörler
# ==============================================================================
# Decorator nedir?
# Bir fonksiyonu, orijinal kodunu DEĞİŞTİRMEDEN sarıp yeni özellik ekler.
# @ sembolü ile kullanılır.
#
# Gerçek hayat analojisi: Kahve bardağına kılıf takarsın.
# Kahveyi (fonksiyonu) değiştirmezsin, ama onu taşıma şeklini (davranışını) değiştirirsin.
#
# Ne zaman kullanılır?
#   - Loglama (hangi fonksiyon çağrıldı?)
#   - Zamanlama (fonksiyon kaç ms sürdü?)
#   - Yetki kontrolü (giriş yapılmış mı?)
#   - Cache (sonucu kaydet, tekrar hesaplama)
# ==============================================================================

import time
from functools import wraps

# --- TEMEL DECORATOR ---
def log_decorator(fonksiyon):
    @wraps(fonksiyon)            # orijinal fonksiyon adını koru
    def sarici(*args, **kwargs):
        print(f"▶ '{fonksiyon.__name__}' çağrıldı")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"✓ '{fonksiyon.__name__}' bitti")
        return sonuc
    return sarici

@log_decorator
def merhaba_de(isim):
    print(f"Merhaba, {isim}!")

merhaba_de("Benn")
# ▶ 'merhaba_de' çağrıldı
# Merhaba, Benn!
# ✓ 'merhaba_de' bitti

# --- ZAMANLAMA DECORATOR'Ü ---
def zamanlayici(fonksiyon):
    @wraps(fonksiyon)
    def sarici(*args, **kwargs):
        baslangic = time.time()
        sonuc     = fonksiyon(*args, **kwargs)
        sure      = time.time() - baslangic
        print(f"⏱ '{fonksiyon.__name__}' {sure:.4f} saniyede tamamlandı")
        return sonuc
    return sarici

@zamanlayici
def yavas_islem():
    time.sleep(0.1)     # 0.1 saniye bekle (simülasyon)
    return "Bitti!"

print(yavas_islem())
# ⏱ 'yavas_islem' 0.1001 saniyede tamamlandı

# --- BİRDEN FAZLA DECORATOR ---
@zamanlayici
@log_decorator
def hesapla(n):
    return sum(range(n))

print(hesapla(1000))
# Alttan üste uygulanır: önce log_decorator, sonra zamanlayici

# --- CACHE DECORATOR (Memoization) ---
# Python'un hazır cache decorator'ü: functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_hesapla(n):
    if n < 2:
        return n
    return fibonacci_hesapla(n-1) + fibonacci_hesapla(n-2)

# lru_cache olmadan: fibonacci(35) = milyonlarca tekrarlı hesaplama
# lru_cache ile:     sonuçlar cache'lenir, aynı n için tekrar hesaplanmaz!
print(fibonacci_hesapla(35))  # 9227465 — çok hızlı!

# --- ARGÜMAN ALAN DECORATOR ---
def tekrar_et(kac_kez):
    def decorator(fonksiyon):
        @wraps(fonksiyon)
        def sarici(*args, **kwargs):
            for _ in range(kac_kez):
                sonuc = fonksiyon(*args, **kwargs)
            return sonuc
        return sarici
    return decorator

@tekrar_et(3)
def yazdir(mesaj):
    print(mesaj)

yazdir("Merhaba!")   # 3 kez yazdırır


# ==============================================================================
# 8️⃣  CONTEXT MANAGERS — with İfadesi
# ==============================================================================
# with nedir?
# Kaynakları güvenli açıp kapamak için. Dosyalar, veritabanı bağlantıları vb.
# Kod bloğu bitince (hata olsa bile) __exit__ çalışır → temizlik garantilenir.
# ==============================================================================

# --- HAZIR CONTEXT MANAGER: open() ---
# Her zaman with kullan. with olmadan açarsan kapatmayı unutabilirsin!

with open("gecici.txt", "w") as f:
    f.write("test")
# Blok bitince f otomatik kapanır. f.close() yazmak gerekmez!

# --- KENDİ CONTEXT MANAGER'INI YAZMA ---
# __enter__ ve __exit__ metodları ile (OOP konusunda daha detaylı göreceksin)

class ZamanOlcucu:
    def __enter__(self):
        self.baslangic = time.time()
        print("⏱ Zamanlayıcı başladı")
        return self   # with ... as x → x = __enter__'ın döndürdüğü şey

    def __exit__(self, exc_type, exc_val, exc_tb):
        sure = time.time() - self.baslangic
        print(f"⏱ Geçen süre: {sure:.4f} saniye")
        return False  # False → hataları yuturmaz, ilet

with ZamanOlcucu() as z:
    toplam = sum(range(1_000_000))
    print(f"Toplam: {toplam}")
# ⏱ Zamanlayıcı başladı
# Toplam: 499999500000
# ⏱ Geçen süre: 0.0523 saniye

# --- contextlib ile daha kolay ---
from contextlib import contextmanager

@contextmanager
def yonetilen_baglanti(baglanti_adi):
    print(f"🔌 {baglanti_adi} bağlantısı açıldı")
    try:
        yield baglanti_adi   # with bloğuna geçilen değer
    finally:
        print(f"🔌 {baglanti_adi} bağlantısı kapatıldı")

with yonetilen_baglanti("Veritabanı") as baglan:
    print(f"  {baglan} ile işlem yapılıyor...")
# 🔌 Veritabanı bağlantısı açıldı
#   Veritabanı ile işlem yapılıyor...
# 🔌 Veritabanı bağlantısı kapatıldı


# ==============================================================================
# 9️⃣  REGULAR EXPRESSIONS (REGEX) — Düzenli İfadeler
# ==============================================================================
# Regex nedir?
# Metin içinde kalıp (pattern) aramak için kullanılan mini dil.
# E-posta doğrulama, telefon numarası bulma, metin temizleme gibi işlerde kullanılır.
# ==============================================================================

import re

# --- TEMEL PATTERN'LER ---
# .       → herhangi bir karakter (yeni satır hariç)
# \d      → rakam [0-9]
# \D      → rakam olmayan
# \w      → harf, rakam, alt çizgi [a-zA-Z0-9_]
# \W      → \w olmayan
# \s      → boşluk karakteri (space, tab, newline)
# \S      → boşluk olmayan
# ^       → satır başı
# $       → satır sonu
# +       → 1 veya daha fazla
# *       → 0 veya daha fazla
# ?       → 0 veya 1 (opsiyonel)
# {n}     → tam n kez
# {n,m}   → n ile m kez arası
# []      → karakter sınıfı [abc] → a, b veya c
# |       → veya (a|b) → a veya b
# ()      → gruplama

# --- re.search() → Pattern var mı? ---
metin = "Telefon numaram: 0532 123 45 67"
eslesme = re.search(r"\d{4} \d{3} \d{2} \d{2}", metin)
if eslesme:
    print(f"Telefon bulundu: {eslesme.group()}")  # 0532 123 45 67

# --- re.findall() → Tüm eşleşmeleri bul ---
metin2   = "Ali 25 yaşında, Veli 30 yaşında, Ayşe 22 yaşında"
yaslar   = re.findall(r"\d+", metin2)
print(yaslar)   # ['25', '30', '22']

# --- re.sub() → Bul ve değiştir ---
metin3   = "tarih: 2024-01-15"
temiz    = re.sub(r"-", "/", metin3)
print(temiz)   # "tarih: 2024/01/15"

# Fazla boşlukları temizle
kirli    = "merhaba    dünya   python"
temiz2   = re.sub(r"\s+", " ", kirli)
print(temiz2)  # "merhaba dünya python"

# --- E-POSTA DOĞRULAMA ---
def email_gecerli_mi(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print(email_gecerli_mi("benn@example.com"))   # True
print(email_gecerli_mi("gecersiz@"))          # False
print(email_gecerli_mi("@nodomain.com"))      # False

# --- GRUPLAR İLE YAKALAMA ---
tarih_metni  = "Doğum tarihi: 15/06/2000"
eslesme      = re.search(r"(\d{2})/(\d{2})/(\d{4})", tarih_metni)
if eslesme:
    gun, ay, yil = eslesme.groups()
    print(f"Gün: {gun}, Ay: {ay}, Yıl: {yil}")   # Gün: 15, Ay: 06, Yıl: 2000

# --- re.compile() → Pattern'i önceden derle (performans için) ---
# Aynı pattern'i çok kez kullanacaksan derle, her seferinde tekrar parse etmesin
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
emails        = email_pattern.findall("benn@test.com ve ali@example.org adresleri")
print(emails)  # ['benn@test.com', 'ali@example.org']


# ==============================================================================
# 🔟  CUSTOM EXCEPTIONS — Özel Hata Sınıfları
# ==============================================================================
# Neden özel hata?
# Python'un yerleşik hataları (ValueError, TypeError...) genel amaçlıdır.
# Uygulamana özel hatalar yaratırsan:
#   - Hata mesajları daha anlamlı olur
#   - Hangi hatanın nerede oluştuğunu kolayca anlarsın
#   - Hataları ayrı ayrı yakalayabilirsin
# ==============================================================================

# Özel hata sınıfı oluşturmak için Exception'dan miras alırsın (OOP konusu)
class UygulamaHatasi(Exception):
    """Temel uygulama hatası"""
    pass

class DogrulamaHatasi(UygulamaHatasi):
    """Veri doğrulama hataları için"""
    def __init__(self, alan, deger, mesaj):
        self.alan   = alan
        self.deger  = deger
        self.mesaj  = mesaj
        super().__init__(f"'{alan}' alanı geçersiz (değer: {deger}): {mesaj}")

class YetkiHatasi(UygulamaHatasi):
    """Yetki/izin hataları için"""
    def __init__(self, kullanici, islem):
        self.kullanici = kullanici
        self.islem     = islem
        super().__init__(f"'{kullanici}' kullanıcısının '{islem}' yetkisi yok!")

class BulunamadiHatasi(UygulamaHatasi):
    """Kayıt bulunamadı hataları için"""
    def __init__(self, kayit_tipi, kimlik):
        super().__init__(f"{kayit_tipi} bulunamadı: {kimlik}")

# Kullanım
def kullanici_kaydet(kullanici_adi, yas, email):
    if len(kullanici_adi) < 3:
        raise DogrulamaHatasi("kullanici_adi", kullanici_adi, "En az 3 karakter olmalı")
    if not (0 < yas < 120):
        raise DogrulamaHatasi("yas", yas, "0 ile 120 arasında olmalı")
    if "@" not in email:
        raise DogrulamaHatasi("email", email, "Geçerli bir email adresi giriniz")
    return {"kullanici_adi": kullanici_adi, "yas": yas, "email": email}

def kullanici_sil(yapan_kullanici, silinecek):
    yetkili_kullanicilar = ["admin", "superuser"]
    if yapan_kullanici not in yetkili_kullanicilar:
        raise YetkiHatasi(yapan_kullanici, "kullanıcı silme")

# Test et
test_durumlari = [
    ("ab",    25, "test@test.com"),    # kullanıcı adı çok kısa
    ("alice", 200, "test@test.com"),   # geçersiz yaş
    ("alice", 25, "gecersiz-email"),   # geçersiz email
    ("alice", 25, "alice@test.com"),   # geçerli!
]

for kadi, y, mail in test_durumlari:
    try:
        sonuc = kullanici_kaydet(kadi, y, mail)
        print(f"✅ Kaydedildi: {sonuc}")
    except DogrulamaHatasi as e:
        print(f"❌ Doğrulama Hatası [{e.alan}]: {e.mesaj}")
    except UygulamaHatasi as e:
        print(f"❌ Uygulama Hatası: {e}")

try:
    kullanici_sil("normal_kullanici", "alice")
except YetkiHatasi as e:
    print(f"🚫 {e}")


# ==============================================================================
# 🏗️  FAZ 2 PROJE — Görev Yöneticisi (Task Manager)
#     Tüm Faz 2 konularını bir araya getirir
# ==============================================================================

import json
import datetime
import os
from collections import Counter
from functools import lru_cache

# --- ÖZEL HATALAR ---
class GorevHatasi(Exception): pass
class GorevBulunamadiHatasi(GorevHatasi):
    def __init__(self, gorev_id):
        super().__init__(f"Görev bulunamadı: #{gorev_id}")

# --- DECORATOR ---
def islem_logu(fonksiyon):
    @wraps(fonksiyon)
    def sarici(*args, **kwargs):
        zaman = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{zaman}] {fonksiyon.__name__} çağrıldı")
        return fonksiyon(*args, **kwargs)
    return sarici

# --- GÖREV YÖNETİCİSİ SINIFI (OOP önizleme!) ---
class GorevYoneticisi:
    DOSYA = "gorevler.json"

    def __init__(self):
        self.gorevler = self._yukle()
        self._sonraki_id = max((g["id"] for g in self.gorevler), default=0) + 1

    def _yukle(self):
        try:
            with open(self.DOSYA, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _kaydet(self):
        with open(self.DOSYA, "w", encoding="utf-8") as f:
            json.dump(self.gorevler, f, ensure_ascii=False, indent=2)

    @islem_logu
    def gorev_ekle(self, baslik, oncelik="orta", etiketler=None):
        gorev = {
            "id":          self._sonraki_id,
            "baslik":      baslik,
            "tamamlandi":  False,
            "oncelik":     oncelik,
            "etiketler":   etiketler or [],
            "olusturuldu": datetime.datetime.now().isoformat(),
        }
        self.gorevler.append(gorev)
        self._sonraki_id += 1
        self._kaydet()
        return gorev

    @islem_logu
    def gorev_tamamla(self, gorev_id):
        gorev = self._bul(gorev_id)
        gorev["tamamlandi"]     = True
        gorev["tamamlanma_tar"] = datetime.datetime.now().isoformat()
        self._kaydet()

    def _bul(self, gorev_id):
        for gorev in self.gorevler:
            if gorev["id"] == gorev_id:
                return gorev
        raise GorevBulunamadiHatasi(gorev_id)

    def filtrele(self, tamamlandi=None, oncelik=None, etiket=None):
        # Generator expression ile filtrele
        sonuclar = (g for g in self.gorevler)
        if tamamlandi is not None:
            sonuclar = (g for g in sonuclar if g["tamamlandi"] == tamamlandi)
        if oncelik:
            sonuclar = (g for g in sonuclar if g["oncelik"] == oncelik)
        if etiket:
            sonuclar = (g for g in sonuclar if etiket in g["etiketler"])
        return list(sonuclar)

    def istatistik(self):
        toplam       = len(self.gorevler)
        tamamlanan   = sum(1 for g in self.gorevler if g["tamamlandi"])
        bekleyen     = toplam - tamamlanan
        oncelik_say  = Counter(g["oncelik"] for g in self.gorevler)
        tum_etiketler = [e for g in self.gorevler for e in g["etiketler"]]
        etiket_say   = Counter(tum_etiketler)

        return {
            "toplam":       toplam,
            "tamamlanan":   tamamlanan,
            "bekleyen":     bekleyen,
            "oncelikler":   dict(oncelik_say),
            "en_cok_etiket": etiket_say.most_common(3),
        }

    def yazdir(self, gorevler=None):
        gorevler = gorevler or self.gorevler
        print(f"\n{'─'*55}")
        for g in gorevler:
            durum   = "✅" if g["tamamlandi"] else "⬜"
            oncelik = {"yuksek": "🔴", "orta": "🟡", "dusuk": "🟢"}.get(g["oncelik"], "⚪")
            etiket  = f" [{', '.join(g['etiketler'])}]" if g["etiketler"] else ""
            print(f"  {durum} #{g['id']:<3} {oncelik} {g['baslik']}{etiket}")
        print(f"{'─'*55}")


# --- DEMO ---
print("\n" + "="*55)
print("       📋 GÖREV YÖNETİCİSİ")
print("="*55)

ym = GorevYoneticisi()

# Görevler ekle
ym.gorev_ekle("Python Faz 2 bitir",    "yuksek", ["öğrenme", "python"])
ym.gorev_ekle("README yaz",            "orta",   ["dokümantasyon"])
ym.gorev_ekle("Unit testler yaz",      "yuksek", ["test", "python"])
ym.gorev_ekle("Alışveriş yap",         "dusuk",  ["kişisel"])
ym.gorev_ekle("OOP konusunu çalış",    "yuksek", ["öğrenme", "python"])

print("\n📋 Tüm Görevler:")
ym.yazdir()

# Tamamla
try:
    ym.gorev_tamamla(1)
    ym.gorev_tamamla(2)
except GorevBulunamadiHatasi as e:
    print(f"Hata: {e}")

print("\n✅ Tamamlanan Görevler:")
ym.yazdir(ym.filtrele(tamamlandi=True))

print("\n⬜ Bekleyen Yüksek Öncelikli:")
ym.yazdir(ym.filtrele(tamamlandi=False, oncelik="yuksek"))

# İstatistik
stat = ym.istatistik()
print(f"\n📊 İstatistikler:")
print(f"  Toplam    : {stat['toplam']}")
print(f"  Tamamlanan: {stat['tamamlanan']}")
print(f"  Bekleyen  : {stat['bekleyen']}")
print(f"  Öncelikler: {stat['oncelikler']}")
print(f"  Popüler   : {stat['en_cok_etiket']}")

# Temizlik
if os.path.exists(GorevYoneticisi.DOSYA):
    os.remove(GorevYoneticisi.DOSYA)


# ==============================================================================
#  📋 FAZ 2 ÖZET TABLOSU
# ==============================================================================
#
#  KONU                   │  EN ÖNEMLİ KAVRAMLAR
# ────────────────────────┼────────────────────────────────────────────────────
#  Comprehension          │  [x for x in ...] │ {k:v} │ set {} │ generator ()
#  File I/O               │  with open() │ r/w/a modu │ json │ csv
#  Modules                │  import │ from x import y │ datetime/random/os
#  pip & venv             │  pip install │ venv │ requirements.txt
#  Higher Order Functions │  map/filter/reduce │ closure
#  Iterators & Generators │  iter/next │ yield │ lazy evaluation
#  Decorators             │  @decorator │ wraps │ lru_cache │ argümanlı decorator
#  Context Managers       │  with │ __enter__/__exit__ │ @contextmanager
#  Regex                  │  re.search/findall/sub │ pattern'ler │ compile
#  Custom Exceptions      │  Exception subclass │ raise │ anlamlı hata mesajları
# ==============================================================================
