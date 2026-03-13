#!/bin/bash

######################################################################
######################################################################
##                                                                  ##
##    ██████╗ ██╗████████╗    ██████╗ ███████╗██╗  ██╗██████╗       ##
##   ██╔════╝ ██║╚══██╔══╝    ██╔══██╗██╔════╝██║  ██║██╔══██╗     ##
##   ██║  ███╗██║   ██║       ██████╔╝█████╗  ███████║██████╔╝     ##
##   ██║   ██║██║   ██║       ██╔══██╗██╔══╝  ██╔══██║██╔══██╗     ##
##   ╚██████╔╝██║   ██║       ██║  ██║███████╗██║  ██║██║  ██║     ##
##    ╚═════╝ ╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ##
##                                                                  ##
##           Git & GitHub — Tam Öğretici Rehber                     ##
##           Yazar: Abdulkadir Yilmaz                               ##
##           Tarih: 2026-03-11                                      ##
##           Seviye: Sıfırdan Profesyonele                          ##
##                                                                  ##
######################################################################
######################################################################
#
# BU DOSYA NEDİR?
# ----------------
# Bu dosya .sh uzantılı bir öğretici dokümandır.
# İçindeki komutları TEK TEK kopyala-yapıştır ile çalıştırabilirsin.
# DOSYANIN TAMAMINI ÇALIŞTIRMA! Sadece oku ve öğren.
#
# NASIL KULLANILIR?
# -----------------
# 1. Bu dosyayı bir metin editöründe aç (VS Code önerilir)
# 2. Bölüm bölüm oku
# 3. Komutları terminal'de tek tek dene
# 4. Hata alırsan BÖLÜM 8'e git
#


######################################################################
#                                                                    #
#                    BÖLÜM 1 — GIT NEDİR?                           #
#                    NEDEN KULLANIRIZ?                               #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 1.1 — Git Nedir?
# ═══════════════════════════════════════════════════════════════════
#
# Git bir "versiyon kontrol sistemi"dir (VCS).
#
# Basit Türkçe ile:
#   Git = dosyalarının her halini hatırlayan bir zaman makinesi.
#
# Düşün ki bir Word belgesi yazıyorsun:
#   - odev_v1.docx
#   - odev_v2.docx
#   - odev_v2_final.docx
#   - odev_v2_final_GERCEKTEN_FINAL.docx
#
# Git ile bunu yapman gerekmiyor. Git her değişikliği otomatik
# kaydeder ve istediğin zaman geriye dönebilirsin.
#
#   Dosya.txt (v1) ──→ Dosya.txt (v2) ──→ Dosya.txt (v3)
#       │                   │                   │
#       └── geri dön ───────┘                   │
#                           └── geri dön ───────┘
#

# ═══════════════════════════════════════════════════════════════════
# 1.2 — Neden Versiyon Kontrol Sistemi Kullanırız?
# ═══════════════════════════════════════════════════════════════════
#
# 1. GERİ ALMA      → Hata yaptın? 5 commit öncesine dön.
# 2. TAKIM ÇALIŞMASI → 10 kişi aynı projede çalışabilir.
# 3. BRANCHING       → Herkes kendi kopyasında çalışır, sonra birleştirir.
# 4. YEDEKLEME       → Kodun GitHub'da, bilgisayarın bozulsa bile güvende.
# 5. GEÇMİŞ TAKİBİ  → Kim, ne zaman, neyi değiştirdi? Hepsi kayıtlı.
#

# ═══════════════════════════════════════════════════════════════════
# 1.3 — Git vs GitHub — Farkı Ne?
# ═══════════════════════════════════════════════════════════════════
#
# ┌──────────────────────────────────────────────────────────┐
# │  GIT                        │  GITHUB                    │
# │─────────────────────────────│────────────────────────────│
# │  Bilgisayarında çalışır     │  İnternette çalışır        │
# │  Komut satırı aracı         │  Web sitesi + platform     │
# │  Offline çalışır            │  Online olmalısın          │
# │  Dosyaları takip eder       │  Git repolarını barındırır │
# │  Linus Torvalds yazdı       │  Microsoft'un platformu   │
# │  Araç (tool)                │  Hizmet (service)          │
# └──────────────────────────────────────────────────────────┘
#
# Kısaca:
#   Git    = motor
#   GitHub = garaj + showroom
#

# ═══════════════════════════════════════════════════════════════════
# 1.4 — Repository (Repo) Nedir?
# ═══════════════════════════════════════════════════════════════════
#
# Repo = Git ile takip edilen bir proje klasörü.
#
# İçinde:
#   - Proje dosyaların (kod, döküman, resim...)
#   - .git klasörü (gizli, Git'in beyni — DOKUNMA!)
#
# İki türü var:
#   Local repo  → Bilgisayarında (git init veya git clone ile oluşur)
#   Remote repo → GitHub'da (github.com/kullanici/repo-adi)
#


######################################################################
#                                                                    #
#                    BÖLÜM 2 — İLK KURULUM                          #
#                    (BİR KERE YAPILIR)                              #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 2.1 — Git'i Kur (macOS)
# ═══════════════════════════════════════════════════════════════════

# macOS'ta Git genelde zaten yüklüdür. Kontrol et:
git --version
# Çıktı: git version 2.xx.x

# Eğer yüklü değilse:
brew install git

# ═══════════════════════════════════════════════════════════════════
# 2.2 — Kendini Tanıt (git config)
# ═══════════════════════════════════════════════════════════════════
#
# Git her commit'e senin adını ve emailini yazar.
# Bu bilgiler GitHub hesabınla AYNI olmalı.

git config --global user.name "abdulkadir-yz"
git config --global user.email "senin-github-emailin@example.com"

# Doğru ayarlandığını kontrol et:
git config --global user.name
git config --global user.email

# Tüm ayarları gör:
git config --list

# ⚠️ ÖNEMLİ:
# --global = tüm projeler için geçerli
# Eğer sadece BİR proje için farklı isim istersen:
#   cd proje-klasoru
#   git config user.name "farkli-isim"    (--global olmadan)

# ═══════════════════════════════════════════════════════════════════
# 2.3 — SSH Key Oluşturma ve GitHub'a Ekleme
# ═══════════════════════════════════════════════════════════════════
#
# SSH = Şifresiz güvenli bağlantı.
# Bir kere kurarsın, bir daha şifre sormaz.
#
# NEDEN SSH?
# - HTTPS → her push'ta şifre/token sorar
# - SSH   → otomatik, güvenli, şifresiz

