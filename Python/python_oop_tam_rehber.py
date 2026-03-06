# ==============================================================================
#
#   🐍 PYTHON OOP — NESNE TABANLI PROGRAMLAMA
#   Sıfırdan Uzmanlığa Tam Rehber
#
#   ╔══════════════════════════════════════════════════════╗
#   ║  İÇİNDEKİLER                                        ║
#   ║  BÖLÜM 1: OOP Nedir? Neden Var?                     ║
#   ║  BÖLÜM 2: Class ve Object — Temel Kavramlar         ║
#   ║  BÖLÜM 3: __init__ ve Attributes                    ║
#   ║  BÖLÜM 4: Methods — Metodlar                        ║
#   ║  BÖLÜM 5: Encapsulation — Kapsülleme                ║
#   ║  BÖLÜM 6: Properties — @property                    ║
#   ║  BÖLÜM 7: Inheritance — Kalıtım                     ║
#   ║  BÖLÜM 8: Polymorphism — Çok Biçimlilik             ║
#   ║  BÖLÜM 9: Abstraction — Soyutlama                   ║
#   ║  BÖLÜM 10: Magic/Dunder Metodlar                    ║
#   ║  BÖLÜM 11: Composition — Kompozisyon                ║
#   ║  BÖLÜM 12: SOLID Prensipleri                        ║
#   ║  BÖLÜM 13: BÜYÜK PROJE — Banka Sistemi              ║
#   ╚══════════════════════════════════════════════════════╝
#
# ==============================================================================


# ==============================================================================
# BÖLÜM 1: OOP NEDİR? NEDEN VAR? NEDEN KULLANIYORUZ?
# ==============================================================================
#
# ── ÖNCE PROBLEMİ ANLAYALIM ──────────────────────────────────────────────────
#
# Diyelim ki bir banka uygulaması yazıyorsun.
# OOP olmadan (prosedürel programlama ile) şöyle yazarsın:
#
#   hesap1_sahibi  = "Ali"
#   hesap1_bakiye  = 5000
#   hesap1_no      = "TR001"
#
#   hesap2_sahibi  = "Veli"
#   hesap2_bakiye  = 12000
#   hesap2_no      = "TR002"
#
#   def para_yatir(bakiye, miktar):
#       return bakiye + miktar
#
#   def para_cek(bakiye, miktar):
#       if miktar > bakiye:
#           print("Yetersiz bakiye!")
#           return bakiye
#       return bakiye - miktar
#
# 100 hesap olsaydı ne olurdu?
#   hesap1_sahibi, hesap2_sahibi ... hesap100_sahibi → KABUSa döner!
#
# ── OOP'UN GETİRDİĞİ ÇÖZÜM ───────────────────────────────────────────────────
#
# OOP'da sen "Banka Hesabı" adlı bir ŞABLOn (class) oluşturursun.
# Bu şablondan istediğin kadar NESNE (object) üretirsin.
# Her nesne kendi verilerini ve davranışlarını taşır.
#
# Gerçek hayat analojisi:
# 🏗️ Class  = Bina MİMARİ PROJESİ (şablon, tek bir tane var)
# 🏠 Object = O projeden inşa edilen BİNA (sonsuz sayıda olabilir)
#
# Her bina aynı planı paylaşır ama farklı adrese, farklı renge sahip olabilir.
#
# ── OOP'UN 4 TEMEL SÜTUNU ────────────────────────────────────────────────────
#
# 1. ENCAPSULATION  (Kapsülleme)   → Veriyi ve davranışı bir arada tut, dışarıyı koru
# 2. INHERITANCE    (Kalıtım)      → Var olan sınıftan yeni sınıf türet, kodu tekrar kullan
# 3. POLYMORPHISM   (Çok Biçimlilik)→ Farklı nesneler, aynı metod adıyla farklı iş yapsın
# 4. ABSTRACTION    (Soyutlama)    → Karmaşıklığı gizle, basit bir arayüz sun
#
# ── OOP NE ZAMAN KULLANILMALI? ───────────────────────────────────────────────
#
# ✅ Kullan:
#   - Birden fazla "aynı türden nesne" varsa (kullanıcılar, ürünler, hesaplar)
#   - Nesnenin hem verisi hem davranışı varsa
#   - Büyük projeler, takım çalışması
#   - Kodun uzun süre bakımı yapılacaksa
#
# ⚠️ Gerekmeyebilir:
#   - Küçük script'ler, tek kullanımlık araçlar
#   - Sadece veri dönüşümü yapan pipeline'lar
#
# ==============================================================================


# ==============================================================================
# BÖLÜM 2: CLASS VE OBJECT — TEMEL KAVRAMLAR
# ==============================================================================

# ─── EN BASİT CLASS ───────────────────────────────────────────────────────────
# class anahtar kelimesi ile tanımlanır.
# İsimler büyük harfle başlar (PascalCase): BankaHesabi, KullaniciBilgisi

class Araba:
    pass   # "pass" = henüz içi boş, ama geçerli bir class

# ─── OBJECT (NESNE) OLUŞTURMA ─────────────────────────────────────────────────
# Class'ı çağırarak object oluşturursun. Buna "instantiation" denir.
# Oluşturulan objeye "instance" denir.

araba1 = Araba()   # Araba sınıfından bir nesne (instance) oluşturduk
araba2 = Araba()   # Başka bir nesne, tamamen bağımsız!

print(type(araba1))          # <class '__main__.Araba'>
print(isinstance(araba1, Araba))   # True → araba1 bir Araba nesnesi mi?
print(araba1 is araba2)      # False → farklı nesneler, bellekte farklı yerlerde

# ─── DİNAMİK ATTRIBUTE EKLEME ─────────────────────────────────────────────────
# Python'da objeye sonradan attribute (özellik) ekleyebilirsin.
# Ama bu İYİ PRATİK değil! Bunu sadece kavramı anlamak için gösteriyorum.

araba1.renk  = "kırmızı"
araba1.marka = "Toyota"
araba2.renk  = "mavi"
araba2.marka = "BMW"

print(araba1.renk)   # "kırmızı"
print(araba2.marka)  # "BMW"

# araba1.renk ≠ araba2.renk → Her nesne kendi verisine sahip!

# ─── NEDEN DİNAMİK EKLEMEYİ KULLANMIYORUZ? ───────────────────────────────────
# Çünkü:
# 1. Hangi attributeların olduğunu bilmek zorunda kalırsın
# 2. Yazım hatası fark edilmez: araba1.rekn = "kırmızı" (hata görmezsin!)
# 3. Standart yok → kargaşa
# Doğru yol: __init__ metodunu kullan (Bölüm 3)


# ==============================================================================
# BÖLÜM 3: __init__ VE ATTRIBUTES — Başlangıç Metodu
# ==============================================================================
#
# __init__ nedir?
# Constructor (kurucu) metod olarak da bilinir.
# Bir nesne oluşturulduğunda OTOMATIK olarak çağrılır.
# Nesnenin başlangıç durumunu (state) ayarlar.
#
# Neden __ (çift alt çizgi)?
# Python'un özel metodları (magic/dunder methods) __ ile başlar ve biter.
# Bu metodlar Python tarafından otomatik çağrılır, sen çağırmazsın.
#
# self nedir?
# Her instance metodun ilk parametresi self'tir.
# self = "bu nesne" anlamına gelir. Hangi nesneyi işliyorsak o.
# araba1.bilgi_ver() çağırırsın → Python arka planda Araba.bilgi_ver(araba1) yapar!
# Yani self = araba1 olur.
# self ismini değiştirebilirsin (this vb.) ama EVRENSEL GELENEK self'tir.