# Adım 1: SSH key oluştur
ssh-keygen -t ed25519 -C "senin-github-emailin@example.com"
# Soru soracak:
#   Enter file in which to save the key → ENTER'a bas (varsayılan)
#   Enter passphrase                    → ENTER'a bas (boş bırak)
#   Enter same passphrase again         → ENTER'a bas

# Adım 2: SSH agent'ı başlat
eval "$(ssh-agent -s)"
# Çıktı: Agent pid 12345

# Adım 3: SSH key'i agent'a ekle
ssh-add ~/.ssh/id_ed25519

# Adım 4: Public key'i kopyala
cat ~/.ssh/id_ed25519.pub
# Çıkan TÜÜÜM metni kopyala (ssh-ed25519 ile başlar)

# Adım 5: GitHub'a ekle
# 1. github.com → Sağ üst profil resmi → Settings
# 2. Sol menüde "SSH and GPG keys"
# 3. "New SSH key" butonuna tıkla
# 4. Title: "Mac Bilgisayarım" (istediğini yaz)
# 5. Key: Kopyaladığın metni yapıştır
# 6. "Add SSH key" butonuna tıkla

# Adım 6: Test et
ssh -T git@github.com
# Başarılı çıktı:
#   Hi abdulkadir-yz! You've successfully authenticated,
#   but GitHub does not provide shell access.
#
# ✅ Bu mesajı gördüysen SSH HAZIR!


######################################################################
#                                                                    #
#                    BÖLÜM 3 — TEMEL KAVRAMLAR                      #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 3.1 — Git'in 4 Alanı (Çok Önemli!)
# ═══════════════════════════════════════════════════════════════════
#
# ┌─────────────┐    git add     ┌──────────────┐   git commit   ┌────────────────┐   git push    ┌─────────────────┐
# │  WORKING    │ ─────────────→ │   STAGING    │ ─────────────→ │    LOCAL       │ ────────────→ │    REMOTE       │
# │  DIRECTORY  │                │   AREA       │                │    REPO        │              │    REPO         │
# │             │                │              │                │    (.git)      │              │    (GitHub)     │
# │ Dosyaları   │                │ "Hazırladım, │                │ "Kaydettim,    │              │ "Herkese        │
# │ düzenlediğin│                │  commit'e    │                │  geçmişe       │              │  gönderdim"     │
# │ yer         │                │  hazır"      │                │  yazıldı"      │              │                 │
# └─────────────┘                └──────────────┘                └────────────────┘              └─────────────────┘
#
#                                                                                    git pull
#                                                                 ←──────────────────────────────
#
# Basit benzetme:
#   Working Directory = Masanın üstü (çalıştığın yer)
#   Staging Area      = Kutuya koydun (göndermek için hazırladın)
#   Local Repo        = Kargoyu teslim ettin (kayıt altında)
#   Remote Repo       = Karşı tarafa ulaştı (GitHub'da herkes görür)
#

# ═══════════════════════════════════════════════════════════════════
# 3.2 — Temel Komutların Akışı
# ═══════════════════════════════════════════════════════════════════
#
#   [Dosya düzenle] → git add . → git commit -m "mesaj" → git push
#        │                │              │                    │
#        ▼                ▼              ▼                    ▼
#   Working Dir      Staging        Local Repo           GitHub
#

# ═══════════════════════════════════════════════════════════════════
# 3.3 — Branch Nedir? Neden Kendi Branch'imizi Oluştururuz?
# ═══════════════════════════════════════════════════════════════════
#
# Branch = Projenin bağımsız bir kopyası üzerinde çalışmak.
#
# Gerçek hayat benzetmesi:
#   main branch = Kitabın yayınlanmış hali
#   senin branch = Kitabın taslak kopyası (üzerinde çalışıyorsun)
#   Taslak bitince → yayınlanmış hale birleştirirsin (merge)
#
# Görsel:
#
#   main:    ●────●────●────●────●────●
#                  \                  /
#   kadir:          ●────●────●────●
#                   (kendi çalışman)
#
# NEDEN BRANCH?
# 1. main branch her zaman ÇALIŞIR durumda kalır
# 2. Hata yapsan bile sadece kendi branch'in bozulur
# 3. Takımda herkes kendi branch'inde çalışır, kimse birbirini bozmaz
# 4. Hazır olunca Pull Request (PR) açarsın, hoca/takım kontrol eder, sonra birleşir
#

# ═══════════════════════════════════════════════════════════════════
# 3.4 — "origin" Ne Demek?
# ═══════════════════════════════════════════════════════════════════
#
# "origin" = GitHub'daki remote repo'nun TAKMA ADI.
#
#   git push origin main
#           │       │
#           │       └── hangi branch?
#           └── nereye? (GitHub'a)
#
# Kontrol et:
git remote -v
# Çıktı:
#   origin  git@github.com:SEAI-007/CS.git (fetch)
#   origin  git@github.com:SEAI-007/CS.git (push)
#

# ═══════════════════════════════════════════════════════════════════
# 3.5 — "HEAD" Ne Demek?
# ═══════════════════════════════════════════════════════════════════
#
# HEAD = "Şu anda neredesin?" işaretçisi.
#
# Her zaman bir commit veya branch'i gösterir.
# Genelde: HEAD → kadir → son commit
#
# Kontrol et:
git log --oneline -1
# Çıktı: abc1234 (HEAD -> kadir) son commit mesajın
#


######################################################################
#                                                                    #
#                    BÖLÜM 4 — REPO CLONE ETME                      #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 4.1 — Clone Neden Yaparız?
# ═══════════════════════════════════════════════════════════════════
#
# Clone = GitHub'daki repoyu bilgisayarına indirmek.
#
# Clone sadece dosyaları indirmez, TÜM GEÇMİŞİ de indirir:
#   - Tüm commit'ler
#   - Tüm branch'ler
#   - Tüm geçmiş
#
# Clone ≠ Download ZIP!
#   ZIP → sadece dosyaları indirir, git geçmişi YOKTUR
#   Clone → her şeyi indirir, push/pull yapabilirsin