class BankaHesabi:
    # ── CLASS ATTRIBUTE ──────────────────────────────────────────────────────
    # Tüm nesneler tarafından PAYLAŞILAN değişken.
    # Her hesabın ayrı bakiyesi var ama faiz oranı tüm hesaplar için aynı.
    # Class üzerinde tanımlanır, __init__ içinde değil.

    faiz_orani     = 0.05    # %5 faiz → tüm hesaplar için aynı
    toplam_hesap   = 0       # kaç hesap oluşturuldu → hepsinin paylaştığı sayaç
    PARA_BIRIMI    = "TL"    # sabit değer (büyük harf = değiştirilmemeli)

    # ── __init__ METODU ───────────────────────────────────────────────────────
    # Nesne oluşturulunca ilk çalışan kod.
    # self.xxx = yyy → INSTANCE ATTRIBUTE: bu nesneye özel değişken

    def __init__(self, hesap_no, sahip_isim, baslangic_bakiye=0):
        # ↑ self hariç diğerleri → nesne oluşturulurken verilen argümanlar

        # Instance attributes → her nesneye özel
        self.hesap_no  = hesap_no         # bu nesnenin hesap numarası
        self.sahip     = sahip_isim       # bu nesnenin sahibi
        self.bakiye    = baslangic_bakiye # bu nesnenin bakiyesi
        self.islemler  = []               # bu nesnenin işlem geçmişi (boş liste)
        self.aktif_mi  = True             # hesap aktif mi?

        # Class attribute'u güncelle → tüm nesneler etkilenir
        BankaHesabi.toplam_hesap += 1

        print(f"✅ Hesap oluşturuldu: {self.hesap_no} ({self.sahip})")

    # ── INSTANCE METHOD ───────────────────────────────────────────────────────
    # self parametresi alan metodlar → o nesneye özgü işlemler yapar

    def bakiye_goster(self):
        # self.bakiye → bu nesnenin bakiyesine eriş
        print(f"  {self.sahip} → Bakiye: {self.bakiye:,.2f} {self.PARA_BIRIMI}")

    def para_yatir(self, miktar):
        if miktar <= 0:
            print("  ❌ Yatırılacak miktar 0'dan büyük olmalı!")
            return
        self.bakiye += miktar
        self.islemler.append(f"+{miktar} TL yatırıldı")
        print(f"  ✅ {miktar} TL yatırıldı. Yeni bakiye: {self.bakiye:,.2f} TL")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("  ❌ Çekilecek miktar 0'dan büyük olmalı!")
            return
        if miktar > self.bakiye:
            print(f"  ❌ Yetersiz bakiye! Mevcut: {self.bakiye:,.2f} TL")
            return
        self.bakiye -= miktar
        self.islemler.append(f"-{miktar} TL çekildi")
        print(f"  ✅ {miktar} TL çekildi. Kalan: {self.bakiye:,.2f} TL")

    def gecmis_goster(self):
        print(f"\n  📋 {self.sahip} İşlem Geçmişi:")
        if not self.islemler:
            print("    (Henüz işlem yapılmadı)")
        for i, islem in enumerate(self.islemler, 1):
            print(f"    {i}. {islem}")

    # ── CLASS METHOD ──────────────────────────────────────────────────────────
    # @classmethod decorator'ü kullanılır.
    # İlk parametre self değil cls (class)'tır.
    # Nesneye değil, SINIFA ait işlemler yapar.
    # Ne zaman kullanılır? Sınıfın kendisiyle ilgili bir işlem yapacaksan.
    # Örnek: toplam hesap sayısını göster, faizi değiştir.

    @classmethod
    def toplam_hesap_say(cls):
        # cls = BankaHesabi sınıfının kendisi
        print(f"  🏦 Toplam hesap sayısı: {cls.toplam_hesap}")

    @classmethod
    def faiz_guncelle(cls, yeni_oran):
        eski = cls.faiz_orani
        cls.faiz_orani = yeni_oran
        print(f"  📈 Faiz oranı güncellendi: %{eski*100} → %{yeni_oran*100}")

    @classmethod
    def hesap_olustur_yatirimsiz(cls, hesap_no, sahip):
        # Alternatif constructor: farklı şekillerde nesne oluşturmak için
        # Örneğin: bakiyesiz hesap açmak için özel bir yol
        return cls(hesap_no, sahip, baslangic_bakiye=0)

    # ── STATIC METHOD ─────────────────────────────────────────────────────────
    # @staticmethod decorator'ü kullanılır.
    # Ne self ne de cls parametresi almaz!
    # Sınıfla mantıksal olarak ilgili ama nesneye/sınıfa doğrudan ihtiyaç duymayan işlemler.
    # Ne zaman kullanılır? Yardımcı (helper) fonksiyonlar için.
    # Örnek: iban doğrulama, para birimi dönüştürme

    @staticmethod
    def iban_gecerli_mi(iban):
        # IBAN doğrulama → nesneye/sınıfa ait veri kullanmaz, sadece gelen iban'ı kontrol eder
        iban = iban.replace(" ", "").upper()
        return len(iban) >= 15 and iban[:2].isalpha() and iban[2:].isdigit()

    @staticmethod
    def para_formatla(miktar, para_birimi="TL"):
        return f"{miktar:,.2f} {para_birimi}"


# ─── KULLANIM ─────────────────────────────────────────────────────────────────

print("\n" + "="*55)
print("BÖLÜM 3 DEMO: Instance, Class, Static Methods")
print("="*55)

# Nesne oluşturma → __init__ otomatik çağrılır
h1 = BankaHesabi("TR001", "Ali Yılmaz", 5000)
h2 = BankaHesabi("TR002", "Ayşe Kaya")      # baslangic_bakiye=0 (varsayılan)

# Instance methods
print()
h1.bakiye_goster()      # sadece h1'in bakiyesi
h2.bakiye_goster()      # sadece h2'nin bakiyesi

h1.para_yatir(2000)
h1.para_cek(500)
h1.para_cek(10000)     # yetersiz bakiye
h1.gecmis_goster()

# Class method → sınıf üzerinden çağırılır (nesne üzerinden de çağırılabilir ama kötü pratik)
print()
BankaHesabi.toplam_hesap_say()   # 2 hesap var
BankaHesabi.faiz_guncelle(0.07)

# Static method
print()
print(BankaHesabi.iban_gecerli_mi("TR330006100519786457841326"))  # True
print(BankaHesabi.para_formatla(12345.6))  # "12,345.60 TL"

# CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE farkı:
print(f"\nFaiz (sınıf üzerinden): {BankaHesabi.faiz_orani}")  # 0.07
print(f"Faiz (nesne üzerinden): {h1.faiz_orani}")            # 0.07 → aynı!
# h1.faiz_orani → önce instance'a bakar, bulamazsa sınıfa bakar


# ==============================================================================
# BÖLÜM 4: METHODS — Metodlar Derinlemesine
# ==============================================================================
#
# 3 tür metod:
# 1. Instance Method  → self alır, nesneye özgü veriye erişir
# 2. Class Method     → cls alır, sınıfa ait veriye erişir
# 3. Static Method    → ne self ne cls, bağımsız yardımcı fonksiyon
# ==============================================================================

print("\n" + "="*55)
print("BÖLÜM 4 DEMO: Method Türleri Karşılaştırma")
print("="*55)

class Sicaklik:
    """
    Sıcaklık dönüşümü yapan sınıf.
    3 metod türünü mükemmel örnekler.
    """
    birim_aciklamalari = {
        "C": "Celsius",
        "F": "Fahrenheit",
        "K": "Kelvin"
    }

    def __init__(self, deger, birim="C"):
        self.deger = deger
        self.birim = birim.upper()

    # Instance method → bu nesnenin değerini kullanır (self.deger)
    def celsius_cevir(self):
        if self.birim == "C":
            return self.deger
        elif self.birim == "F":
            return (self.deger - 32) * 5/9
        elif self.birim == "K":
            return self.deger - 273.15

    def fahrenheit_cevir(self):
        celsius = self.celsius_cevir()
        return celsius * 9/5 + 32

    def goster(self):
        c = self.celsius_cevir()
        f = self.fahrenheit_cevir()
        k = c + 273.15
        print(f"  {self.deger}°{self.birim} = {c:.1f}°C = {f:.1f}°F = {k:.1f}K")

    # Class method → alternatif constructor pattern (çok yaygın kullanım!)
    # Farklı birimlerden nesne oluşturmak için
    @classmethod
    def fahrenheit_ile_olustur(cls, fahrenheit):
        return cls(fahrenheit, "F")   # cls = Sicaklik → Sicaklik(fahrenheit, "F")

    @classmethod
    def kelvin_ile_olustur(cls, kelvin):
        return cls(kelvin, "K")

    @classmethod
    def birimleri_listele(cls):
        print("  Desteklenen birimler:")
        for kod, isim in cls.birim_aciklamalari.items():
            print(f"    {kod}: {isim}")

    # Static method → Sicaklik sınıfıyla mantıksal ilgili ama
    # nesneye/sınıfa ait veri kullanmıyor
    @staticmethod
    def insanlar_icin_sicaklik_mi(celsius):
        return -10 <= celsius <= 45

    @staticmethod
    def donma_noktasi_alti_mi(celsius):
        return celsius < 0

# Kullanım
s1 = Sicaklik(100)                              # 100°C
s2 = Sicaklik.fahrenheit_ile_olustur(98.6)      # 98.6°F (vücut ısısı)
s3 = Sicaklik.kelvin_ile_olustur(300)           # 300K

s1.goster()
s2.goster()
s3.goster()

Sicaklik.birimleri_listele()

print(f"\n  25°C insan için uygun mu? {Sicaklik.insanlar_icin_sicaklik_mi(25)}")
print(f"  -5°C donma altında mı? {Sicaklik.donma_noktasi_alti_mi(-5)}")