# ═══════════════════════════════════════════════════════════════════
# 4.2 — HTTPS vs SSH Clone — Fark Ne?
# ═══════════════════════════════════════════════════════════════════
#
# ┌─────────────────────────────────────────────────────────────┐
# │  YÖNTEM   │  KOMUT                                         │
# │───────────│────────────────────────────────────────────────│
# │  HTTPS    │  git clone https://github.com/user/repo.git   │
# │  SSH      │  git clone git@github.com:user/repo.git       │
# └─────────────────────────────────────────────────────────────┘
#
# ┌─────────────────────────────────────────────────────────────┐
# │  HTTPS                      │  SSH                         │
# │─────────────────────────────│───────────────────────────��──│
# │  Her push'ta şifre sorar    │  Şifre sormaz (key ile)     │
# │  Token gerekir              │  SSH key gerekir             │
# │  Kurulumu kolay              │  Bir kere kurulur, sonra ok │
# │  Yeni başlayanlar için       │  Profesyoneller tercih eder │
# └─────────────────────────────────────────────────────────────┘
#
# ÖNERİ: SSH kullan! Bir kere kur, bir daha uğraşma.
#

# ═══════════════════════════════════════════════════════════════════
# 4.3 — Birisi Beni Repoya Ekledi, Nasıl Clone Ederim?
# ═══════════════════════════════════════════════════════════════════

# Adım 1: İstediğin klasöre git
cd ~/Desktop

# Adım 2: SSH ile clone et (ÖNEMLİ: SSH linkini kullan!)
git clone git@github.com:SEAI-007/CS.git

# Adım 3: Klasöre gir
cd CS

# Adım 4: Kontrol et
git status
# Çıktı: On branch main ... nothing to commit, working tree clean ✅

# ═══════════════════════════════════════════════════════════════════
# 4.4 — Clone Sonrası İlk Yapılacaklar
# ═══════════════════════════════════════════════════════════════════

# 1. Doğru yerde misin?
pwd
# Çıktı: /Users/abdulkadiryilmaz/Desktop/CS

# 2. Branch'leri gör
git branch -a
# Çıktı:
# * main                          ← local branch (şu anda buradasın)
#   remotes/origin/main           ← GitHub'daki branch
#   remotes/origin/kadir          ← varsa diğer branch'ler

# 3. Kendi branch'ini oluştur
git checkout -b kadir

# 4. Bağlantı SSH mi kontrol et
git remote -v
# ✅ git@github.com ile başlamalı
# ❌ https:// ile başlıyorsa BÖLÜM 7.2'ye git


######################################################################
#                                                                    #
#                    BÖLÜM 5 — BRANCH İŞ AKIŞI                      #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 5.1 — Neden Branch Oluştururuz? (Gerçek Hayat Senaryosu)
# ═══════════════════════════════════════════════════════════════════
#
# SENARYO:
#   Hoca "CS" reposunda ders materyallerini paylaşıyor.
#   10 öğrenci aynı repoda çalışıyor.
#
#   Eğer herkes main'e push yaparsa:
#   ❌ Öğrenci A'nın kodu Öğrenci B'nin kodunu bozar
#   ❌ Hoca kimin ne yaptığını takip edemez
#   ❌ Çalışan kod bozulur, kimse çalışamaz
#
#   Branch ile:
#   ✅ Herkesin kendi alanı var
#   ✅ main her zaman temiz ve çalışır
#   ✅ PR ile kontrollü birleşme
#

# ═══════════════════════════════════════════════════════════════════
# 5.2 — Branch Komutları
# ═══════════════════════════════════════════════════════════════════

# Yeni branch oluştur VE o branch'e geç (en çok kullanılan):
git checkout -b kadir
# Çıktı: Switched to a new branch 'kadir'

# Tüm local branch'leri listele:
git branch
# Çıktı:
# * kadir     ← * olan = şu anda bulunduğun branch
#   main

# Tüm branch'leri listele (remote dahil):
git branch -a

# main branch'e geri dön:
git checkout main

# Tekrar kendi branch'ine geç:
git checkout kadir

# Branch sil (artık lazım değilse):
git branch -d kadir
# ⚠️ Dikkat: Silmeden önce main'e geç!

# ═══════════════════════════════════════════════════════════════════
# 5.3 — Branch İsimlendirme Kuralları (Best Practices)
# ═══════════════════════════════════════════════════════════════════
#
# ✅ İYİ İSİMLER:
#   kadir
#   kadir/week5-homework
#   feature/login-page
#   fix/bug-123
#   homework/linear-data-structures
#
# ❌ KÖTÜ İSİMLER:
#   my branch          (boşluk kullanma!)
#   KADIR              (küçük harf kullan)
#   asdfgh             (anlamlı isim ver)
#   yeni               (ne yenisi? açıklayıcı ol)
#
# KURALLAR:
# 1. Boşluk kullanma → tire (-) veya slash (/) kullan
# 2. Küçük harf kullan
# 3. Anlamlı isim ver
# 4. Türkçe karakter kullanma (ş, ğ, ü, ö, ç, ı)


######################################################################
#                                                                    #
#                    BÖLÜM 6 — GÜNLÜK ÇALIŞMA DÖNGÜSÜ               #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 6.1 — Sabah Başlarken (Her Gün İlk Yaptığın Şey)
# ═══════════════════════════════════════════════════════════════════

# 1. Proje klasörüne git
cd ~/Desktop/CS

# 2. Kendi branch'ine geç
git checkout kadir

# 3. Hocanın/takımın güncellemelerini çek
git pull origin main
# Bu komut main'deki yenilikleri senin branch'ine alır

# 4. Durumu kontrol et
git status

# ═══════════════════════════════════════════════════════════════════
# 6.2 — git status — HER ZAMAN BUNUNLA BAŞLA!
# ═══════════════════════════════════════════════════════════════════

git status

# Olası çıktılar ve anlamları:
#
# ✅ "nothing to commit, working tree clean"
#    → Her şey yolunda, değişiklik yok
#
# 🔴 "Untracked files:" (kırmızı dosya adları)
#    → Yeni dosyalar var, henüz git add yapılmamış
#
# 🟢 "Changes to be committed:" (yeşil dosya adları)
#    → git add yapılmış, commit'e hazır
#
# 🔴 "Changes not staged for commit:" (kırmızı dosya adları)
#    → Dosya değişmiş ama git add yapılmamış

# ═══════════════════════════════════════════════════════════════════
# 6.3 — git add — Değişiklikleri Hazırla
# ═══════════════════════════════════════════════════════════════════

# Tüm değişiklikleri ekle (en yaygın kullanım):
git add .

# Sadece belirli bir dosyayı ekle:
git add dosya.txt

# Sadece belirli bir klasörü ekle:
git add weekly/

# Birden fazla dosya ekle:
git add dosya1.txt dosya2.txt dosya3.txt

# ⚠️ "git add ." noktayı unutma! Nokta = "bu klasördeki her şey"

# ═══════════════════════════════════════════════════════════════════
# 6.4 — git commit — Değişiklikleri Kaydet
# ═══════════════════════════════════════════════════════════════════

git commit -m "açıklayıcı commit mesajı"

# İYİ COMMIT MESAJLARI:
# ✅ "week5 ödev tamamlandı - linked list implementasyonu"
# ✅ "binary search fonksiyonu eklendi"
# ✅ "README güncellendi - proje açıklaması eklendi"
# ✅ "bug fix: sonsuz döngü sorunu çözüldü"
#
# KÖTÜ COMMIT MESAJLARI:
# ❌ "asdfasdf"
# ❌ "update"
# ❌ "fix"
# ❌ "aaa"
# ❌ "değişiklik yaptım"
#
# KURALI: Mesajı okuyan biri "ne değişti?" sorusunu anlayabilmeli.

# ═══════════════════════════════════════════════════════════════════
# 6.5 — git push — GitHub'a Gönder
# ═════════════════════════════════════════���═════════════════════════

# İLK PUSH (branch'i GitHub'a ilk kez gönderirken):
git push -u origin kadir
# -u = upstream ayarla (bir kere yeterli)
# origin = GitHub
# kadir = branch adın

# SONRAKI PUSH'LAR (artık sadece bu yeterli):
git push

# ═══════════════════════════════════════════════════════════════════
# 6.6 — git pull — GitHub'dan Çek
# ═══════════════════════════════════════════════════════════════════

# Hocanın/takımın main'deki güncellemelerini çek:
git pull origin main

# Kendi branch'indeki güncellemeleri çek (başka bilgisayardan push yaptıysan):
git pull origin kadir

# ⚠️ ÖNEMLİ: Push'tan ÖNCE her zaman pull yap!

# ═══════════════════════════════════════════════════════════════════
# 6.7 — Gün Sonu Rutini
# ══════════���════════════════════════════════════════════════════════

git status                          # 1. Ne değişti?
git add .                           # 2. Hepsini ekle
git commit -m "bugün ne yaptığını yaz"  # 3. Kaydet
git push                            # 4. GitHub'a gönder

# 4 ADIM — her gün, her zaman, bu sırayla. Ezberle! ✅


######################################################################
#                                                                    #
#                    BÖLÜM 7 — GERÇEK HAYAT SENARYOLARI             #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.1 — Hoca Beni Repoya Ekledi, İlk Kez Çalışmaya Başlıyorum
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Hoca "SEAI-007/CS" reposuna seni collaborator olarak ekledi.
#        GitHub'dan davet emaili geldi, kabul ettin.
#        Şimdi bilgisayarına çekip çalışmaya başlamak istiyorsun.

# Adım 1: İstediğin klasöre git
cd ~/Desktop

# Adım 2: SSH ile clone et
git clone git@github.com:SEAI-007/CS.git

# Adım 3: İçine gir
cd CS

# Adım 4: Kendi branch'ini oluştur
git checkout -b kadir

# Adım 5: Branch'ini GitHub'a tanıt
git push -u origin kadir

# ✅ Artık çalışmaya hazırsın!

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.2 — HTTPS ile Clone Yaptım Ama SSH Kullanmam Lazım
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Yanlışlıkla şu komutu kullandın:
#   git clone https://github.com/SEAI-007/CS.git
# Her push'ta şifre soruyor veya "fatal: failed to get: -128" hatası alıyorsun.

# Adım 1: Mevcut bağlantıyı kontrol et
git remote -v
# Çıktı (SORUNLU):
#   origin  https://github.com/SEAI-007/CS.git (fetch)
#   origin  https://github.com/SEAI-007/CS.git (push)

# Adım 2: SSH'a çevir (TEK KOMUT!)
git remote set-url origin git@github.com:SEAI-007/CS.git

# Adım 3: Doğrulandığını kontrol et
git remote -v
# Çıktı (DOĞRU):
#   origin  git@github.com:SEAI-007/CS.git (fetch)
#   origin  git@github.com:SEAI-007/CS.git (push)

# Adım 4: Test et
git push
# ✅ Artık şifre sormayacak!

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.3 — Dosya Düzenledim, GitHub'a Göndermek İstiyorum
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Ödevini yaptın, dosyaları düzenledin, şimdi GitHub'a yüklemek istiyorsun.

# Adım 1: Kendi branch'inde olduğundan emin ol
git branch
# * kadir    ← burada olmalısın

# Adım 2: Ne değişti kontrol et
git status

# Adım 3-4-5: Ekle, kaydet, gönder
git add .
git commit -m "hafta 5 linear data structures ödevi tamamlandı"
git push

# ✅ GitHub'a gitti!

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.4 — Hoca Main'de Bir Şey Değiştirdi, Locale Çekmem Lazım
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Hoca main branch'e yeni ders materyali ekledi.
#        Senin local'inde bu güncellemeler yok.

# Adım 1: Kendi branch'inde ol
git checkout kadir

# Adım 2: Main'deki güncellemeleri çek
git pull origin main

# Olası sonuçlar:
#   a) "Already up to date."           → Zaten güncelsin
#   b) "Fast-forward"                  → Otomatik güncellendi ✅
#   c) "CONFLICT..."                   → Çakışma var → SENARYO 7.6'ya git

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.5 — Push Yapmaya Çalıştım Ama Hata Aldım
# ═══════════════════════════════════════════════════════════════════
#
# HATA: error: failed to push some refs to 'github.com:...'
# SEBEP: Remote'da (GitHub'da) senin local'inde olmayan değişiklikler var.

# Çözüm: Önce çek, sonra gönder
git pull origin kadir         # veya git pull origin main
# Otomatik birleşirse:
git push

# Eğer conflict çıkarsa → SENARYO 7.6

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.6 — Merge Conflict Çıktı, Ne Yapacağım?!
# ═══════════════════════════════════════════════════════════════════
#
# HATA: CONFLICT (content): Merge conflict in dosya.txt
#
# PANİK YAPMA! Bu normal bir durum. Git sana soruyor:
# "İki farklı değişiklik var, hangisini istiyorsun?"
#
# Çakışan dosyayı açtığında şunu göreceksin:
#
#   <<<<<<< HEAD
#   Senin yazdığın kod (local)
#   =======
#   Başkasının yazdığı kod (GitHub'daki)
#   >>>>>>> origin/main
#
# ÇÖZÜM:

# Adım 1: Çakışan dosyayı VS Code'da aç
code dosya.txt
# VS Code'da "Accept Current Change", "Accept Incoming Change",
# veya "Accept Both Changes" butonları göreceksin.
# Birini seç veya manuel düzenle.

# Adım 2: <<<<<<< , ======= , >>>>>>> satırlarını tamamen sil

# Adım 3: Dosyayı kaydet

# Adım 4: Git'e "çözdüm" de
git add .
git commit -m "merge conflict çözüldü"
git push

# ✅ Tamamdır!

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.7 — Yanlış Branch'te Çalıştığımı Fark Ettim
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: main branch'te dosya düzenledin ama kadir'de olman gerekiyordu.
#        Henüz COMMIT yapmadın.

# Çözüm: Değişiklikleri stash'le ve doğru branch'e taşı
git stash                   # Değişiklikleri geçici sakla
git checkout kadir          # Doğru branch'e geç
git stash pop               # Değişiklikleri geri getir

# Artık doğru branch'tesin ve değişikliklerin kaybolmadı! ✅

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.8 — Commit'imi Geri Almak İstiyorum
# ═══════════════════════════════════════════════════════════════════

# DURUM A: Commit yaptım ama henüz PUSH yapmadım
# Son commit'i geri al, değişiklikler dosyalarda kalsın:
git reset --soft HEAD~1
# Şimdi dosyalar hala değişmiş durumda, tekrar düzenleyebilirsin

# DURUM B: Commit yaptım VE push da yaptım
# Yeni bir commit ile geri al (geçmişi silmez, güvenli yol):
git revert HEAD
git push

# ⚠️ DİKKAT: git reset --hard kullanma! Değişikliklerini kalıcı olarak siler.

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.9 — Yanlışlıkla main'e Push Ettim
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: main branch'te olduğunu fark etmeden commit + push yaptın.
# ⚠️ Eğer repo'da branch protection varsa zaten push edemezsin.

# Çözüm:
# 1. Commit hash'ini not al
git log --oneline -3
# Çıktı: abc1234 yanlış commit mesajı   ← bunu not al

# 2. main'deki commit'i geri al
git revert HEAD
git push origin main

# 3. Kendi branch'ine geç ve orada çalışmaya devam et
git checkout kadir

# DERS: Her zaman çalışmaya başlamadan "git branch" ile nerede
#       olduğunu kontrol et!

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.10 — .gitignore'a Dosya Eklemem Lazım
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Bazı dosyaların GitHub'a gitmesini istemiyorsun.
#   Örnek: .DS_Store, node_modules/, __pycache__/, .env
#
# .gitignore dosyası Git'e "bu dosyaları takip etme" der.

# .gitignore dosyası oluştur veya düzenle:
cat > .gitignore << 'EOF'
# macOS sistem dosyaları
.DS_Store
.DS_Store?
._*

# Python
__pycache__/
*.pyc
*.pyo
.env
venv/

# Node.js
node_modules/

# IDE ayarları
.vscode/
.idea/

# Geçici dosyalar
*.tmp
*.log
EOF

# Commit et
git add .gitignore
git commit -m ".gitignore eklendi"
git push

# ⚠️ Eğer dosya ZATEN commit edilmişse .gitignore EKLENDİKTEN SONRA
#    onu cache'den silmen lazım:
git rm --cached .DS_Store
git commit -m ".DS_Store git takibinden çıkarıldı"
git push

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.11 — Takım Arkadaşımın Branch'ini Locale Çekmek İstiyorum
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Arkadaşın "mehmet" branch'inde güzel bir kod yazmış,
#        sen de görmek/denemek istiyorsun.

# Adım 1: Remote branch'leri güncelle
git fetch origin

# Adım 2: Arkadaşın branch'ine geç
git checkout mehmet
# veya
git checkout -b mehmet origin/mehmet

# Adım 3: İncelemeyi bitirdikten sonra kendi branch'ine dön
git checkout kadir

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.12 — Pull Request (PR) Açmam Lazım
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Ödevini bitirdin, kendi branch'ine push ettin.
#        Şimdi hocanın görmesi için PR açman lazım.

# Adım 1: Tüm değişiklikleri push et
git push

# Adım 2: Tarayıcıda GitHub'a git
#   https://github.com/SEAI-007/CS

# Adım 3: Sarı banner'ı gör
#   "kadir had recent pushes — Compare & pull request"
#   Bu butona tıkla

# Adım 4: PR bilgilerini doldur
#   Title: "Kadir - Hafta 5 Linear Data Structures"
#   Description: Ne yaptığını kısaca açıkla
#   base: main  ←  compare: kadir

# Adım 5: "Create pull request" butonuna tıkla

# ✅ PR açıldı! Hoca inceleyip merge edecek.

# VEYA terminal'den (GitHub CLI kuruluysa):
gh pr create --title "Kadir - Hafta 5" --body "Ödev tamamlandı"

# ═══════════════════════════════════════════════════════════════════
# SENARYO 7.13 — Büyük Bir Dosyayı Yanlışlıkla Commit Ettim
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: 100MB'lık bir video/veri dosyasını yanlışlıkla commit ettin.
#        GitHub bunu kabul etmeyecek (100MB limit).

# HENÜZ PUSH YAPMADIYSAN:
# Son commit'i geri al:
git reset --soft HEAD~1

# Büyük dosyayı .gitignore'a ekle:
echo "buyuk-dosya.zip" >> .gitignore

# Tekrar commit et (büyük dosya olmadan):
git add .
git commit -m "büyük dosya çıkarıldı, .gitignore güncellendi"
git push

# PUSH YAPTIYSAN:
# Dosyayı geçmişten tamamen silmek lazım (karmaşık):
# Bu durumda benden yardım iste!


######################################################################
#                                                                    #
#                    BÖLÜM 8 — HATA ÇÖZME REHBERİ                   #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# HATA 8.1 — fatal: not a git repository
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Git repo'su olan bir klasörde değilsin.
# NEDEN OLUR: Yanlış klasördesin veya henüz clone yapmamışsın.
#
# ÇÖZÜM:
pwd                    # Neredesin kontrol et
ls -la                 # .git klasörü var mı bak
cd ~/Desktop/CS        # Doğru klasöre git
git status             # Tekrar dene