# ==============================================================================
# BÖLÜM 5: ENCAPSULATION — KAPSÜLLEME
# ==============================================================================
#
# Encapsulation nedir?
# Nesnenin iç verilerini dışarıdan doğrudan erişime KAPATMAK.
# Veriye sadece belirlenmiş metodlar üzerinden erişilmesini sağlamak.
#
# Neden?
# 1. Veri bütünlüğü → Geçersiz değer atanmasını önler
# 2. Değişime kapalılık → İç uygulama değişse bile dışarıya aynı arayüz sunar
# 3. Kontrollü erişim → Kimin ne yapabileceğini belirlersin
#
# Gerçek hayat: ATM makinesi.
# Para hesaplama algoritmasını görmen gerekmez.
# Sadece kartını takarsın, para çekersin. Arayüz sabittir.
#
# Python'da üç seviye "erişim":
# public    → isim         → Her yerden erişilebilir (varsayılan)
# protected → _isim        → Alt sınıflar erişebilir (gelenek, Python zorlamaz)
# private   → __isim       → Sınıf dışından erişilemez (Python name mangling uygular)
# ==============================================================================

print("\n" + "="*55)
print("BÖLÜM 5 DEMO: Encapsulation")
print("="*55)

class Kullanici:
    def __init__(self, kullanici_adi, email, sifre):
        # public → dışarıdan serbestçe okunabilir/değiştirilebilir
        self.kullanici_adi = kullanici_adi

        # protected → alt sınıflar erişebilir, dışarıdan erişim "nezaketsizlik"
        self._email = email
        self._kayit_tarihi = "2024-01-15"

        # private → __çift alt çizgi → Python name mangling uygular
        # Dışarıdan erişilmemeli! Sadece sınıf içinde kullanılır.
        self.__sifre       = self.__sifrele(sifre)
        self.__giris_sayisi = 0
        self.__hesap_kilitli = False

    # private metod → sadece sınıf içinden çağrılır
    def __sifrele(self, sifre):
        # Gerçekte bcrypt kullanılır, burada basit örnek
        return f"HASH_{sifre[::-1].upper()}"   # tersine çevir + büyük harf

    def __giris_basarisiz_say(self):
        self.__giris_sayisi += 1
        if self.__giris_sayisi >= 3:
            self.__hesap_kilitli = True
            print("  🔒 Hesap kilitlendi! (3 başarısız deneme)")

    # public metod → dışarıdan kullanılır, private metodları çağırır
    def giris_yap(self, sifre):
        if self.__hesap_kilitli:
            print("  ❌ Hesap kilitli! Destek ile iletişime geçin.")
            return False

        if self.__sifre == self.__sifrele(sifre):
            self.__giris_sayisi = 0
            print(f"  ✅ Hoş geldin, {self.kullanici_adi}!")
            return True
        else:
            self.__giris_basarisiz_say()
            kalan = 3 - self.__giris_sayisi
            if kalan > 0:
                print(f"  ❌ Hatalı şifre! {kalan} hak kaldı.")
            return False

    def sifre_degistir(self, eski_sifre, yeni_sifre):
        if self.__sifre != self.__sifrele(eski_sifre):
            print("  ❌ Eski şifre hatalı!")
            return False
        if len(yeni_sifre) < 8:
            print("  ❌ Yeni şifre en az 8 karakter olmalı!")
            return False
        self.__sifre = self.__sifrele(yeni_sifre)
        print("  ✅ Şifre güncellendi!")
        return True

    def profil_goster(self):
        print(f"  Kullanıcı : {self.kullanici_adi}")
        print(f"  E-posta   : {self._email}")
        print(f"  Kayıt     : {self._kayit_tarihi}")
        # __sifre ve __giris_sayisi gösterilmiyor → private!

# Test
print()
u = Kullanici("benn_coder", "benn@mail.com", "super123")
u.profil_goster()

print()
u.giris_yap("yanlis")    # ❌
u.giris_yap("yanlis")    # ❌
u.giris_yap("super123")  # ✅

print()
u.sifre_degistir("super123", "yeniSifre99")
u.giris_yap("yeniSifre99")   # ✅

# NAME MANGLING: Python private attribute'u tamamen gizlemez
# _ClassName__attribute şeklinde erişilebilir (ama yapma!)
# print(u._Kullanici__sifre)  → çalışır ama ETİK DEĞİL!
print(f"\n  Name mangling örneği: {u._Kullanici__hesap_kilitli}")
# False → ama bu şekilde erişim NORMAL KULLANIM DEĞİL!


# ==============================================================================
# BÖLÜM 6: PROPERTIES — @property Decorator'ü
# ==============================================================================
#
# Property nedir?
# Method'u attribute gibi kullanmak.
# Doğrudan attribute erişimi gibi görünür ama aslında bir metod çalışır.
#
# Neden kullanılır?
# 1. Attribute okunurken hesaplama yapabilirsin
# 2. Değer atanırken doğrulama yapabilirsin
# 3. Geriye dönük uyumluluk: Önce attribute olarak kullandın,
#    sonra mantık eklemen gerekti. Property ile kodu bozmadan eklersin.
#
# 3 bileşen:
# @property         → getter: değer okunurken çalışır (obj.x)
# @x.setter         → setter: değer atanırken çalışır (obj.x = 5)
# @x.deleter        → deleter: silinirken çalışır (del obj.x)
# ==============================================================================

print("\n" + "="*55)
print("BÖLÜM 6 DEMO: Properties")
print("="*55)

class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        # setter'ları çağırır → doğrulama otomatik çalışır!
        self.genislik   = genislik    # @genislik.setter çağrılır
        self.yukseklik  = yukseklik  # @yukseklik.setter çağrılır

    # GETTER → obj.genislik diyince çalışır
    @property
    def genislik(self):
        return self.__genislik     # private attribute'u döndür

    # SETTER → obj.genislik = 10 diyince çalışır
    @genislik.setter
    def genislik(self, deger):
        if not isinstance(deger, (int, float)):
            raise TypeError("Genişlik sayısal olmalı!")
        if deger <= 0:
            raise ValueError(f"Genişlik 0'dan büyük olmalı! Verilen: {deger}")
        self.__genislik = deger

    @property
    def yukseklik(self):
        return self.__yukseklik

    @yukseklik.setter
    def yukseklik(self, deger):
        if not isinstance(deger, (int, float)):
            raise TypeError("Yükseklik sayısal olmalı!")
        if deger <= 0:
            raise ValueError(f"Yükseklik 0'dan büyük olmalı! Verilen: {deger}")
        self.__yukseklik = deger

    # READ-ONLY property → sadece getter, setter yok
    # alan değiştirilmemeli, her zaman genislik*yukseklik'ten hesaplanır
    @property
    def alan(self):
        return self.__genislik * self.__yukseklik

    @property
    def cevre(self):
        return 2 * (self.__genislik + self.__yukseklik)

    @property
    def kare_mi(self):
        return self.__genislik == self.__yukseklik

    def __repr__(self):
        return f"Dikdortgen({self.genislik}x{self.yukseklik})"


d = Dikdortgen(10, 5)
print(f"\n  {d}")
print(f"  Alan  : {d.alan}")      # metod gibi değil, attribute gibi erişilir!
print(f"  Çevre : {d.cevre}")
print(f"  Kare? : {d.kare_mi}")

d.genislik = 8    # setter çağrılır → doğrulama yapılır
print(f"\n  Genişlik değişti: {d.genislik}")
print(f"  Yeni alan: {d.alan}")   # otomatik güncellendi!

# Hatalı değer atama:
try:
    d.genislik = -5
except ValueError as e:
    print(f"\n  ❌ Hata: {e}")

try:
    d.alan = 100   # read-only property'ye yazmaya çalış
except AttributeError as e:
    print(f"  ❌ Hata: {e}")


# Başka property örneği: Çevre → Sıcaklık
class KisiProfili:
    def __init__(self, ad, soyad, dogum_yili):
        self.ad          = ad
        self.soyad       = soyad
        self.dogum_yili  = dogum_yili

    @property
    def tam_isim(self):
        return f"{self.ad} {self.soyad}"

    @tam_isim.setter
    def tam_isim(self, deger):
        # "Ali Veli" → ad="Ali", soyad="Veli"
        parcalar   = deger.split(" ", 1)
        self.ad    = parcalar[0]
        self.soyad = parcalar[1] if len(parcalar) > 1 else ""

    @property
    def yas(self):
        import datetime
        return datetime.date.today().year - self.dogum_yili

    @property
    def yetiskin_mi(self):
        return self.yas >= 18

k = KisiProfili("Ali", "Yılmaz", 1995)
print(f"\n  Tam isim: {k.tam_isim}")
print(f"  Yaş: {k.yas}")
print(f"  Yetişkin: {k.yetiskin_mi}")

k.tam_isim = "Mehmet Demir"   # setter çalışır
print(f"  Yeni isim: {k.tam_isim}")
print(f"  Ad: {k.ad}, Soyad: {k.soyad}")
# ==============================================================================
#
#   🐍 PYTHON OOP — BÖLÜM 7-13
#   Kalıtım, Polimorfizm, Soyutlama, Magic Metodlar, SOLID, Büyük Proje
#
# ==============================================================================

from abc import ABC, abstractmethod
import datetime
import math