# ═══════════════════════════════════════════════════════════════════
# HATA 8.2 — error: failed to push some refs
# ═══════════════���═══════════════════════════════════════════════════
#
# NE ANLAMA GELİR: GitHub'da sende olmayan değişiklikler var.
# NEDEN OLUR: Başkası (veya sen web'den) bir şey push etmiş.
#
# ÇÖZÜM:
git pull origin main     # Önce çek
git push                 # Sonra gönder

# ═══════════════════════════════════════════════════════════════════
# HATA 8.3 — CONFLICT (content): Merge conflict
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Aynı dosyanın aynı satırı farklı şekilde değiştirilmiş.
# NEDEN OLUR: Sen ve başkası aynı yeri düzenlemiş.
#
# ÇÖZÜM: SENARYO 7.6'ya bak (detaylı anlatıldı)

# ═══════════════════════════════════════════════════════════════════
# HATA 8.4 — fatal: refusing to merge unrelated histories
# ══════════════════════════════════════════════════════���════════════
#
# NE ANLAMA GELİR: İki repo'nun geçmişi birbiriyle bağlantılı değil.
# NEDEN OLUR: Farklı zamanlarda oluşturulmuş repolar birleştirilmeye çalışılıyor.
#
# ÇÖZÜM:
git pull origin main --allow-unrelated-histories
# Conflict varsa çöz, sonra:
git add .
git commit -m "unrelated histories birleştirildi"
git push

# ═══════════════════════════════════════════════════════════════════
# HATA 8.5 — Permission denied (publickey)
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: SSH key'in GitHub'a tanımlı değil veya yanlış.
# NEDEN OLUR: SSH key oluşturmadın veya GitHub'a eklemedin.
#
# KONTROL:
ssh -T git@github.com
# Eğer "Permission denied" diyorsa:

# ÇÖZÜM: BÖLÜM 2.3'e git ve SSH key'i baştan kur.
# Veya geçici olarak HTTPS'e geç:
git remote set-url origin https://github.com/SEAI-007/CS.git

# ═══════════════════════════════════════════════════════════════════
# HATA 8.6 — remote: Support for password authentication was removed
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: GitHub artık şifre ile push'u kabul etmiyor.
# NEDEN OLUR: HTTPS kullanıyorsun ve token ayarlamadın.
#
# ÇÖZÜM (en kolay): SSH'a geç
git remote set-url origin git@github.com:SEAI-007/CS.git

# ALTERNATİF: GitHub CLI kur
brew install gh
gh auth login

# ═══════════════════════════════════════════════════════════════════
# HATA 8.7 — error: Your local changes would be overwritten by merge
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Commit etmediğin değişiklikler var, pull yapamıyorsun.
# NEDEN OLUR: Dosya değiştirdin ama commit yapmadan pull yapıyorsun.
#
# ÇÖZÜM A: Commit et, sonra pull yap
git add .
git commit -m "devam eden çalışma"
git pull origin main

# ÇÖZÜM B: Geçici sakla, pull yap, geri getir
git stash
git pull origin main
git stash pop

# ═══════════════════════════════════════════════════════════════════
# HATA 8.8 — fatal: failed to get: -128 (credential helper hatası)
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Git şifre yöneticisi (credential helper) çalışamadı.
# NEDEN OLUR: HTTPS ile clone yaptın ama SSH key kurmuşsun.
#
# ⚠️ ÖNEMLİ: Bu hata genelde push'u ENGELLEMEZ! Arka planda
#    hata verir ama push çoğunlukla başarılı olur.
#
# KALICI ÇÖZÜM: SSH'a geç
git remote set-url origin git@github.com:SEAI-007/CS.git
# Bu hata bir daha gelmeyecek ✅

# ═══════════════════════════════════════════════════════════════════
# HATA 8.9 — error: pathspec 'branch-name' did not match
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Geçmeye çalıştığın branch yok.
# NEDEN OLUR: Branch adını yanlış yazdın veya branch henüz oluşturulmadı.
#
# ÇÖZÜM:
# 1. Mevcut branch'leri kontrol et:
git branch -a

# 2. Branch adını doğru yaz:
git checkout kadir          # local branch
git checkout -b yeni-branch # yeni oluştur

# 3. Remote branch'i çek:
git fetch origin
git checkout remote-branch-adi

# ═══════════════════════════════════════════════════════════════════
# HATA 8.10 — detached HEAD state
# ═══════════════════════════════════════════════════════════════════
#
# NE ANLAMA GELİR: Bir branch'te değilsin, eski bir commit'tesin.
# NEDEN OLUR: git checkout <commit-hash> yaptın veya yanlışlıkla eski commit'e geçtin.
#
# Şöyle bir uyarı görürsün:
#   You are in 'detached HEAD' state...
#
# ÇÖZÜM:
git checkout kadir     # Branch'ine geri dön

# Eğer detached HEAD'deyken değişiklik yaptıysan:
git checkout -b gecici-branch    # Değişiklikleri yeni branch'e kaydet
git checkout kadir               # Branch'ine geç
git merge gecici-branch          # Değişiklikleri al
git branch -d gecici-branch      # Geçici branch'i sil

# ═══════════════════════════════════════════════════════════════════
# GENEL HATA ÇÖZME STRATEJİSİ
# ═══════════════════════════════════════════════════════════════════
#
# Git'te hata aldığında şu adımları takip et:
#
# 1. HATA MESAJINI OKU (ciddi ciddi oku, Git genelde çözümü de söyler)
# 2. git status yap (her zaman ilk bu)
# 3. git branch yap (doğru yerde misin?)
# 4. git remote -v yap (doğru repo'ya mı bağlısın?)
# 5. Hata mesajını Google'a yapıştır
# 6. Stack Overflow'da çözümü bul
# 7. Hala çözülemediyse → AI mentor'a sor
#
# ⚠️ ASLA YAPMA:
#   - .git klasörünü silme!
#   - git reset --hard (emin değilsen)
#   - Proje klasörünü silip tekrar clone atma (son çare olmalı)
#


######################################################################
#                                                                    #
#                    BÖLÜM 9 — FAYDALI KOMUTLAR                     #
#                    VE İPUÇLARI                                     #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 9.1 — git log — Commit Geçmişini Gör
# ═══════════════════════════════════════════════════════════════════