# ==============================================================================
# BÖLÜM 7: INHERITANCE — KALITIM
# ==============================================================================
#
# Kalıtım nedir?
# Var olan bir sınıftan yeni bir sınıf türetmek.
# Türetilen sınıf, üst sınıfın TÜM özelliklerini ve metodlarını alır.
# Üzerine yeni özellikler ekleyebilir veya mevcutları değiştirebilir.
#
# Terminoloji:
# Parent/Base/Super class  → üst sınıf (Hayvan)
# Child/Derived/Sub class  → alt sınıf (Kedi, Köpek)
#
# Neden kullanılır?
# "IS-A" ilişkisi: Kedi bir Hayvandır. → Hayvan sınıfından türet!
# Ortak kod bir yerde, tekrar yazmana gerek yok.
# Bir yerde düzeltirsin, hepsi düzelir.
#
# Gerçek hayat: Şirket çalışanları.
# Tüm çalışanların ortak özellikleri var: isim, maaş, id
# Ama mühendis ≠ satış elemanı → farklı özellikler de var
# Çözüm: Calisan (parent) → Muhendis, SatisElemani, Yonetici (child)
# ==============================================================================

print("="*60)
print("BÖLÜM 7: INHERITANCE — KALITIM")
print("="*60)

# ─── PARENT CLASS ─────────────────────────────────────────────────────────────
class Calisan:
    sirket_adi    = "TechCorp A.Ş."
    calisanlar    = []

    def __init__(self, calisan_id, isim, soyisim, maas, departman):
        self.calisan_id  = calisan_id
        self.isim        = isim
        self.soyisim     = soyisim
        self._maas       = maas        # protected → alt sınıflar erişebilir
        self.departman   = departman
        self.izin_gunu   = 14          # yıllık izin hakkı
        self.ise_giris   = datetime.date.today()

        Calisan.calisanlar.append(self)

    @property
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    @property
    def maas(self):
        return self._maas

    def maas_artir(self, yuzde):
        artis      = self._maas * (yuzde / 100)
        self._maas += artis
        print(f"  💰 {self.tam_isim} maaşı %{yuzde} arttı → {self._maas:,.0f} TL")

    def izin_kullan(self, gun):
        if gun > self.izin_gunu:
            print(f"  ❌ Yetersiz izin bakiyesi! Kalan: {self.izin_gunu} gün")
            return False
        self.izin_gunu -= gun
        print(f"  🏖️ {self.tam_isim} {gun} gün izin kullandı. Kalan: {self.izin_gunu}")
        return True

    def calis(self):
        # Alt sınıflar OVERRIDE eder (geçersiz kılar)
        print(f"  👷 {self.tam_isim} çalışıyor...")

    def bilgi_goster(self):
        print(f"\n  👤 {self.tam_isim} (#{self.calisan_id})")
        print(f"     Departman : {self.departman}")
        print(f"     Maaş      : {self._maas:,.0f} TL")
        print(f"     İzin Hakkı: {self.izin_gunu} gün")

    @classmethod
    def calisan_sayisi(cls):
        return len(cls.calisanlar)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.calisan_id}, '{self.tam_isim}')"


# ─── CHILD CLASS: Muhendis ────────────────────────────────────────────────────
class Muhendis(Calisan):     # Calisan'dan türet → parantez içine yaz
    """
    Calisan'dan türeyen Muhendis sınıfı.
    Calisan'ın HER ŞEYİNİ miras alır + mühendise özel özellikler ekler.
    """
    def __init__(self, calisan_id, isim, soyisim, maas, programlama_dili, seviye="junior"):
        # super() → parent class'ın metodunu çağır
        # Neden super().__init__() kullanıyoruz?
        # Parent'ın __init__'ini tekrar yazmamak için!
        # Ortak başlatma işlemini parent halleder, biz sadece ekstraları ekleriz.
        super().__init__(calisan_id, isim, soyisim, maas, "Mühendislik")

        # Muhendise özel attributes
        self.programlama_dili = programlama_dili
        self.seviye           = seviye   # junior, mid, senior
        self.tamamlanan_proje = 0

    # Yeni metod → sadece Muhendis'te var
    def proje_tamamla(self, proje_adi):
        self.tamamlanan_proje += 1
        print(f"  🎯 {self.tam_isim}: '{proje_adi}' projesi tamamlandı! ({self.tamamlanan_proje}. proje)")

    # OVERRIDE → calis metodunu Muhendis'e göre yeniden yaz
    def calis(self):
        print(f"  💻 {self.tam_isim} ({self.programlama_dili}) kod yazıyor...")

    # bilgi_goster'ı EXTEND et → parent'ınkini çağır + ekstra bilgi ekle
    def bilgi_goster(self):
        super().bilgi_goster()     # parent'ın metodunu çalıştır
        print(f"     Dil       : {self.programlama_dili}")
        print(f"     Seviye    : {self.seviye}")
        print(f"     Projeler  : {self.tamamlanan_proje}")


# ─── CHILD CLASS: SatisElemani ────────────────────────────────────────────────
class SatisElemani(Calisan):
    def __init__(self, calisan_id, isim, soyisim, taban_maas, bolge):
        super().__init__(calisan_id, isim, soyisim, taban_maas, "Satış")
        self.bolge       = bolge
        self.taban_maas  = taban_maas
        self.aylik_satis = 0

    def satis_yap(self, tutar):
        self.aylik_satis += tutar
        komisyon = tutar * 0.05   # %5 komisyon
        self._maas += komisyon
        print(f"  💼 {self.tam_isim}: {tutar:,.0f} TL satış! Komisyon: {komisyon:,.0f} TL")

    def calis(self):
        print(f"  📞 {self.tam_isim} ({self.bolge}) müşteri arıyor...")

    def bilgi_goster(self):
        super().bilgi_goster()
        print(f"     Bölge     : {self.bolge}")
        print(f"     Aylık Sat.: {self.aylik_satis:,.0f} TL")


# ─── CHILD CLASS: Yonetici (Calisan'dan türeyen) ─────────────────────────────
class Yonetici(Calisan):
    def __init__(self, calisan_id, isim, soyisim, maas, ekip_buyuklugu):
        super().__init__(calisan_id, isim, soyisim, maas, "Yönetim")
        self.ekip          = []
        self.maks_ekip     = ekip_buyuklugu

    def calisan_ekle(self, calisan):
        if len(self.ekip) >= self.maks_ekip:
            print(f"  ❌ Ekip kapasitesi dolu! ({self.maks_ekip} kişi)")
            return
        if not isinstance(calisan, Calisan):
            raise TypeError("Sadece Calisan nesnesi eklenebilir!")
        self.ekip.append(calisan)
        print(f"  👥 {calisan.tam_isim} → {self.tam_isim}'ın ekibine eklendi")

    def calis(self):
        print(f"  📊 {self.tam_isim} toplantı yönetiyor... (Ekip: {len(self.ekip)} kişi)")

    def ekip_raporu(self):
        print(f"\n  📋 {self.tam_isim}'ın Ekibi:")
        for c in self.ekip:
            print(f"    - {c}")

    def bilgi_goster(self):
        super().bilgi_goster()
        print(f"     Ekip Büy. : {len(self.ekip)}/{self.maks_ekip}")


# ─── DEMO ─────────────────────────────────────────────────────────────────────
m1 = Muhendis("E001", "Benn", "Yılmaz", 35000, "Python", "senior")
m2 = Muhendis("E002", "Alice", "Demir", 28000, "JavaScript", "mid")
s1 = SatisElemani("S001", "Veli", "Kaya", 20000, "İstanbul")
y1 = Yonetici("M001", "Zeynep", "Arslan", 60000, ekip_buyuklugu=5)

m1.bilgi_goster()
m1.calis()
m1.proje_tamamla("E-ticaret Sistemi")
m1.maas_artir(10)

print()
s1.bilgi_goster()
s1.calis()
s1.satis_yap(50000)

print()
y1.calisan_ekle(m1)
y1.calisan_ekle(m2)
y1.calisan_ekle(s1)
y1.calis()
y1.ekip_raporu()

# isinstance ve issubclass kontrolleri
print(f"\n  m1 bir Calisan mı?  {isinstance(m1, Calisan)}")   # True!
print(f"  m1 bir Muhendis mi? {isinstance(m1, Muhendis)}")   # True
print(f"  m1 bir Yonetici mi? {isinstance(m1, Yonetici)}")   # False
print(f"  Muhendis, Calisan'ın alt sınıfı mı? {issubclass(Muhendis, Calisan)}")  # True

print(f"\n  Toplam çalışan: {Calisan.calisan_sayisi()}")


# ─── ÇOKLU KALITIM (Multiple Inheritance) ─────────────────────────────────────
# Python'da bir sınıf birden fazla sınıftan türeyebilir.
# Dikkatli kullanılmalı → MRO (Method Resolution Order) önemli