# Kısa ve öz:
git log --oneline
# Çıktı:
# abc1234 son commit mesajı
# def5678 önceki commit
# ghi9012 ilk commit

# Görsel branch yapısı (çok güzel!):
git log --oneline --graph --all
# Çıktı:
# * abc1234 (HEAD -> kadir) benim commit'im
# | * xyz789 (origin/main) hocanın commit'i
# |/
# * def5678 ortak geçmiş

# Son 5 commit:
git log --oneline -5

# ═══════════════════════════════════════════════════════════════════
# 9.2 — git diff — Değişiklikleri Gör
# ═══════════════════════════════════════════════════════════════════

# Henüz add yapılmamış değişiklikleri gör:
git diff

# Add yapılmış (staged) değişiklikleri gör:
git diff --staged

# İki branch arasındaki farkı gör:
git diff main..kadir

# ═══════════════════════════════════════════════════════════════════
# 9.3 — git stash — Değişiklikleri Geçici Sakla
# ═══════════════════════════════════════════════════════════════════
#
# DURUM: Bir şey üzerinde çalışıyorsun ama acil olarak
#        başka branch'e geçmen lazım. Commit yapmak istemiyorsun.

# Değişiklikleri geçici olarak sakla:
git stash
# Çıktı: Saved working directory and index state WIP on kadir: abc1234...

# Başka branch'e geç, işini yap:
git checkout main
# ... işini yap ...
git checkout kadir

# Sakladığın değişiklikleri geri getir:
git stash pop

# Stash listesini gör:
git stash list

# ═══════════════════════════════════════════════════════════════════
# 9.4 — git reset vs git revert — Fark Ne?
# ═══════════════════════════════════════════════════════════════════
#
# ┌─────────────────────────────────────────────────────────────┐
# │  git reset                  │  git revert                  │
# │─────────────────────────────│──────────────────────────────│
# │  Commit'i SİLER             │  Yeni commit ile GERİ ALIR  │
# │  Geçmişi değiştirir         │  Geçmişi korur              │
# │  Push yapmadıysan kullan    │  Push yaptıysan kullan      │
# │  Tehlikeli (dikkatli ol)    │  Güvenli                     │
# └─────────────────────────────────────────────────────────────┘
#
# KURAL: Push yaptıysan → revert kullan
#        Push yapmadıysan → reset kullanabilirsin

# reset (push yapmadan önce):
git reset --soft HEAD~1    # Son commit'i geri al, dosyalar staged kalır

# revert (push yaptıktan sonra):
git revert HEAD            # Son commit'i yeni commit ile geri al
git push

# ═══════════════════════════════════════════════════════════════════
# 9.5 — .gitignore Nasıl Çalışır?
# ═══════════════════════════════════════════════════════════════════
#
# .gitignore dosyası proje kök dizininde olur.
# İçine yazdığın dosya/klasörler Git tarafından GÖRÜNMEZ olur.
#
# KURALLAR:
#   dosya.txt        → bu dosyayı yoksay
#   *.log            → .log ile biten TÜM dosyaları yoksay
#   klasor/          → bu klasörü yoksay
#   !onemli.log      → bu dosyayı YOKSAYMA (istisna)
#   **/temp           → herhangi bir yerdeki temp klasörünü yoksay
#
# ⚠️ .gitignore sadece HENÜZ TAKİP EDİLMEYEN dosyalar için çalışır!
#    Zaten commit edilmiş dosyayı yoksaymak için:
git rm --cached dosya.txt    # Git takibinden çıkar (dosyayı silmez)

# ═══════════════════════════════════════════════════════════════════
# 9.6 — git fetch vs git pull — Fark Ne?
# ═══════════════════════════════════════════════════════════════════
#
# ┌─────────────────────────────────────────────────────────────┐
# │  git fetch                  │  git pull                    │
# │─────────────────────────────│──────────────────────────────│
# │  Bilgileri İNDİRİR          │  İndirir + BİRLEŞTİRİR      │
# │  Dosyalarını DEĞİŞTİRMEZ   │  Dosyalarını GÜNCELLER       │
# │  Güvenli (sadece bakar)     │  Conflict çıkabilir          │
# │  "Ne değişmiş?" diye bakmak │  "Güncelle" demek            │
# └─────────────────────────────────────────────────────────────┘
#
# Kısaca: git pull = git fetch + git merge

git fetch origin          # "Bak ama dokunma"
git pull origin main      # "Güncelle"


######################################################################
#                                                                    #
#                    BÖLÜM 10 — PULL REQUEST (PR) REHBERİ           #
#                                                                    #
######################################################################

# ═════════════���═════════════════════════════════════════════════════
# 10.1 — PR Nedir, Neden Açarız?
# ═══════════════════════════════════════════════════════════════════
#
# Pull Request = "Benim branch'imi main'e birleştir" talebi.
#
# NEDEN PR?
# 1. Kod kontrolü → Hoca/takım değişiklikleri inceler
# 2. Tartışma    → Yorum yapılabilir, soru sorulabilir
# 3. Güvenlik    → Hatalı kod direkt main'e girmez
# 4. Kayıt       → Kim ne yaptı, hepsi kayıtlı
#
# AKIŞ:
#   Branch'te çalış → Push et → PR aç → İnceleme → Merge
#

# ═══════════════════════════════════════════════════════════════════
# 10.2 — PR Nasıl Açılır (Adım Adım)
# ═══════════════════════════════════════════════════════════════════
#
# ÖN KOŞUL: Branch'ine push yapmış olmalısın!

# Terminal'den:
git push -u origin kadir

# Sonra tarayıcıda:
# 1. https://github.com/SEAI-007/CS adresine git
# 2. "Compare & pull request" butonunu gör (sarı banner)
# 3. Tıkla
# 4. Bilgileri doldur:
#    ┌──────────────────────────────────────────────┐
#    │  base: main       ←  compare: kadir          │
#    │                                              │
#    │  Title: Kadir - Week 5 Homework              │
#    │                                              │
#    │  Description:                                │
#    │  - Linked list implementasyonu yapıldı       │
#    │  - Binary search eklendi                     │
#    │  - Test dosyaları eklendi                    │
#    └──────────────────────────────────────────────┘
# 5. "Create pull request" butonuna tıkla
# 6. ✅ PR açıldı!