class UzakCalisan:
    """Uzaktan çalışma özelliği"""
    def __init__(self):
        self.uzak_calisma = True
        self.zaman_dilimi = "UTC+3"

    def uzaktan_baglan(self):
        print(f"  🌐 VPN'e bağlanıldı ({self.zaman_dilimi})")

class SertifikaliCalisan:
    """Sertifika sahibi çalışanlar için"""
    def __init__(self):
        self.sertifikalar = []

    def sertifika_ekle(self, sertifika):
        self.sertifikalar.append(sertifika)
        print(f"  📜 Sertifika eklendi: {sertifika}")


# Çoklu kalıtım: hem UzakCalisan hem SertifikaliCalisan hem Calisan
class UzmanMuhendis(Muhendis, UzakCalisan, SertifikaliCalisan):
    def __init__(self, calisan_id, isim, soyisim, maas, programlama_dili):
        Muhendis.__init__(self, calisan_id, isim, soyisim, maas, programlama_dili, "senior")
        UzakCalisan.__init__(self)
        SertifikaliCalisan.__init__(self)

    def calis(self):
        self.uzaktan_baglan()
        super().calis()


uzman = UzmanMuhendis("E003", "Can", "Öz", 50000, "Python")
uzman.sertifika_ekle("AWS Solutions Architect")
uzman.sertifika_ekle("Python Professional")
uzman.calis()
print(f"  Sertifikalar: {uzman.sertifikalar}")

# MRO → Python hangi sırayla arar?
print(f"\n  MRO: {[c.__name__ for c in UzmanMuhendis.__mro__]}")


# ==============================================================================
# BÖLÜM 8: POLYMORPHISM — ÇOK BİÇİMLİLİK
# ==============================================================================
#
# Polymorphism nedir?
# "Çok biçimlilik" = aynı arayüz, farklı davranış.
# Farklı sınıfların aynı metod adını farklı şekillerde uygulaması.
#
# Neden güçlü?
# Kod, spesifik tipe değil ARAYÜZE bağlıdır.
# Yeni bir tür eklerken var olan kodu değiştirmezsin!
#
# Gerçek hayat: Müzik aleti.
# "Çal" diyorsun → Gitar teller titreştirir, Davul vurulur, Piyano tuşa basılır.
# Hepsi "Çal" metoduna sahip ama çalma biçimleri farklı.
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 8: POLYMORPHISM — ÇOK BİÇİMLİLİK")
print("="*60)

class Sekil:
    """Tüm şekiller için base class"""
    def __init__(self, renk="siyah"):
        self.renk = renk

    def alan_hesapla(self):
        # Alt sınıflar BU METODU override etmek ZORUNDA
        raise NotImplementedError(f"{self.__class__.__name__} alan_hesapla() metodunu implement etmeli!")

    def cevre_hesapla(self):
        raise NotImplementedError(f"{self.__class__.__name__} cevre_hesapla() metodunu implement etmeli!")

    def bilgi_ver(self):
        print(f"  {self.__class__.__name__} ({self.renk})")
        print(f"    Alan  : {self.alan_hesapla():.2f} birim²")
        print(f"    Çevre : {self.cevre_hesapla():.2f} birim")


class Daire(Sekil):
    def __init__(self, yaricap, renk="siyah"):
        super().__init__(renk)
        self.yaricap = yaricap

    def alan_hesapla(self):     # OVERRIDE
        return math.pi * self.yaricap ** 2

    def cevre_hesapla(self):    # OVERRIDE
        return 2 * math.pi * self.yaricap


class Dikdortgen2(Sekil):
    def __init__(self, genislik, yukseklik, renk="siyah"):
        super().__init__(renk)
        self.genislik   = genislik
        self.yukseklik  = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

    def cevre_hesapla(self):
        return 2 * (self.genislik + self.yukseklik)


class Ucgen(Sekil):
    def __init__(self, a, b, c, renk="siyah"):
        super().__init__(renk)
        self.a = a
        self.b = b
        self.c = c

    def alan_hesapla(self):   # Heron formülü
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def cevre_hesapla(self):
        return self.a + self.b + self.c


# ─── POLİMORFİZMİN GÜCÜ ───────────────────────────────────────────────────────
# Farklı türlerdeki nesneleri aynı şekilde işleyebiliyoruz!
# Yeni bir şekil eklemek → sadece yeni class yaz, var olan kodu değiştirme!

sekiller = [
    Daire(5, "kırmızı"),
    Dikdortgen2(4, 6, "mavi"),
    Ucgen(3, 4, 5, "yeşil"),
    Daire(10),
]

print()
toplam_alan = 0
for sekil in sekiller:
    sekil.bilgi_ver()          # hangi class olduğunu bilmiyoruz, önemli değil!
    toplam_alan += sekil.alan_hesapla()

print(f"\n  Toplam alan: {toplam_alan:.2f} birim²")

# sorted() ile polymorphism
sekiller.sort(key=lambda s: s.alan_hesapla())   # alanlarına göre sırala
print(f"\n  Alana göre sıralı:")
for s in sekiller:
    print(f"    {s.__class__.__name__}: {s.alan_hesapla():.2f}")

# isinstance ile tür bazlı işlem
daireler = [s for s in sekiller if isinstance(s, Daire)]
print(f"\n  Sadece daireler: {daireler}")


# ==============================================================================
# BÖLÜM 9: ABSTRACTION — SOYUTLAMA (ABC)
# ==============================================================================
#
# Abstraction nedir?
# Karmaşıklığı gizleyip basit bir arayüz sunmak.
# Kullanıcı "nasıl çalıştığını" bilmek zorunda değil, "ne yaptığını" bilmesi yeter.
#
# Abstract Class nedir?
# Direkt olarak nesne OLUŞTURULAMAZAN şablon sınıf.
# Alt sınıfların uygulaması gereken metodları tanımlar ama kendisi uygulamaz.
# Bunu "sözleşme" gibi düşün: "Bu sınıftan türeyen herkes şu metodları ZORUNDA yazmak zorunda!"
#
# Ne zaman kullanılır?
# Birden fazla benzer sınıf yazarken ortak arayüzü garanti altına almak için.
# Örnek: Ödeme sistemi → KrediKarti, HavaleEFT, Kripto
# Hepsi "odeme_yap" metodunu uygulamak ZORUNDA ama her biri farklı yapar.
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 9: ABSTRACTION — SOYUTLAMA")
print("="*60)

class OdemeSistemi(ABC):   # ABC'den türetince abstract class olur
    """
    Tüm ödeme sistemleri için sözleşme.
    Bu sınıftan türeyen HER SINIF
    odeme_yap() ve iade_yap() metodlarını ZORUNDA implement etmeli!
    """

    def __init__(self, sahip_adi):
        self.sahip_adi   = sahip_adi
        self.islem_gecmisi = []

    @abstractmethod
    def odeme_yap(self, miktar, aciklama=""):
        """Ödeme yap. Alt sınıf implement etmeli."""
        pass   # body yok!

    @abstractmethod
    def iade_yap(self, miktar, aciklama=""):
        """İade yap. Alt sınıf implement etmeli."""
        pass

    # Concrete method → tüm alt sınıflar kullanabilir, override gerekmez
    def islem_ekle(self, tur, miktar, aciklama):
        self.islem_gecmisi.append({
            "tur"       : tur,
            "miktar"    : miktar,
            "aciklama"  : aciklama,
            "tarih"     : datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        })

    def gecmis_goster(self):
        print(f"\n  📋 {self.sahip_adi} İşlem Geçmişi:")
        for islem in self.islem_gecmisi:
            tur_icon = "💚" if islem["tur"] == "odeme" else "🔄"
            print(f"    {tur_icon} {islem['tarih']} | {islem['miktar']:>8,.2f} TL | {islem['aciklama']}")

    @property
    def odeme_yontemi(self):
        return self.__class__.__name__


class KrediKartiOdeme(OdemeSistemi):
    def __init__(self, sahip_adi, kart_no, son_kullanim):
        super().__init__(sahip_adi)
        self.__kart_no    = kart_no       # private → güvenlik
        self.son_kullanim = son_kullanim
        self.limit        = 10000
        self.borc         = 0

    @property
    def maskelenmiş_kart(self):
        return f"**** **** **** {self.__kart_no[-4:]}"

    def odeme_yap(self, miktar, aciklama=""):   # ABSTRACT METODU implement et
        if miktar > (self.limit - self.borc):
            print(f"  ❌ Limit aşıldı! Kullanılabilir: {self.limit - self.borc:,.2f} TL")
            return False
        self.borc += miktar
        self.islem_ekle("odeme", miktar, aciklama)
        print(f"  💳 {self.maskelenmiş_kart} → {miktar:,.2f} TL ödendi ({aciklama})")
        return True

    def iade_yap(self, miktar, aciklama=""):
        self.borc = max(0, self.borc - miktar)
        self.islem_ekle("iade", miktar, aciklama)
        print(f"  🔄 {miktar:,.2f} TL iade edildi → Kalan borç: {self.borc:,.2f} TL")
        return True