# ═══════════════════════════════════════════════════════════════════
# 10.3 — PR Merge Edildikten Sonra Ne Yapılır?
# ═══════════════════════════════════════════════════════════════════

# Hoca PR'ı merge etti. Şimdi:

# 1. main branch'e geç
git checkout main

# 2. Güncellemeleri çek
git pull origin main

# 3. Eski branch'i sil (isteğe bağlı)
git branch -d kadir

# 4. Yeni iş için yeni branch oluştur
git checkout -b kadir/week-6

# ✅ Temiz başlangıç!


######################################################################
#                                                                    #
#                    BÖLÜM 11 — TAKIM ÇALIŞMASI KURALLARI           #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 11.1 — Altın Kurallar
# ═══════════════════════════════════════════════════════════════════
#
# 1. ❌ main branch'e DİREKT push YAPMA!
#    ✅ Kendi branch'inde çalış, PR aç
#
# 2. ❌ Tek büyük commit yapma!
#    ✅ Küçük, anlamlı commit'ler yap
#
# 3. ❌ "fix" "update" "asdf" commit mesajı yazma!
#    ✅ "binary search fonksiyonu eklendi" gibi açıklayıcı yaz
#
# 4. ❌ Push'tan önce pull yapmayı UNUTMA!
#    ✅ Her zaman önce pull, sonra push
#
# 5. ❌ Conflict çıkınca panik yapma!
#    ✅ Dosyayı aç, düzenle, commit et
#
# 6. ❌ .git klasörünü silme!
#    ✅ Sorun varsa komutlarla çöz
#
# 7. ❌ Büyük dosyaları (video, zip, data) commit etme!
#    ✅ .gitignore'a ekle


######################################################################
#                                                                    #
#                    BÖLÜM 12 — HIZLI REFERANS                      #
#                    (CHEAT SHEET)                                   #
#                                                                    #
######################################################################

# ═══════════════════════════════════════════════════════════════════
# 12.1 — En Çok Kullanılan 20 Komut
# ═══════════════════════════════════════════════════════════════════
#
# ┌────┬──────────────────────────────────┬─────────────────────────────────┐
# │ #  │ KOMUT                            │ NE YAPAR?                       │
# │────│──────────────────────────────────│─────────────────────────────────│
# │ 1  │ git clone <url>                  │ Repo'yu indir                   │
# │ 2  │ git status                       │ Durumu göster                   │
# │ 3  │ git add .                        │ Tüm değişiklikleri hazırla      │
# │ 4  │ git commit -m "mesaj"            │ Değişiklikleri kaydet           │
# │ 5  │ git push                         │ GitHub'a gönder                 │
# │ 6  │ git pull origin main             │ GitHub'dan çek                  │
# │ 7  │ git checkout -b branch-adi       │ Yeni branch oluştur ve geç     │
# │ 8  │ git checkout branch-adi          │ Branch'e geç                    │
# │ 9  │ git branch                       │ Branch listesi                  │
# │ 10 │ git branch -a                    │ Tüm branch'ler (remote dahil)  │
# │ 11 │ git log --oneline                │ Commit geçmişi (kısa)          │
# │ 12 │ git log --oneline --graph --all  │ Görsel branch yapısı           │
# │ 13 │ git diff                         │ Değişiklikleri göster           │
# │ 14 │ git stash                        │ Değişiklikleri geçici sakla     │
# │ 15 │ git stash pop                    │ Saklananları geri getir         │
# │ 16 │ git remote -v                    │ Remote bağlantıyı göster       │
# │ 17 │ git fetch origin                 │ Remote'u kontrol et             │
# │ 18 │ git reset --soft HEAD~1          │ Son commit'i geri al            │
# │ 19 │ git revert HEAD                  │ Son commit'i geri al (güvenli)  │
# │ 20 │ git rm --cached dosya            │ Dosyayı takipten çıkar          │
# └────┴──────────────────────────────────┴─────────────────────────────────┘

# ═══════════════════════════════════════════════════════════════════
# 12.2 — Günlük Rutin Özeti
# ═══════════════════════════════════════════════════════════════════
#
# ┌─────────────────────────────────────────────────────────────────┐
# │                                                                 │
# │   ☀️  SABAH                                                     │
# │   ├── cd ~/Desktop/CS                                          │
# │   ├── git checkout kadir                                       │
# │   ├── git pull origin main                                     │
# │   └── git status                                               │
# │                                                                 │
# │   💻  ÇALIŞMA                                                   │
# │   ├── (kodla, dosya ekle, düzenle)                             │
# │   ├── git status (ara ara kontrol et)                          │
# │   └── (küçük adımlarda commit yapabilirsin)                    │
# │                                                                 │
# │   🌙  AKŞAM                                                     │
# │   ├── git status                                               │
# │   ├── git add .                                                │
# │   ├── git commit -m "bugün ne yaptım"                         │
# │   └── git push                                                 │
# │                                                                 │
# │   📋  ÖDEV BİTTİĞİNDE                                          │
# │   └── GitHub'da Pull Request aç                                │
# │                                                                 │
# └─────────────────────────────────────────────────────────────────┘

# ═══════════════════════════════════════════════════════════════════
# 12.3 — Acil Durum Komutları (SOS!)
# ═══════════════════════════════════════════════════════════════════
#
# 🆘 "Neredeyim?"
git status && git branch && git remote -v
#
# 🆘 "Her şeyi geri almak istiyorum!" (commit yapmadıysan)
git checkout -- .
#
# 🆘 "Son commit'i geri al!" (push yapmadıysan)
git reset --soft HEAD~1
#
# 🆘 "Branch'ler karıştı, main'e döneyim"
git stash
git checkout main
git pull origin main
#
# 🆘 "Hiçbir şey çalışmıyor, sıfırdan başlayım"
cd ..
rm -rf CS
git clone git@github.com:SEAI-007/CS.git
cd CS
git checkout -b kadir
# ⚠️ Bu SON ÇARE! Push etmediğin değişiklikler kaybolur!

######################################################################
#                                                                    #
#         🎓 TEBRİKLER! Bu rehberi okuyan biri Git'in                #
#         %90'ını biliyor demektir. Gerisi pratikle gelir.           #
#                                                                    #
#         Unutma: Hata yapmak öğrenmenin parçası.                    #
#         Git'te neredeyse her şey geri alınabilir.                  #
#         PANİK YAPMA, git status YAP! 😄                            #
#                                                                    #
######################################################################