class BankaTransferiOdeme(OdemeSistemi):
    def __init__(self, sahip_adi, iban, bakiye=0):
        super().__init__(sahip_adi)
        self.__iban = iban
        self.bakiye = bakiye

    def odeme_yap(self, miktar, aciklama=""):
        if miktar > self.bakiye:
            print(f"  ❌ Yetersiz bakiye! Mevcut: {self.bakiye:,.2f} TL")
            return False
        self.bakiye -= miktar
        self.islem_ekle("odeme", miktar, aciklama)
        print(f"  🏦 {self.__iban[-6:]}... → {miktar:,.2f} TL gönderildi ({aciklama})")
        return True

    def iade_yap(self, miktar, aciklama=""):
        self.bakiye += miktar
        self.islem_ekle("iade", miktar, aciklama)
        print(f"  🔄 {miktar:,.2f} TL iade alındı → Yeni bakiye: {self.bakiye:,.2f} TL")
        return True


class KriptoOdeme(OdemeSistemi):
    def __init__(self, sahip_adi, cuzdan_adresi, kripto_miktari=0):
        super().__init__(sahip_adi)
        self.cuzdan       = cuzdan_adresi
        self.kripto       = kripto_miktari
        self.btc_kur      = 2_500_000   # 1 BTC = 2.5M TL (örnek)

    def odeme_yap(self, miktar, aciklama=""):
        btc_gerekli = miktar / self.btc_kur
        if btc_gerekli > self.kripto:
            print(f"  ❌ Yetersiz kripto! Gerekli: {btc_gerekli:.8f} BTC")
            return False
        self.kripto -= btc_gerekli
        self.islem_ekle("odeme", miktar, aciklama)
        print(f"  ₿ {btc_gerekli:.8f} BTC → {miktar:,.2f} TL ({aciklama})")
        return True

    def iade_yap(self, miktar, aciklama=""):
        btc_iade = miktar / self.btc_kur
        self.kripto += btc_iade
        self.islem_ekle("iade", miktar, aciklama)
        print(f"  🔄 {btc_iade:.8f} BTC iade edildi")
        return True


# Abstract class'tan direkt nesne oluşturulamaz!
try:
    odeme = OdemeSistemi("Ali")
except TypeError as e:
    print(f"\n  ❌ Abstract class: {e}")

# Kullanım — polimorfizm ile!
print()
odeme1 = KrediKartiOdeme("Benn", "4532123456781234", "12/26")
odeme2 = BankaTransferiOdeme("Ali", "TR33000610051978645784", 50000)
odeme3 = KriptoOdeme("Veli", "1A2B3C4D5E", 0.01)

# Aynı arayüz, farklı davranış → ABSTRACTION + POLYMORPHISM birlikte!
odemeler = [odeme1, odeme2, odeme3]
for odeme in odemeler:
    odeme.odeme_yap(1500, "E-ticaret alışveriş")

print()
odeme2.iade_yap(500, "İptal edilen sipariş")
odeme1.gecmis_goster()


# ==============================================================================
# BÖLÜM 10: MAGIC/DUNDER METODLAR
# ==============================================================================
#
# Magic metodlar nedir?
# __init__, __str__, __len__ gibi __ ile başlayıp biten metodlar.
# Python tarafından özel durumlarda otomatik çağrılır.
# Sen çağırmazsın → Python çağırır.
#
# Neden önemli?
# Kendi sınıflarını Python'un yerleşik davranışlarıyla uyumlu hale getirir.
# Nesnenin +, -, *, ==, <, len(), str(), in gibi operatörlere tepki vermesini sağlar.
#
# Yaygın magic metodlar:
# __init__    → nesne oluşturulunca
# __str__     → str(obj) veya print(obj) çağrılınca
# __repr__    → repr(obj) veya konsol çıktısı
# __len__     → len(obj) çağrılınca
# __eq__      → obj1 == obj2
# __lt__      → obj1 < obj2
# __add__     → obj1 + obj2
# __contains__→ item in obj
# __iter__    → for item in obj
# __getitem__ → obj[index]
# __setitem__ → obj[index] = value
# __call__    → obj() → nesneyi fonksiyon gibi çağır
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 10: MAGIC/DUNDER METODLAR")
print("="*60)

class AlisverisSepetiUrunü:
    def __init__(self, isim, fiyat, adet=1):
        self.isim  = isim
        self.fiyat = fiyat
        self.adet  = adet

    @property
    def toplam(self):
        return self.fiyat * self.adet

    def __str__(self):
        # str(urun) veya print(urun) → kullanıcı dostu çıktı
        return f"{self.isim} x{self.adet} = {self.toplam:.2f} TL"

    def __repr__(self):
        # repr(urun) veya konsol çıktısı → geliştirici dostu, tekrar oluşturulabilir
        return f"AlisverisUrun('{self.isim}', {self.fiyat}, {self.adet})"

    def __eq__(self, other):
        # urun1 == urun2
        if not isinstance(other, AlisverisSepetiUrunü):
            return False
        return self.isim == other.isim

    def __lt__(self, other):
        # urun1 < urun2 → fiyata göre karşılaştır
        return self.toplam < other.toplam

    def __add__(self, other):
        # urun1 + urun2 → toplam fiyat
        if isinstance(other, AlisverisSepetiUrunü):
            return self.toplam + other.toplam
        return self.toplam + other


class AlisverisSepefi:
    def __init__(self, sahip):
        self.sahip  = sahip
        self.__urunler = []

    def ekle(self, urun):
        # Zaten varsa adedi artır
        for mevcut in self.__urunler:
            if mevcut == urun:   # __eq__ çağrılır
                mevcut.adet += urun.adet
                return
        self.__urunler.append(urun)

    def cikar(self, urun_adi):
        self.__urunler = [u for u in self.__urunler if u.isim != urun_adi]

    # __len__ → len(sepet) çağrılınca
    def __len__(self):
        return len(self.__urunler)

    # __str__ → print(sepet) çağrılınca
    def __str__(self):
        if not self.__urunler:
            return f"🛒 {self.sahip}'ın sepeti boş"
        satirlar = [f"🛒 {self.sahip}'ın Sepeti:"]
        for u in self.__urunler:
            satirlar.append(f"    {u}")   # u.__str__() çağrılır
        satirlar.append(f"  {'─'*30}")
        satirlar.append(f"  TOPLAM: {self.toplam:.2f} TL")
        return "\n".join(satirlar)

    # __contains__ → "laptop" in sepet
    def __contains__(self, urun_adi):
        return any(u.isim == urun_adi for u in self.__urunler)

    # __iter__ → for urun in sepet
    def __iter__(self):
        return iter(self.__urunler)

    # __getitem__ → sepet[0]
    def __getitem__(self, index):
        return self.__urunler[index]

    @property
    def toplam(self):
        return sum(u.toplam for u in self.__urunler)

    # __call__ → sepet() → nesneyi fonksiyon gibi çağır
    def __call__(self, indirim_yuzde):
        indirim = self.toplam * (indirim_yuzde / 100)
        print(f"  🏷️ %{indirim_yuzde} indirim: -{indirim:.2f} TL → Net: {self.toplam - indirim:.2f} TL")
        return self.toplam - indirim


# Demo
laptop   = AlisverisSepetiUrunü("Laptop",  25000, 1)
fare     = AlisverisSepetiUrunü("Mouse",    500,  2)
klavye   = AlisverisSepetiUrunü("Klavye",   800,  1)

print(f"\n  {laptop}")      # __str__
print(f"  {repr(laptop)}")  # __repr__
print(f"  Laptop + Mouse: {laptop + fare:.2f} TL")  # __add__

sepet = AlisverisSepefi("Benn")
sepet.ekle(laptop)
sepet.ekle(fare)
sepet.ekle(klavye)

print(f"\n{sepet}")                          # __str__
print(f"\n  Sepette {len(sepet)} ürün")      # __len__
print(f"  'Mouse' sepette mi? {'Mouse' in sepet}")  # __contains__

print(f"\n  Ürünler (for döngüsü):")
for urun in sepet:                           # __iter__
    print(f"    {urun.isim}: {urun.fiyat} TL")

print(f"\n  İlk ürün: {sepet[0].isim}")      # __getitem__

# Fiyata göre sırala → __lt__ kullanılır
sirali = sorted(sepet)
print(f"\n  Fiyata göre sıralı:")
for u in sirali:
    print(f"    {u}")

sepet(15)   # __call__ → %15 indirim uygula


# ==============================================================================
# BÖLÜM 11: COMPOSITION — KOMPOZİSYON
# ==============================================================================
#
# Composition nedir?
# "HAS-A" ilişkisi: Araba bir motora sahiptir.
# Kalıtım "IS-A" iken kompozisyon "HAS-A"dır.
#
# Ne zaman kalıtım, ne zaman kompozisyon?
# "IS-A" → Kedi bir Hayvandır → Kalıtım
# "HAS-A" → Araba bir motora sahiptir → Kompozisyon
#
# Kural: "Composition over Inheritance"
# Mümkün olduğunca kalıtım yerine kompozisyon kullan.
# Daha esnek, daha az bağımlı kod üretir.
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 11: COMPOSITION — KOMPOZİSYON")
print("="*60)

class Motor:
    def __init__(self, hacim, beygir, yakit_tipi="benzin"):
        self.hacim      = hacim
        self.beygir     = beygir
        self.yakit_tipi = yakit_tipi
        self.__calisiyor = False

    def calistir(self):
        if self.__calisiyor:
            print("  ⚙️ Motor zaten çalışıyor.")
            return
        self.__calisiyor = True
        print(f"  ⚙️ Motor çalıştı ({self.hacim}L, {self.beygir}hp, {self.yakit_tipi})")

    def durdur(self):
        self.__calisiyor = False
        print("  ⚙️ Motor durduruldu.")

    @property
    def calisiyor_mu(self):
        return self.__calisiyor

    def __str__(self):
        return f"Motor({self.hacim}L, {self.beygir}hp)"


class Vites:
    def __init__(self, tip="manuel"):
        self.tip         = tip
        self.mevcut_vites = 0

    def vites_yukari(self):
        if self.mevcut_vites < 6:
            self.mevcut_vites += 1
            print(f"  🔄 Vites: {self.mevcut_vites}")

    def vites_asagi(self):
        if self.mevcut_vites > 0:
            self.mevcut_vites -= 1
            print(f"  🔄 Vites: {self.mevcut_vites}")


class Araba:
    def __init__(self, marka, model, yil, motor_hacim, motor_beygir):
        self.marka  = marka
        self.model  = model
        self.yil    = yil
        self.hiz    = 0

        # HAS-A → Araba bir Motora SAHİPTİR
        self.motor  = Motor(motor_hacim, motor_beygir)
        self.vites  = Vites("otomatik")

    def calistir(self):
        self.motor.calistir()    # kompozisyon → motora delege et

    def hizlan(self, artis):
        if not self.motor.calisiyor_mu:
            print("  ❌ Önce motoru çalıştır!")
            return
        self.hiz += artis
        self.vites.vites_yukari()
        print(f"  🚗 Hız: {self.hiz} km/h")

    def dur(self):
        self.hiz = 0
        print(f"  🛑 {self.marka} {self.model} durdu.")
        self.motor.durdur()

    def __str__(self):
        return f"{self.yil} {self.marka} {self.model} ({self.motor})"


araba = Araba("Toyota", "Corolla", 2023, 1.6, 132)
print(f"\n  {araba}")
araba.calistir()
araba.hizlan(30)
araba.hizlan(20)
araba.dur()

# Motor bağımsız test edilebilir → kompozisyonun gücü!
test_motor = Motor(2.0, 200, "elektrik")
test_motor.calistir()
test_motor.durdur()


# ==============================================================================
# BÖLÜM 12: SOLID PRENSİPLERİ — Kısa Özet
# ==============================================================================
#
# SOLID = 5 nesne yönelimli tasarım prensibi.
# Robert C. Martin (Uncle Bob) tarafından tanımlanmıştır.
# Bu prensiplere uyan kod: daha okunabilir, test edilebilir, değiştirilebilir.
#
# S: Single Responsibility → Her sınıfın tek bir sorumluluğu olsun
# O: Open/Closed           → Genişletmeye açık, değiştirmeye kapalı
# L: Liskov Substitution   → Alt sınıf, üst sınıfın yerine kullanılabilmeli
# I: Interface Segregation → Küçük, spesifik arayüzler, dev arayüzler değil
# D: Dependency Inversion  → Soyuta bağlan, somuta değil
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 12: SOLID — Kısa Örnekler")
print("="*60)

# S: Single Responsibility Principle
# ❌ YANLIŞ: Kullanici sınıfı hem kullanıcı verisi hem de email hem de DB
# class Kullanici:
#     def kaydet(self): ...
#     def email_gonder(self): ...
#     def html_olustur(self): ...

# ✅ DOĞRU: Her sınıf tek iş
class KullaniciVerisi:
    def __init__(self, isim, email):
        self.isim  = isim
        self.email = email

class KullaniciDepolama:
    def kaydet(self, kullanici):
        print(f"  💾 {kullanici.isim} veritabanına kaydedildi")

class KullaniciEmail:
    def hosgeldin_gonder(self, kullanici):
        print(f"  📧 {kullanici.email}'e hoşgeldin e-postası gönderildi")


# O: Open/Closed — İndirim örneği
class IndirimHesaplayici:
    def hesapla(self, siparis, indirim_tipi):
        # ❌ Her yeni indirim tipi için bu kodu değiştirmek gerekir!
        if indirim_tipi == "yuzde10":
            return siparis * 0.10
        elif indirim_tipi == "yuzde20":
            return siparis * 0.20

# ✅ DOĞRU: Her yeni indirim tipi için yeni class yaz, mevcut koda dokunma
class IndirimStratejisi(ABC):
    @abstractmethod
    def hesapla(self, tutar): pass

class YuzdeOnIndirim(IndirimStratejisi):
    def hesapla(self, tutar):
        return tutar * 0.10

class YuzdeyirmiIndirim(IndirimStratejisi):
    def hesapla(self, tutar):
        return tutar * 0.20

class OgrenciIndirimi(IndirimStratejisi):  # Yeni ekledik → mevcut koda dokunmadık!
    def hesapla(self, tutar):
        return tutar * 0.15

class Siparis:
    def __init__(self, tutar):
        self.tutar = tutar

    def indirimli_fiyat(self, indirim: IndirimStratejisi):
        indirim_miktari = indirim.hesapla(self.tutar)
        return self.tutar - indirim_miktari

siparis = Siparis(1000)
print(f"\n  %10 indirimli: {siparis.indirimli_fiyat(YuzdeOnIndirim())} TL")
print(f"  %20 indirimli: {siparis.indirimli_fiyat(YuzdeyirmiIndirim())} TL")
print(f"  Öğrenci ind.: {siparis.indirimli_fiyat(OgrenciIndirimi())} TL")


# ==============================================================================
# BÖLÜM 13: BÜYÜK PROJE — BANKA SİSTEMİ
# Tüm OOP konularını bir arada kullanır
# ==============================================================================

print("\n" + "="*60)
print("BÖLÜM 13: BÜYÜK PROJE — BANKA SİSTEMİ")
print("="*60)

# Custom Exceptions
class BankaHatasi(Exception): pass
class YetersizBakiyeHatasi(BankaHatasi):
    def __init__(self, gereken, mevcut):
        super().__init__(f"Yetersiz bakiye. Gereken: {gereken:.2f} TL, Mevcut: {mevcut:.2f} TL")
class HesapKapaliHatasi(BankaHatasi): pass
class LimitAsildiHatasi(BankaHatasi): pass


# Abstract base
class Hesap(ABC):
    _sonraki_id = 1000

    def __init__(self, sahip_adi, baslangic_bakiye=0):
        self.hesap_no      = f"TR{Hesap._sonraki_id:06d}"
        Hesap._sonraki_id += 1
        self.sahip         = sahip_adi
        self._bakiye       = baslangic_bakiye
        self._islemler     = []
        self._aktif        = True
        self._acilis_tar   = datetime.date.today()

    @property
    def bakiye(self):
        return self._bakiye

    @property
    def aktif_mi(self):
        return self._aktif

    @abstractmethod
    def para_yatir(self, miktar):
        pass

    @abstractmethod
    def para_cek(self, miktar):
        pass

    def _islem_kaydet(self, tur, miktar, aciklama=""):
        self._islemler.append({
            "id"       : len(self._islemler) + 1,
            "tur"      : tur,
            "miktar"   : miktar,
            "bakiye"   : self._bakiye,
            "aciklama" : aciklama,
            "tarih"    : datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        })

    def transfer_gonder(self, hedef_hesap, miktar):
        if not self._aktif:
            raise HesapKapaliHatasi(f"{self.hesap_no} hesabı kapalı!")
        self.para_cek(miktar)
        hedef_hesap.para_yatir(miktar)
        self._islemler[-1]["aciklama"] = f"Transfer → {hedef_hesap.hesap_no}"
        print(f"  ✅ Transfer: {miktar:,.2f} TL → {hedef_hesap.hesap_no}")

    def ekstre_yazdir(self):
        print(f"\n  {'═'*50}")
        print(f"  HESAP EKSTRESİ")
        print(f"  Hesap No : {self.hesap_no}")
        print(f"  Sahip    : {self.sahip}")
        print(f"  Tür      : {self.__class__.__name__}")
        print(f"  Bakiye   : {self._bakiye:>10,.2f} TL")
        print(f"  {'─'*50}")
        print(f"  {'No':<4} {'Tarih':<18} {'Tür':<10} {'Miktar':>10} {'Bakiye':>12}")
        print(f"  {'─'*50}")
        for i in self._islemler[-5:]:   # son 5 işlem
            tur_goster = f"+{i['miktar']:,.2f}" if i["tur"] == "yatirma" else f"-{i['miktar']:,.2f}"
            print(f"  {i['id']:<4} {i['tarih']:<18} {i['tur']:<10} {tur_goster:>10} {i['bakiye']:>12,.2f}")
        print(f"  {'═'*50}")

    def __str__(self):
        durum = "✅" if self._aktif else "❌"
        return f"{durum} {self.hesap_no} | {self.sahip:<20} | {self._bakiye:>12,.2f} TL"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.hesap_no}', '{self.sahip}', {self._bakiye})"

    def __eq__(self, other):
        return isinstance(other, Hesap) and self.hesap_no == other.hesap_no

    def __lt__(self, other):
        return self._bakiye < other._bakiye


class VadesizHesap(Hesap):
    def __init__(self, sahip_adi, baslangic_bakiye=0, gunluk_limit=5000):
        super().__init__(sahip_adi, baslangic_bakiye)
        self.gunluk_limit      = gunluk_limit
        self._bugun_cekilen    = 0

    def para_yatir(self, miktar):
        if miktar <= 0:
            raise ValueError("Miktar 0'dan büyük olmalı!")
        if not self._aktif:
            raise HesapKapaliHatasi("Hesap kapalı!")
        self._bakiye += miktar
        self._islem_kaydet("yatirma", miktar)
        print(f"  ✅ {miktar:,.2f} TL yatırıldı → Bakiye: {self._bakiye:,.2f} TL")

    def para_cek(self, miktar):
        if not self._aktif:
            raise HesapKapaliHatasi("Hesap kapalı!")
        if miktar <= 0:
            raise ValueError("Miktar 0'dan büyük olmalı!")
        if miktar > self._bakiye:
            raise YetersizBakiyeHatasi(miktar, self._bakiye)
        if self._bugun_cekilen + miktar > self.gunluk_limit:
            raise LimitAsildiHatasi(f"Günlük limit ({self.gunluk_limit:,.0f} TL) aşıldı!")
        self._bakiye        -= miktar
        self._bugun_cekilen += miktar
        self._islem_kaydet("cekme", miktar)
        print(f"  ✅ {miktar:,.2f} TL çekildi → Bakiye: {self._bakiye:,.2f} TL")


class KrediHesabi(Hesap):
    def __init__(self, sahip_adi, kredi_limiti=10000):
        super().__init__(sahip_adi, 0)
        self.kredi_limiti  = kredi_limiti
        self._borc         = 0
        self.faiz_orani    = 0.02   # aylık %2

    @property
    def kullanilabilir_limit(self):
        return self.kredi_limiti - self._borc

    @property
    def borc(self):
        return self._borc

    def para_yatir(self, miktar):
        # Kredi hesabına para yatırmak = borç ödemek
        odenen = min(miktar, self._borc)
        self._borc -= odenen
        self._bakiye = -self._borc
        self._islem_kaydet("yatirma", miktar, "Borç ödeme")
        print(f"  ✅ {odenen:,.2f} TL borç ödendi → Kalan borç: {self._borc:,.2f} TL")

    def para_cek(self, miktar):
        if not self._aktif:
            raise HesapKapaliHatasi("Hesap kapalı!")
        if miktar > self.kullanilabilir_limit:
            raise LimitAsildiHatasi(
                f"Kredi limiti aşılır! Kullanılabilir: {self.kullanilabilir_limit:,.2f} TL"
            )
        self._borc   += miktar
        self._bakiye  = -self._borc
        self._islem_kaydet("cekme", miktar, "Kredi kullanımı")
        print(f"  ✅ {miktar:,.2f} TL kredi kullanıldı → Borç: {self._borc:,.2f} TL")

    def faiz_hesapla(self):
        faiz = self._borc * self.faiz_orani
        print(f"  💸 Aylık faiz: {faiz:,.2f} TL (Borç: {self._borc:,.2f} TL × %{self.faiz_orani*100})")
        return faiz


class Banka:
    def __init__(self, banka_adi):
        self.banka_adi  = banka_adi
        self.__hesaplar = {}
        self.__kurulus  = datetime.date.today()

    def hesap_ac(self, hesap_tipi, sahip_adi, **kwargs):
        tipler = {
            "vadesiz": VadesizHesap,
            "kredi"  : KrediHesabi,
        }
        if hesap_tipi not in tipler:
            raise ValueError(f"Bilinmeyen hesap tipi: {hesap_tipi}")
        hesap = tipler[hesap_tipi](sahip_adi, **kwargs)
        self.__hesaplar[hesap.hesap_no] = hesap
        print(f"  🏦 {self.banka_adi}: {hesap_tipi} hesabı açıldı → {hesap.hesap_no}")
        return hesap

    def hesap_bul(self, hesap_no):
        if hesap_no not in self.__hesaplar:
            raise KeyError(f"Hesap bulunamadı: {hesap_no}")
        return self.__hesaplar[hesap_no]

    def tum_hesaplar(self):
        print(f"\n  🏦 {self.banka_adi} — Tüm Hesaplar")
        print(f"  {'─'*55}")
        for hesap in sorted(self.__hesaplar.values(), reverse=True):  # __lt__ kullanır
            print(f"  {hesap}")
        print(f"  {'─'*55}")
        toplam = sum(h.bakiye for h in self.__hesaplar.values() if h.bakiye > 0)
        print(f"  Toplam mevduat: {toplam:,.2f} TL")

    def __len__(self):
        return len(self.__hesaplar)

    def __contains__(self, hesap_no):
        return hesap_no in self.__hesaplar


# ─── SENARYO ─────────────────────────────────────────────────────────────────
print()
banka = Banka("Python Bank A.Ş.")

# Hesap aç
h1 = banka.hesap_ac("vadesiz", "Ali Yılmaz",    baslangic_bakiye=10000)
h2 = banka.hesap_ac("vadesiz", "Ayşe Kaya",     baslangic_bakiye=5000, gunluk_limit=3000)
h3 = banka.hesap_ac("kredi",   "Mehmet Demir",   kredi_limiti=20000)

print()
h1.para_yatir(5000)
h1.para_cek(2000)

try:
    h2.para_cek(5000)  # günlük limit aşımı
except LimitAsildiHatasi as e:
    print(f"  ⚠️ {e}")

try:
    h1.transfer_gonder(h2, 3000)
except BankaHatasi as e:
    print(f"  ⚠️ {e}")

print()
h3.para_cek(8000)
h3.faiz_hesapla()
h3.para_yatir(3000)

banka.tum_hesaplar()
h1.ekstre_yazdir()

print(f"\n  {banka.banka_adi} toplam hesap: {len(banka)}")   # __len__
print(f"  {h1.hesap_no} bankada var mı? {h1.hesap_no in banka}")  # __contains__


# ==============================================================================
# 📋 OOP ÖZET TABLOSU
# ==============================================================================
print("\n")
print("="*60)
print("  📋 OOP ÖZET TABLOSU")
print("="*60)
ozet = [
    ("Class/Object",    "Şablon ve örnekler",                 "BankaHesabi / h1, h2"),
    ("__init__",        "Nesne başlatma",                     "self.bakiye = 0"),
    ("self",            "O anki nesneye referans",            "self.para_cek()"),
    ("Instance Method", "Nesneye özgü işlem",                 "h1.para_yatir(100)"),
    ("Class Method",    "Sınıfa ait işlem (@classmethod)",    "Hesap.toplam_say()"),
    ("Static Method",   "Bağımsız yardımcı (@staticmethod)",  "Hesap.iban_gecerli_mi()"),
    ("@property",       "Attribute gibi metod",               "hesap.bakiye"),
    ("Encapsulation",   "Veriyi koru (__private)",            "self.__sifre"),
    ("Inheritance",     "Sınıftan türetme (IS-A)",            "Muhendis(Calisan)"),
    ("super()",         "Parent metodunu çağır",              "super().__init__()"),
    ("Override",        "Miras alınan metodu yeniden yaz",    "def calis(self)"),
    ("Polymorphism",    "Aynı arayüz, farklı davranış",       "sekil.alan_hesapla()"),
    ("Abstraction",     "Abstract class (ABC)",               "class Odeme(ABC)"),
    ("@abstractmethod", "Alt sınıf implement etmeli",         "def odeme_yap()"),
    ("Magic Methods",   "Operatör overloading",               "__str__, __len__"),
    ("Composition",     "İçinde nesne tutmak (HAS-A)",        "self.motor = Motor()"),
]
print(f"  {'KAVRAM':<20} {'AÇIKLAMA':<30} {'ÖRNEK'}")
print(f"  {'─'*60}")
for kavram, aciklama, ornek in ozet:
    print(f"  {kavram:<20} {aciklama:<30} {ornek}")
print("="*60)
