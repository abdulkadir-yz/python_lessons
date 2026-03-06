# ==============================================================================
#
#   🐙 GIT & GITHUB — TAM REHBER
#   MacBook M4 Pro için hazırlanmıştır
#   Güncel versiyon: Git 2.53.0 (Şubat 2026)
#
#   ╔══════════════════════════════════════════════════════════╗
#   ║  BÖLÜM 1:  Git Nedir? Neden Var?                        ║
#   ║  BÖLÜM 2:  Temel Kavramlar (origin, main, branch...)    ║
#   ║  BÖLÜM 3:  Kurulum & İlk Ayarlar (Mac M4)              ║
#   ║  BÖLÜM 4:  Temel Komutlar (Her Gün Kullandıkların)      ║
#   ║  BÖLÜM 5:  Branch — Dal Yönetimi                        ║
#   ║  BÖLÜM 6:  Remote — Uzak Repo İşlemleri                 ║
#   ║  BÖLÜM 7:  Merge & Rebase                               ║
#   ║  BÖLÜM 8:  Geri Alma Teknikleri                         ║
#   ║  BÖLÜM 9:  CASE SENARYOLARI (Gerçek Hayat)              ║
#   ║  BÖLÜM 10: Yaygın HATALAR & ÇÖZÜMLER                    ║
#   ║  BÖLÜM 11: Profesyonel İpuçları                         ║
#   ║  BÖLÜM 12: Hızlı Referans Tablosu                       ║
#   ╚══════════════════════════════════════════════════════════╝
#
#   NOT: Bu dosyadaki komutlar Terminal'de çalıştırılır.
#        # ile başlayan satırlar YORUM'dur — Terminal'de çalıştırma.
#        $ ile başlayan satırlar KOMUT'tur — $ işaretini yazma, sadece sonrasını.
#
# ==============================================================================


# ==============================================================================
# BÖLÜM 1: GİT NEDİR? NEDEN VAR?
# ==============================================================================
#
# ── PROBLEMİ ANLAYALIM ───────────────────────────────────────────────────────
#
# Hiç şöyle bir şey yaşadın mı?
#
#   proje_v1.py
#   proje_v2.py
#   proje_v2_final.py
#   proje_v2_final_GERCEKTEN_FINAL.py
#   proje_v2_son_hali_BUNU_KULLAN.py
#
# Ya da takım arkadaşınla aynı dosyayı aynı anda düzenleyip birbirinizin
# değişikliklerini sildiniz mi?
#
# ── GİT'İN ÇÖZÜMÜ ────────────────────────────────────────────────────────────
#
# Git = Dağıtık Versiyon Kontrol Sistemi
#
# Ne yapar?
#   1. Her değişikliği ZAMANDAMGASIyla kaydeder (commit)
#   2. İstediğin zaman geçmişe dönebilirsin
#   3. Birden fazla "paralel evren" yaratabilirsin (branch)
#   4. Takım arkadaşlarının değişiklikleriyle birleştirebilirsin (merge)
#   5. "Kimin ne zaman ne değiştirdiğini" görebilirsin (blame/log)
#
# ── GİT ≠ GİTHUB ─────────────────────────────────────────────────────────────
#
# Git     = Araç (version control software) — bilgisayarında çalışır
# GitHub  = Platform (bulut servis)         — git repo'larını internet'te barındırır
#
# Analoji:
# Git    = Kelime işlemci (Word)
# GitHub = Google Drive (dosyaları bulutta saklar, paylaşmanı sağlar)
#
# Alternatifler: GitLab, Bitbucket (GitHub gibi platformlar)
# Ama sektörde STANDART = GitHub
#
# ── GİT NASIL ÇALIŞIR? (3 Bölge Modeli) ─────────────────────────────────────
#
#   ┌─────────────────┐    git add     ┌──────────────┐    git commit    ┌──────────────┐
#   │  WORKING DIR    │ ─────────────► │ STAGING AREA │ ──────────────► │  REPOSITORY  │
#   │  (çalışma alan) │                │  (sahne)     │                  │  (.git klas.)│
#   └─────────────────┘                └──────────────┘                  └──────────────┘
#         ↑                                                                     │
#         │                                git checkout / git restore           │
#         └─────────────────────────────────────────────────────────────────────┘
#
# Working Dir  → Dosyaları düzenlediğin yer. Normal klasörün.
# Staging Area → "Bu değişiklikleri commit'e dahil edeceğim" diye işaretlediğin yer.
#                Fotoğraf çekmeden önce pozisyon alma gibi. (git add ile buraya taşırsın)
# Repository   → Commit'lerin kalıcı olarak saklandığı yer. (.git klasörü)
#                Buraya bir kez commit'lersen, neredeyse geri dönmek mümkün.
#
# ── YEREL (LOCAL) vs UZAK (REMOTE) ───────────────────────────────────────────
#
# Local  = Kendi bilgisayarındaki repo
# Remote = GitHub'daki (internetteki) repo
#
# git push → Local'den Remote'a gönder
# git pull → Remote'dan Local'e al


# ==============================================================================
# BÖLÜM 2: TEMEL KAVRAMLAR
# ==============================================================================
#
# ── REPOSITORY (REPO) ─────────────────────────────────────────────────────────
# Projenin tüm dosyaları + değişiklik geçmişi = Repo
# .git adlı gizli bir klasör içinde saklanır.
# $ ls -la komutuyla .git klasörünü görebilirsin.
#
# ── COMMIT ────────────────────────────────────────────────────────────────────
# Anlık fotoğraf (snapshot). "Bu değişiklikleri kalıcı olarak kaydet" demek.
# Her commit'in benzersiz bir SHA hash'i vardır: a3f8c2d...
# Her commit mesajı var: "Login sayfası eklendi"
# Her commit kim yaptı, ne zaman yaptı bilgisini taşır.
#
# ── BRANCH (DAL) ──────────────────────────────────────────────────────────────
# Paralel geliştirme hattı. "Yan çalışma alanı" gibi.
#
# Neden var?
# Senaryo: Ana proje çalışıyor. Sen yeni özellik geliştiriyorsun.
# Direkt main'de geliştirirsen → yarım iş canlıya çıkabilir → felaket!
# Branch açarsın → orada dener, geliştirirsin → hazır olunca main'e birleştirirsin.
#
#   main ──── A ──── B ──── C ──────────────── G (merge)
#                     \                       /
#   feature-login      D ──── E ──── F ──────
#
# A, B, C, D... = commitler
# main'de C'desin. Ama feature-login branch'inde F'ye kadar gidip test ettin.
# Hazır olunca G commit'iyle main'e merge ettin.
#
# ── MAIN (eski adı MASTER) ────────────────────────────────────────────────────
# Varsayılan/ana branch. "Canlı kod" buradadır.
# GitHub 2020'de "master"dan "main"e geçti.
# Git 2.52+ artık varsayılan olarak "main" kullanıyor.
# Eski repolarda hâlâ "master" görebilirsin.
#
# ── ORIGIN ────────────────────────────────────────────────────────────────────
# Remote repo'nun kısa adı (alias).
# "origin" = GitHub'daki reponun URL'ine verilen varsayılan takma isim.
#
# Şöyle düşün:
# "origin" yerine her seferinde tam URL yazabilirdin:
#   git push https://github.com/kullanici/repo.git main
# Ama "origin" dersen kısa yoldan:
#   git push origin main
#
# Birden fazla remote olabilir:
#   origin    → kendi fork'un (github.com/benn/proje)
#   upstream  → orijinal repo (github.com/baskafirma/proje)
#
# ── HEAD ──────────────────────────────────────────────────────────────────────
# "Şu an neredesin?" işaretçisi.
# Hangi branch'in hangi commit'indesin? HEAD orayı gösterir.
# Normally HEAD → branch adını → en son commit
# "Detached HEAD" = HEAD direkt bir commit'i gösteriyor (branch yok)
#
# ── MERGE vs REBASE ───────────────────────────────────────────────────────────
# İkisi de branch'leri birleştirme yöntemi. Fark:
# Merge  → İki dalı birleştirir, tarihi OLDUĞU GİBİ korur (merge commit ekler)
# Rebase → Bir dalın commitlerini başka bir dalın üstüne TAŞİR (temiz tarih)
#
# ── PULL REQUEST (PR) / MERGE REQUEST (MR) ────────────────────────────────────
# "Bu branch'i main'e birleştir" talebi. GitHub üzerinden açılır.
# Takım arkadaşların kodu inceler (code review), onaylarsa merge edilir.
# Bu sektörün STANDART çalışma şekli.
#
# ── FORK ──────────────────────────────────────────────────────────────────────
# Başkasının reposunu kendi GitHub hesabına kopyalamak.
# Orijinal repoya doğrudan yazma iznin yok ama fork'una yazabilirsin.
# Değişiklikleri orijinale göndermek için Pull Request açarsın.
#
# ── CLONE ─────────────────────────────────────────────────────────────────────
# Remote repo'yu local'e indirmek. Tek seferlik işlem.
# "git clone URL" → tüm dosyalar + tüm geçmiş local'e gelir.


# ==============================================================================
# BÖLÜM 3: KURULUM & İLK AYARLAR (MacBook M4 Pro)
# ==============================================================================

# ─── ADIM 1: Git Yüklü mü Kontrol Et ────────────────────────────────────────
$ git --version
# git version 2.53.0 (en güncel)
# Eğer eski sürümse güncelle:

# ─── ADIM 2: Homebrew ile Git Güncelle (M4 için önerilen) ───────────────────
# Homebrew Mac'in paket yöneticisi — yoksa önce yükle:
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git yükle / güncelle:
$ brew install git
# veya güncelle:
$ brew upgrade git

# Homebrew Git'in öncelikli kullanılması için (M4 Apple Silicon):
# ~/.zshrc dosyasına şunu ekle:
# export PATH="/opt/homebrew/bin:$PATH"

# ─── ADIM 3: Git Kimliğini Tanıt (BİR KEZ YAPILIR) ──────────────────────────
# Bu bilgiler her commit'e otomatik eklenir.
# GitHub hesabındaki isim ve email ile aynı olsun!

$ git config --global user.name "Benn Yılmaz"
$ git config --global user.email "benn@example.com"

# --global → tüm projeler için geçerli
# --local  → sadece bu proje için geçerli (farklı iş/kişisel hesaplar için)

# Varsayılan branch adını "main" yap (Git 2.52+ default ama garanti ol):
$ git config --global init.defaultBranch main

# Terminal çıktılarını renkli göster:
$ git config --global color.ui auto

# Varsayılan editörü VS Code yap:
$ git config --global core.editor "code --wait"

# Ayarları kontrol et:
$ git config --list
$ git config --global --list   # sadece global ayarlar

# ─── ADIM 4: SSH Key Oluştur (GitHub için — HTTPS yerine SSH önerilen) ───────
# Neden SSH? Her push/pull'da şifre sormaz. Daha güvenli.

# Yeni SSH key oluştur (email = GitHub email'in):
$ ssh-keygen -t ed25519 -C "benn@example.com"
# Soruları: Enter (varsayılan konum), şifre belirleyebilirsin (opsiyonel)

# SSH agent'a ekle:
$ eval "$(ssh-agent -s)"
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519
# Mac Keychain'e kaydeder → her açılışta otomatik yüklenir

# Public key'i kopyala:
$ pbcopy < ~/.ssh/id_ed25519.pub
# → GitHub.com → Settings → SSH and GPG keys → New SSH key → Paste

# Bağlantıyı test et:
$ ssh -T git@github.com
# "Hi benn! You've successfully authenticated" → ✅


# ==============================================================================
# BÖLÜM 4: TEMEL KOMUTLAR — Her Gün Kullandıkların
# ==============================================================================

# ─── YENİ REPO BAŞLATMAK ─────────────────────────────────────────────────────

# Mevcut klasörü Git reposu yap:
$ git init
# → .git klasörü oluşturulur. Artık bu klasör bir repo!
# Neden: Sıfırdan bir proje başlatırken kullanılır.

# Remote repo'yu local'e indir (clone):
$ git clone git@github.com:kullanici_adi/repo_adi.git
# → repo_adi adlı klasör oluşturulur, içine tüm dosyalar indirilir
# Neden: Var olan bir projeye katılırken kullanılır.

# Belirli bir klasör adıyla clone:
$ git clone git@github.com:kullanici/repo.git benim-klasorum

# ─── DURUM KONTROLÜ ──────────────────────────────────────────────────────────

$ git status
# En sık kullanılan komut! Her şeyden önce bunu çalıştır.
# Gösterir: hangi dosyalar değişti, hangisi staged, hangisi untracked
#
# Çıktı örneği:
# On branch main
# Changes not staged for commit:
#   modified:   app.py        → değiştirildi, henüz staged değil
# Untracked files:
#   new_file.py               → yeni dosya, git bilmiyor

$ git status -s
# Kısa format: M = modified, A = added, ?? = untracked

# ─── DEĞİŞİKLİKLERİ İNCELEMEK ───────────────────────────────────────────────

$ git diff
# Working dir ile staging area arasındaki farkları göster
# Staged olmayan değişiklikleri gösterir
# Neden: "Neyi değiştirdim?" sorusuna cevap

$ git diff --staged
# Staging area ile son commit arasındaki farkları göster
# Staged edilmiş ama henüz commit'lenmemiş değişiklikler
# Neden: "Commit'e ne ekledim?" sorusuna cevap

$ git diff main..feature-login
# İki branch arasındaki farkları göster

# ─── STAGING (SAHNE) ─────────────────────────────────────────────────────────

$ git add dosya.py
# Belirli bir dosyayı stage et
# Neden: "Bu dosyadaki değişikliği commit'e dahil et"

$ git add klasor/
# Bir klasörün tüm içeriğini stage et

$ git add .
# Bulunduğun klasördeki TÜM değişiklikleri stage et
# ⚠️ Dikkat! Yanlışlıkla istemediğin dosyayı da ekleyebilirsin
# .gitignore ile hariç tutulacakları belirle (Bölüm 11'e bak)

$ git add -p
# Interaktif staging: Dosyayı parça parça (hunk) incele, "Bu kısmı ekleyeyim mi?"
# En profesyonel yol! Her değişikliği tek tek kontrol edersin.
# y = yes, n = no, s = split, ? = help

# Staging'den geri al (ama dosyayı değiştirme):
$ git restore --staged dosya.py
# Veya eski yol (hâlâ çalışır):
$ git reset HEAD dosya.py

# ─── COMMİT ──────────────────────────────────────────────────────────────────

$ git commit -m "Login sayfası eklendi"
# Staged değişiklikleri kalıcı olarak kaydet
# -m = mesaj (message)
# Neden: "Bu anı kaydet, açıklamam şu"

# Stage + Commit bir arada (YENİ dosyalar için çalışmaz, sadece tracked olanlar):
$ git commit -am "Hata düzeltildi"
# -a = all tracked files'ı otomatik stage et
# ⚠️ Sadece modified dosyalar için, yeni (untracked) dosyalar için değil!

# Detaylı mesaj (editörde):
$ git commit
# → VS Code açılır, çok satırlı commit mesajı yaz, kaydet ve kapat

# Son commit'i düzelt (henüz push etmediysen!):
$ git commit --amend -m "Düzeltilmiş mesaj"
# Veya mesajı değiştirmeden son commit'e dosya ekle:
$ git add unuttuğum_dosya.py
$ git commit --amend --no-edit
# ⚠️ SADECE push etmediğin commit'lerde kullan!

# ─── GEÇMİŞE BAKMAK ─────────────────────────────────────────────────────────

$ git log
# Tüm commit geçmişini göster (en yeniden en eskiye)
# q tuşuyla çık

$ git log --oneline
# Her commit tek satırda: a3f8c2d "Login sayfası eklendi"
# En kullanışlı format!

$ git log --oneline --graph --all
# Tüm branch'leri grafik olarak göster
# Harika! Branch yapısını görmek için ideal.

$ git log --oneline -10
# Son 10 commit

$ git log --author="Benn"
# Belirli kişinin commitleri

$ git log --since="2024-01-01" --until="2024-12-31"
# Tarih aralığına göre filtrele

$ git log dosya.py
# Belirli dosyanın geçmişi

$ git show a3f8c2d
# Belirli bir commit'in içeriğini göster


# ==============================================================================
# BÖLÜM 5: BRANCH — DAL YÖNETİMİ
# ==============================================================================
#
# Branch neden var? Tekrar anlayalım:
#
# Olmasa ne olurdu?
# → Herkes direkt main'de çalışır
# → Yarım kalan özellikler canlıya çıkar
# → Birinin değişikliği diğerinin çalışmasını bozar
# → Geri almak zor
#
# Branch sayesinde:
# → Her özellik kendi izole alanında gelişir
# → Test edilene kadar main'e gelmez
# → İstersen branch'i sil, main etkilenmez
#
# Sektörde yaygın branch isimlendirme:
# main / master   → canlı, kararlı kod
# develop         → bir sonraki sürüm için birleştirme noktası
# feature/xxx     → yeni özellik: feature/user-authentication
# bugfix/xxx      → hata düzeltme: bugfix/login-crash
# hotfix/xxx      → acil üretim düzeltmesi: hotfix/payment-error
# release/xxx     → sürüm hazırlık: release/v2.0
# ==============================================================================

# ─── BRANCH LISTELEME ─────────────────────────────────────────────────────────

$ git branch
# Local branch'leri listele (* = şu an hangi branch'tesin)

$ git branch -r
# Remote branch'leri listele

$ git branch -a
# Tüm branch'ler (local + remote)

$ git branch -v
# Branch'ler + son commit bilgisi

# ─── BRANCH OLUŞTURMA ─────────────────────────────────────────────────────────

$ git branch feature/login
# "feature/login" adlı branch oluştur (ama geçiş yapma)
# Neden: Yeni özellik geliştirmeden önce

$ git checkout -b feature/login
# Branch oluştur VE geç (eski yol, hâlâ yaygın)

$ git switch -c feature/login
# Branch oluştur VE geç (yeni yol, Git 2.23+, önerilen!)
# -c = create

$ git switch -c feature/login main
# main branch'inden yeni branch oluştur
# Neden: Her zaman güncel main'den branch almak istersin!

# ─── BRANCH DEĞİŞTİRME ───────────────────────────────────────────────────────

$ git switch main
# main branch'ine geç (yeni yol)

$ git checkout main
# main branch'ine geç (eski yol, hâlâ çalışır)

# ⚠️ Branch değiştirmeden önce değişikliklerini commit et veya stash'le!
# Aksi hâlde Git "uncommitted changes var" diye hata verebilir.

# ─── BRANCH SİLME ─────────────────────────────────────────────────────────────

$ git branch -d feature/login
# Branch'i sil (sadece merge edilmişse siler — güvenli)
# Neden: İşi biten branch'ler temizlenmeli

$ git branch -D feature/login
# ZORLA sil (merge edilmemiş olsa bile)
# ⚠️ Dikkat! Commit'ler kaybolabilir.

$ git push origin --delete feature/login
# Remote'daki branch'i de sil

# ─── BRANCH YENİDEN ADLANDIRMA ───────────────────────────────────────────────

$ git branch -m eski-isim yeni-isim
# Branch'i yeniden adlandır

# Şu an bulunduğun branch'i yeniden adlandır:
$ git branch -m yeni-isim


# ==============================================================================
# BÖLÜM 6: REMOTE — UZAK REPO İŞLEMLERİ
# ==============================================================================

# ─── REMOTE YÖNETİMİ ─────────────────────────────────────────────────────────

$ git remote
# Remote'ları listele (genellikle "origin" çıkar)

$ git remote -v
# Remote'ları URL'leriyle listele
# Çıktı: origin  git@github.com:benn/proje.git (fetch)
#        origin  git@github.com:benn/proje.git (push)

$ git remote add origin git@github.com:benn/proje.git
# Yeni remote ekle (genellikle ilk kez GitHub'a bağlarken)
# origin = takma isim, sonrasındaki = URL

$ git remote add upstream git@github.com:orijinal/proje.git
# Fork'ta çalışırken orijinal repoyu "upstream" olarak ekle

$ git remote remove origin
# Remote bağlantısını kaldır

$ git remote set-url origin git@github.com:benn/yeni-repo.git
# Remote URL'ini değiştir

# ─── PUSH — LOCAL'DEN REMOTE'A GÖNDER ───────────────────────────────────────

$ git push origin main
# Local main branch'ini remote origin'e gönder
# YAPI: git push [remote_adı] [branch_adı]

$ git push
# Kısa yol (upstream ayarlıysa)

$ git push -u origin feature/login
# Branch'i remote'a gönder VE upstream'i ayarla
# -u = --set-upstream → bir sonraki "git push" için "origin feature/login" hatırlanır
# İlk push'ta her zaman -u kullan!

$ git push origin --force
# ZORLA push (⚠️ çok tehlikeli! Remote geçmişin üzerine yazar)
# Ne zaman kullanılır? Sadece kendi feature branch'inde, rebase sonrası

$ git push origin --force-with-lease
# Daha güvenli force push
# "Remote'da benim bilmediğim commit varsa iptal et"
# Takım arkadaşının çalışmasını silmekten korur

# ─── PULL — REMOTE'DAN LOCAL'E ÇEK ──────────────────────────────────────────

$ git pull
# Remote'dan değişiklikleri çek VE merge et
# = git fetch + git merge (iki komutun kısayolu)

$ git pull origin main
# Spesifik remote ve branch'ten çek

$ git pull --rebase
# Çek ama merge yerine rebase yap
# Daha temiz tarih oluşturur, pro developers bunu tercih eder
# Kural olarak: git pull --rebase origin main

$ git fetch
# Remote'daki değişiklikleri indir AMA mevcut çalışmanla birleştirme
# Neden: Önce ne geldiğini görmek istiyorsun
# Sonra git log origin/main ile bakarsın, sonra merge/rebase kararı verirsin

$ git fetch --prune
# Remote'da silinmiş branch'leri local'den de temizle
# Remote'da olmayan branch'ler local listenden kaybolur


# ==============================================================================
# BÖLÜM 7: MERGE & REBASE
# ==============================================================================
#
# ── MERGE ─────────────────────────────────────────────────────────────────────
# İki branch'i birleştirir.
# Tarih korunur, merge commit eklenir.
# "Bu iki iş birleşti" açıkça görülür.
#
# NE ZAMAN: Pull request merge ederken, main'e feature eklerken
#
# ── REBASE ────────────────────────────────────────────────────────────────────
# Branch'teki commit'leri başka branch'in üstüne "taşır".
# Commit geçmişi düz/temiz görünür, merge commit olmaz.
# Tarih yeniden yazılır!
#
# NE ZAMAN: Feature branch'ini main'in son haliyle güncellerken
#           "Çalışırken main ilerledi, ben de main'in üstüne geçeyim"
# ==============================================================================

# ─── MERGE ────────────────────────────────────────────────────────────────────

# feature/login branch'ini main'e merge et:
$ git switch main              # önce main'e geç
$ git merge feature/login      # feature branch'ini getir
# → Fast-forward (main'de yeni commit yoksa) veya merge commit oluşur

$ git merge --no-ff feature/login
# Her zaman merge commit oluştur (fast-forward olsa bile)
# Neden: "Hangi özellik ne zaman merge edildi" geçmişte görülsün

$ git merge --squash feature/login
# Feature branch'teki TÜM commit'leri tek bir commit'e sıkıştır
# Sonra git commit -m "Feature login tamamlandı" yazmak gerekir
# Neden: 50 "düzeltme", "test", "xxx" commit'i main'e gelmesin, tek temiz commit gelsin

# ─── REBASE ───────────────────────────────────────────────────────────────────

# Feature branch'ini main'in üstüne taşı:
$ git switch feature/login     # feature branch'e geç
$ git rebase main              # main'in son commitlerini altına al

# İnteraktif rebase (son 3 commit'i düzenle):
$ git rebase -i HEAD~3
# → Editör açılır. Her commit için:
#   pick   = commit'i tut
#   reword = mesajı değiştir
#   edit   = commit içeriğini değiştir
#   squash = önceki commit'le birleştir
#   drop   = commit'i sil
# ⚠️ Push edilmemiş commit'lerde kullan!

# ─── CONFLICT (ÇAKIŞMA) ÇÖZME ────────────────────────────────────────────────
#
# Conflict nedir?
# Aynı dosyanın aynı satırını iki farklı branch değiştirdi.
# Git "hangisini alayım?" diyemez, sen karar vermelisin.
#
# Conflict olduğunda dosya içinde şunu görürsün:
#
#   <<<<<<< HEAD (current change)
#   def giris_yap():
#       return "Yeni login"
#   =======
#   def giris_yap():
#       return "Eski login"
#   >>>>>>> feature/login (incoming change)
#
# HEAD = senin mevcut branch'in
# feature/login = merge etmeye çalıştığın branch

# Conflict'i VS Code'da çözmek için:
$ code .   # VS Code aç → çakışan dosyalar kırmızı gösterilir
# VS Code: "Accept Current" / "Accept Incoming" / "Accept Both" seçenekleri
# Manuel de düzenleyebilirsin: <<<, ===, >>> satırlarını sil, istediğini bırak

# Conflict çözdükten sonra:
$ git add cakisan_dosya.py     # çözüldü diye işaretle
$ git commit                   # merge commit'i tamamla

# Conflict çıkınca "Dur, geri al" demek istersen:
$ git merge --abort            # merge işlemini iptal et
$ git rebase --abort           # rebase işlemini iptal et


# ==============================================================================
# BÖLÜM 8: GERİ ALMA TEKNİKLERİ
# ==============================================================================
#
# ⚠️ ALTIN KURAL:
# Push ETMEDİĞİN commit'leri değiştirebilirsin.
# Push ETTİĞİN commit'leri değiştirmek için force push gerekir → takımda tehlikeli!
# ==============================================================================

# ─── WORKING DIR'DAKİ DEĞİŞİKLİĞİ GERİ AL ────────────────────────────────────

# Bir dosyadaki değişikliği geri al (son commit'e döndür):
$ git restore dosya.py          # Yeni yol (Git 2.23+)
$ git checkout -- dosya.py      # Eski yol
# ⚠️ GERİ ALINAMAZ! Değişiklikler tamamen kaybolur.

# Tüm değişiklikleri geri al:
$ git restore .

# ─── STAGED DEĞİŞİKLİĞİ UNSTAGE ET ──────────────────────────────────────────

$ git restore --staged dosya.py  # Dosyayı staging'den çıkar (değişiklikler korunur)
$ git reset HEAD dosya.py        # Eski yol

# ─── COMMİT'İ GERİ AL ────────────────────────────────────────────────────────

# git revert → Yeni bir "geri alma" commit'i ekler. Geçmiş korunur. (GÜVENLİ)
$ git revert a3f8c2d             # O commit'in etkisini geri alan yeni commit yarat
$ git revert HEAD                # Son commit'i geri al
# Ne zaman: Push ettikten sonra geri almak için. Takım çalışmasında bu!

# git reset → Commit'leri "sanki olmamış gibi" siler. Geçmiş değişir. (TEHLİKELİ)
$ git reset --soft HEAD~1
# Son commit'i geri al → değişiklikler staging'de kalır
# Ne zaman: "Son commit mesajını değiştirmek istiyorum, dosyaları kaybetmeyeyim"

$ git reset --mixed HEAD~1
# Son commit'i geri al → değişiklikler working dir'de kalır (staging'den de çıkar)
# Varsayılan davranış

$ git reset --hard HEAD~1
# Son commit'i geri al → tüm değişiklikler KAYBOLUR
# ⚠️ En tehlikeli! Geri alınamaz (neredeyse).
# Ne zaman: "Son commit berbattı, sanki hiç yapmamış gibi olsun"

# HEAD~1 = bir önceki commit
# HEAD~3 = 3 commit öncesi
# a3f8c2d = spesifik commit hash'i

# ─── STASH — İŞİ SAKLA ───────────────────────────────────────────────────────
#
# Stash nedir?
# Yarım kalan değişikliklerini geçici olarak sakla.
# Senaryo: Feature geliştiriyorsun, acil bir bug fix gerekti.
# Commit etmeye hazır değil ama branch değiştirmen lazım.
# Stash → değişiklikler saklanır → branch değiştir → bug fix → geri al

$ git stash
# Değişiklikleri sakla (working dir + staging temizlenir)

$ git stash push -m "Login sayfası yarım kaldı"
# Açıklamalı stash (önerilenl)

$ git stash list
# Tüm stash'leri listele
# stash@{0}: WIP on feature/login: "Login sayfası yarım kaldı"
# stash@{1}: WIP on main: ...

$ git stash pop
# En son stash'i geri getir VE stash'ten sil

$ git stash apply stash@{1}
# Belirli stash'i getir ama stash'ten silme (tekrar kullanabilirsin)

$ git stash drop stash@{0}
# Belirli stash'i sil

$ git stash clear
# Tüm stash'leri sil

$ git stash branch feature/stashten-branch
# Stash'ten yeni branch oluştur (conflict riski varsa)

# ─── KAYBOLAN KOMMİT'İ KURTAR (git reflog) ──────────────────────────────────

$ git reflog
# "Git'teki tüm işlemlerin geçmişi" — kurtarma aracı
# git reset --hard yaptın ve pişman oldun? reflog ile kurtarabilirsin!
# Çıktı: a3f8c2d HEAD@{0}: reset: moving to HEAD~1
#        b7e9f1a HEAD@{1}: commit: "Login sayfası eklendi"

$ git reset --hard HEAD@{1}
# "HEAD@{1}'e geri dön" → kayıp commit geri gelir!
# reflog genellikle 30 gün saklar


# ==============================================================================
# BÖLÜM 9: CASE SENARYOLARI — Gerçek Hayat Durumları
# ==============================================================================

# ══════════════════════════════════════════════════════════════════════════════
# CASE 1: Sıfırdan Yeni Proje — GitHub'a Bağla
# Senaryo: Yeni bir Python projesi başlattın, GitHub'a yükleyeceksin.
# ══════════════════════════════════════════════════════════════════════════════

# 1. Lokal klasör oluştur ve git başlat:
$ mkdir benim-projem && cd benim-projem
$ git init
# → .git klasörü oluşturuldu

# 2. İlk dosyaları oluştur:
$ echo "# Benim Projem" > README.md
$ touch main.py
$ echo "__pycache__/\n*.pyc\n.env\nvenv/" > .gitignore

# 3. Stage ve commit:
$ git add .
$ git commit -m "İlk commit: Proje başlatıldı"

# 4. GitHub'da yeni repo oluştur:
# → github.com → New Repository → "benim-projem" → Create (README ekleme! Zaten var)

# 5. Remote bağla ve push et:
$ git remote add origin git@github.com:benn/benim-projem.git
$ git push -u origin main
# -u → ilk push'ta zorunlu. Sonraki push'larda sadece "git push" yeter.


# ══════════════════════════════════════════════════════════════════════════════
# CASE 2: Var Olan Repoya Katıl ve Çalışmaya Başla
# Senaryo: Şirkete yeni katıldın, mevcut projeye katkıda bulunacaksın.
# ══════════════════════════════════════════════════════════════════════════════

# 1. Repoyu clone et:
$ git clone git@github.com:sirket/ana-proje.git
$ cd ana-proje

# 2. Remote'ları kontrol et:
$ git remote -v
# → origin git@github.com:sirket/ana-proje.git

# 3. Mevcut branch'leri gör:
$ git branch -a

# 4. Main'in güncel olduğundan emin ol:
$ git switch main
$ git pull origin main

# 5. Yeni feature branch aç:
$ git switch -c feature/kullanici-profili
# Her zaman main'den branch al!

# 6. Çalış, commit'le:
$ git add .
$ git commit -m "feat: Kullanıcı profil sayfası eklendi"

# 7. Remote'a push et:
$ git push -u origin feature/kullanici-profili

# 8. GitHub'da Pull Request aç:
# → GitHub.com → Repo → "Compare & pull request" butonu
# → Açıklama yaz, reviewer ekle → Create Pull Request

# 9. Code review sonrası merge edilir. Branch silinir.
$ git switch main
$ git pull origin main                    # merge'i al
$ git branch -d feature/kullanici-profili # local branch'i sil


# ══════════════════════════════════════════════════════════════════════════════
# CASE 3: Feature Branch'te Çalışırken Main İlerledi
# Senaryo: 3 gündür feature branch'indesin. Bu arada main'e 10 commit geldi.
#          PR açmadan önce main ile senkronize olman gerekiyor.
# ══════════════════════════════════════════════════════════════════════════════

# Yöntem A: Rebase (önerilen — temiz geçmiş)
$ git switch feature/login
$ git fetch origin
$ git rebase origin/main
# → Senin commit'lerin, main'in en son commit'inin üstüne taşınır

# Conflict olursa:
$ git status                    # hangi dosyada conflict var?
# → Dosyayı aç, conflict'i çöz
$ git add cakisan_dosya.py
$ git rebase --continue         # devam et
# Sonraki conflict için tekrarla...
# Vazgeçmek istersen: git rebase --abort

# Rebase sonrası push (tarih değişti, force gerekir):
$ git push --force-with-lease origin feature/login
# --force-with-lease = güvenli force push

# Yöntem B: Merge (daha basit ama geçmiş karmaşıklaşır)
$ git switch feature/login
$ git merge origin/main
# → Merge commit oluşturulur


# ══════════════════════════════════════════════════════════════════════════════
# CASE 4: Acil Bug Fix — Hotfix Branch
# Senaryo: Canlıda kritik bir hata var! Hemen düzeltilmeli.
#          Ama sen başka bir feature üzerinde çalışıyorsun.
# ══════════════════════════════════════════════════════════════════════════════

# 1. Mevcut yarım işi sakla:
$ git stash push -m "Login sayfası yarım kaldı"

# 2. Ana branch'e geç ve güncelle:
$ git switch main
$ git pull origin main

# 3. Hotfix branch aç:
$ git switch -c hotfix/odeme-hatasi

# 4. Düzelt ve commit'le:
$ git add .
$ git commit -m "fix: Ödeme işleminde NullPointer hatası giderildi"

# 5. Main'e merge et:
$ git switch main
$ git merge --no-ff hotfix/odeme-hatasi
$ git push origin main

# 6. Tag ekle (sürüm işaretle):
$ git tag -a v1.0.1 -m "Hotfix: Ödeme hatası düzeltildi"
$ git push origin v1.0.1

# 7. Hotfix'i develop/feature branch'lerine de uygula:
$ git switch develop
$ git merge hotfix/odeme-hatasi
$ git push origin develop

# 8. Hotfix branch'ini sil:
$ git branch -d hotfix/odeme-hatasi
$ git push origin --delete hotfix/odeme-hatasi

# 9. Yarım kalan işe geri dön:
$ git switch feature/login
$ git stash pop


# ══════════════════════════════════════════════════════════════════════════════
# CASE 5: Yanlış Branch'e Commit Yaptım!
# Senaryo: main'deyken commit yaptın. Oysa feature/login'e yapmalıydın.
# ══════════════════════════════════════════════════════════════════════════════

# Durum: main branch'indesin, son commit yanlış yere gitti.

# 1. Son commit'in hash'ini al:
$ git log --oneline -3
# a3f8c2d "Yanlış commit"
# b7e9f1a "Doğru commit"

# 2. Doğru branch'e geç (veya oluştur):
$ git switch -c feature/login
# → feature/login, main'in mevcut durumunu (yanlış commit dahil) alır

# 3. Main'deki yanlış commit'i geri al:
$ git switch main
$ git reset --hard HEAD~1       # son commit'i sil (yanlış olan)
# main artık temiz

# 4. feature/login'de commit var, main'de yok — ✅
$ git switch feature/login
# → yanlış commit aslında doğru yerde!


# ══════════════════════════════════════════════════════════════════════════════
# CASE 6: Open Source Projeye Katkı (Fork Workflow)
# Senaryo: Başkasının GitHub reposuna katkı yapmak istiyorsun.
# ══════════════════════════════════════════════════════════════════════════════

# 1. GitHub'da repoyu fork et:
# → github.com/orijinal-kullanici/proje → Fork butonu → kendi hesabına kopyalanır

# 2. Fork'unu clone et:
$ git clone git@github.com:benn/proje.git
$ cd proje

# 3. Upstream'i ekle (orijinal repo):
$ git remote add upstream git@github.com:orijinal-kullanici/proje.git
$ git remote -v
# origin   → senin fork'un
# upstream → orijinal repo

# 4. Feature branch aç:
$ git switch -c feature/yeni-ozellik

# 5. Değişikliklerini yap, commit'le:
$ git commit -m "feat: Yeni özellik eklendi"

# 6. Fork'una push et:
$ git push origin feature/yeni-ozellik

# 7. GitHub'da Pull Request aç:
# → github.com/benn/proje → Compare & Pull Request
# → base: orijinal-kullanici/proje:main ← compare: benn/proje:feature/yeni-ozellik

# 8. Upstream güncellemelerini al (zaman içinde):
$ git fetch upstream
$ git switch main
$ git merge upstream/main
$ git push origin main


# ══════════════════════════════════════════════════════════════════════════════
# CASE 7: Commit Geçmişini Temizle (Interactive Rebase)
# Senaryo: Feature branch'inde 15 commit var: "deneme", "test", "xxx", "düzelt"
#          PR açmadan önce bunları 3 anlamlı commit'e dönüştürmek istiyorsun.
# ══════════════════════════════════════════════════════════════════════════════

$ git rebase -i HEAD~15
# → Editör açılır:
#
# pick a3f8c2d "Login formu oluşturuldu"
# pick b7e9f1a "deneme"
# pick c2d4e5f "test"
# pick d5e6f7a "xxx düzelt"
# pick e6f7a8b "Validasyon eklendi"
# ... 10 daha
#
# Şöyle düzenle:
# pick a3f8c2d "Login formu oluşturuldu"
# squash b7e9f1a "deneme"           → öncekiyle birleş
# squash c2d4e5f "test"             → öncekiyle birleş
# squash d5e6f7a "xxx düzelt"       → öncekiyle birleş
# pick e6f7a8b "Validasyon eklendi"
# squash ... (validasyonla ilgili hepsini squash)
# pick ... "Hata mesajları eklendi"
# ...
#
# Kaydet ve kapat. Birleştirilen her commit için mesaj yazman istenir.


# ══════════════════════════════════════════════════════════════════════════════
# CASE 8: Belirli Bir Commit'i Başka Branch'e Uygula (Cherry-pick)
# Senaryo: feature/a branch'indeki tek bir commit'i feature/b'ye de almak istiyorsun.
# ══════════════════════════════════════════════════════════════════════════════

# feature/a'daki commit hash'ini öğren:
$ git log feature/a --oneline
# a3f8c2d "Kritik performans iyileştirmesi"

# feature/b'ye geç ve cherry-pick yap:
$ git switch feature/b
$ git cherry-pick a3f8c2d
# → O commit feature/b'ye de uygulanır (yeni hash ile)

# Birden fazla commit:
$ git cherry-pick a3f8c2d b7e9f1a c2d4e5f


# ==============================================================================
# BÖLÜM 10: YAYGIN HATALAR & ÇÖZÜMLER
# ==============================================================================

# ═══════════════════════════════════════════════════════════
# HATA 1: "Please tell me who you are"
# NEDEN: Git kimliğin tanımlanmamış
# NE ZAMAN: İlk kurulumda veya yeni bilgisayarda
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git config --global user.name "Benn Yılmaz"
$ git config --global user.email "benn@example.com"


# ═══════════════════════════════════════════════════════════
# HATA 2: "fatal: not a git repository"
# NEDEN: Git repo olmayan bir klasörde git komutu çalıştırdın
# NE ZAMAN: Yanlış klasörde olduğunda
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ pwd                       # Neredesin?
$ ls -la                    # .git klasörü var mı?
$ cd dogru/klasor           # Doğru klasöre git
# Veya:
$ git init                  # Bu klasörü repo yap


# ═══════════════════════════════════════════════════════════
# HATA 3: "Your branch is ahead of 'origin/main' by X commits"
# NEDEN: Local'de push edilmemiş commitler var
# NE ZAMAN: push yapmayı unuttuysan
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git push origin main      # Sadece push et!


# ═══════════════════════════════════════════════════════════
# HATA 4: "Your branch is behind 'origin/main'"
# NEDEN: Remote'da local'inde olmayan commitler var
# NE ZAMAN: Takım arkadaşı push ettiyse ve sen pull yapmadıysan
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git pull origin main      # Veya:
$ git pull --rebase origin main  # Daha temiz


# ═══════════════════════════════════════════════════════════
# HATA 5: "CONFLICT — Merge conflict in dosya.py"
# NEDEN: Aynı dosyanın aynı satırı iki farklı yerde değiştirildi
# NE ZAMAN: Merge veya rebase sırasında
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git status                        # hangi dosyalarda conflict var?
# → Çakışan dosyaları aç (VS Code)
# → <<<<<<, =======, >>>>>>> işaretlerini bul
# → İstediğin kodu bırak, işaretleri sil
$ git add cakisan_dosya.py          # çözüldü işareti
$ git commit                        # merge'i tamamla
# Vazgeçmek için:
$ git merge --abort


# ═══════════════════════════════════════════════════════════
# HATA 6: "Permission denied (publickey)"
# NEDEN: SSH key GitHub'a eklenmemiş veya agent'ta yüklü değil
# NE ZAMAN: push/pull/clone yaparken
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ eval "$(ssh-agent -s)"            # Agent'ı başlat
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519  # Key'i ekle
$ ssh -T git@github.com             # Test et

# Key yoksa yeni oluştur (Bölüm 3'e bak)
# GitHub'a ekli mi kontrol et: GitHub → Settings → SSH Keys


# ═══════════════════════════════════════════════════════════
# HATA 7: "! [rejected] main → main (non-fast-forward)"
# NEDEN: Remote'da local'inde olmayan commit var, Git karışmasın diye reddediyor
# NE ZAMAN: pull yapmadan push etmeye çalıştığında
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git pull --rebase origin main     # Önce remote'u al
$ git push origin main              # Sonra push et


# ═══════════════════════════════════════════════════════════
# HATA 8: "detached HEAD state"
# NEDEN: Bir branch'te değil, direkt bir commit'tesin
# NE ZAMAN: git checkout <commit-hash> yaptığında
# ═══════════════════════════════════════════════════════════

# Çıktı: HEAD detached at a3f8c2d

# ÇÖZÜM (branch'e geri dön):
$ git switch main                   # var olan branch'e dön
# Veya detached HEAD'deyken yaptığın değişiklikleri korumak için:
$ git switch -c yeni-branch-adi     # yeni branch oluştur ve buraya kaydet


# ═══════════════════════════════════════════════════════════
# HATA 9: Yanlışlıkla .env veya büyük dosya commit ettim
# NEDEN: .gitignore'a eklemeyi unutmak
# NE ZAMAN: Hassas bilgileri (API key, şifre) veya büyük dosyaları commit edince
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM (push etmediysen):
$ git rm --cached .env              # Git'ten kaldır ama dosyayı silme
$ echo ".env" >> .gitignore         # .gitignore'a ekle
$ git commit -m "fix: .env gitignore'a eklendi"

# Push ettiysen (acil!):
# 1. Önce credential/API key'i değiştir (artık herkese açık!)
# 2. git-filter-repo ile geçmişten temizle:
$ pip install git-filter-repo
$ git filter-repo --path .env --invert-paths
$ git push --force origin main


# ═══════════════════════════════════════════════════════════
# HATA 10: "fatal: remote origin already exists"
# NEDEN: Remote origin zaten tanımlı, tekrar eklemek istedin
# NE ZAMAN: git remote add origin yaparken
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM:
$ git remote -v                              # Mevcut remote'u gör
$ git remote set-url origin YENİ_URL         # URL'i güncelle
# Veya mevcut remote'u sil ve tekrar ekle:
$ git remote remove origin
$ git remote add origin git@github.com:benn/repo.git


# ═══════════════════════════════════════════════════════════
# HATA 11: Commit mesajında yazım hatası (push etmediysen)
# ═══════════════════════════════════════════════════════════

$ git commit --amend -m "Düzeltilmiş mesaj"
# Sadece son commit! Push etmeden önce.


# ═══════════════════════════════════════════════════════════
# HATA 12: git pull yaparken "Please commit your changes or stash them"
# NEDEN: Local'de commit edilmemiş değişiklikler var, pull ile çakışabilir
# ═══════════════════════════════════════════════════════════

# ÇÖZÜM A — Stash:
$ git stash
$ git pull origin main
$ git stash pop

# ÇÖZÜM B — Commit et:
$ git add .
$ git commit -m "WIP: devam eden çalışma"
$ git pull --rebase origin main


# ==============================================================================
# BÖLÜM 11: PROFESYONEL İPUÇLARI
# ==============================================================================

# ─── .GİTİGNORE ──────────────────────────────────────────────────────────────
# Hangi dosyaların Git tarafından takip edilmeyeceğini belirtir.
# Proje kökünde .gitignore dosyası oluştur.

# Python projesi için örnek .gitignore:
# __pycache__/          → Python cache
# *.pyc                 → Compiled Python
# *.pyo
# .env                  → Ortam değişkenleri (API key'ler!)
# venv/                 → Virtual environment
# .venv/
# *.egg-info/
# dist/
# build/
# .DS_Store             → MacOS sistem dosyası
# .idea/                → JetBrains IDE
# .vscode/              → VS Code ayarları (paylaşmak istenmiyorsa)
# *.log                 → Log dosyaları
# node_modules/         → Node.js (full-stack projeler için)

# Global .gitignore (tüm projeler için — Mac'e özel):
$ git config --global core.excludesfile ~/.gitignore_global
# ~/.gitignore_global içine .DS_Store, .idea/ gibi Mac'e özel dosyaları ekle

# ─── COMMİT MESAJI STANDARDI ─────────────────────────────────────────────────
# Sektörde yaygın kullanılan "Conventional Commits" formatı:
#
# <type>(<scope>): <subject>
#
# type:
#   feat     → yeni özellik
#   fix      → hata düzeltme
#   docs     → dokümantasyon
#   style    → format (boşluk, virgül vb.)
#   refactor → ne özellik ne fix, kodu yeniden yazmak
#   test     → test ekle/düzelt
#   chore    → build, paket güncelleme vb.
#
# Örnekler:
# feat(auth): JWT tabanlı kimlik doğrulama eklendi
# fix(payment): Null pointer hatası giderildi
# docs(readme): Kurulum adımları güncellendi
# refactor(user): UserService sınıfı OOP'a dönüştürüldü
#
# Kural: İmperatif cümle yaz ("eklendi" yerine "ekle")
# Kural: 50 karakteri geçme (subject satırı)
# Kural: Neden değiştiğini açıkla, neyi değiştirdiğini değil

# ─── GİT ALIAS — KISAYOLLAR ──────────────────────────────────────────────────
# Uzun komutlara kısayol tanımla:

$ git config --global alias.s "status -s"          # git s
$ git config --global alias.lg "log --oneline --graph --all --decorate"  # git lg
$ git config --global alias.unstage "restore --staged"  # git unstage dosya.py
$ git config --global alias.last "log -1 HEAD"     # git last
$ git config --global alias.undo "reset HEAD~1 --mixed"  # git undo

# Kullanım:
$ git s                     # git status -s
$ git lg                    # güzel grafik log

# ─── GİT TAGS ─────────────────────────────────────────────────────────────────
$ git tag v1.0.0                           # lightweight tag
$ git tag -a v1.0.0 -m "Version 1.0.0"    # annotated tag (önerilen)
$ git push origin v1.0.0                  # tag'i remote'a gönder
$ git push origin --tags                  # tüm tag'leri gönder
$ git tag -l                              # tag listesi
$ git tag -d v1.0.0                       # tag sil


# ─── BÜYÜK PROJELERde git WORKFLOW ───────────────────────────────────────────
#
# Sektörde 2 yaygın model:
#
# 1. GITFLOW (klasik, karmaşık projeler):
#    main     → canlı kod
#    develop  → bir sonraki sürüm
#    feature/ → özellikler (develop'dan açılır)
#    release/ → sürüm hazırlığı
#    hotfix/  → acil düzeltme (main'den açılır)
#
# 2. TRUNK-BASED (modern, CI/CD ile):
#    main     → tek ana dal, her zaman deploy edilebilir
#    feature/ → kısa ömürlü dallar (max 1-2 gün)
#    Her commit main'e hızla entegre edilir
#    Büyük şirketler (Google, Facebook) bu modeli kullanır
#
# Başlangıç için: Gitflow'u öğren, ilerledikçe Trunk-based'e geç.


# ==============================================================================
# BÖLÜM 12: HIZLI REFERANS TABLOSU
# ==============================================================================
#
#  DURUM                          KOMUT
# ──────────────────────────────────────────────────────────────────────────────
#  Repo başlat                    git init
#  Repo clone et                  git clone URL
#  Durum kontrol et               git status  /  git status -s
#  Değişikliklere bak             git diff  /  git diff --staged
#  Dosya ekle (stage)             git add dosya.py  /  git add .  /  git add -p
#  Commit et                      git commit -m "mesaj"
#  Son commit'i düzelt            git commit --amend -m "yeni mesaj"
#  Log gör                        git log --oneline --graph --all
#  ──────────────────────────────────────────────────────────────────────────────
#  Branch listele                 git branch -a
#  Branch oluştur + geç           git switch -c feature/xxx
#  Branch değiştir                git switch main
#  Branch sil (güvenli)           git branch -d feature/xxx
#  Branch sil (zorla)             git branch -D feature/xxx
#  ──────────────────────────────────────────────────────────────────────────────
#  Remote listele                 git remote -v
#  Remote ekle                    git remote add origin URL
#  Push (ilk kez)                 git push -u origin branch-adi
#  Push                           git push origin branch-adi
#  Pull + merge                   git pull origin main
#  Pull + rebase                  git pull --rebase origin main
#  Fetch (merge olmadan)          git fetch origin
#  ──────────────────────────────────────────────────────────────────────────────
#  Merge branch                   git merge feature/xxx
#  Rebase                         git rebase main
#  Conflict çöz                   [Dosyayı düzenle] → git add → git commit
#  Merge/rebase iptal             git merge --abort  /  git rebase --abort
#  ──────────────────────────────────────────────────────────────────────────────
#  Değişikliği geri al            git restore dosya.py
#  Staging'den çıkar              git restore --staged dosya.py
#  Son commit'i geri al           git reset --soft HEAD~1  (değişiklikler kalır)
#  Son commit'i SİL               git reset --hard HEAD~1  (⚠️ kaybolur!)
#  Commit'i geri al (güvenli)     git revert HEAD
#  ──────────────────────────────────────────────────────────────────────────────
#  Yarım işi sakla                git stash push -m "açıklama"
#  Stash listesi                  git stash list
#  Stash'i geri al                git stash pop
#  ──────────────────────────────────────────────────────────────────────────────
#  Kayıp commit'i bul             git reflog
#  Belirli commit'e dön           git reset --hard HEAD@{N}
#  Dosyanın geçmişi               git log dosya.py
#  Kim yazdı?                     git blame dosya.py
#  Belirli commit'i başka         git cherry-pick <hash>
#    branch'e uygula
#  ──────────────────────────────────────────────────────────────────────────────
#  Tag oluştur                    git tag -a v1.0.0 -m "mesaj"
#  Tag'i push et                  git push origin v1.0.0
#  Interactive rebase             git rebase -i HEAD~N
#  Remote branch sil              git push origin --delete branch-adi
# ──────────────────────────────────────────────────────────────────────────────
#
#  GÜNDELİK RUTIN (Her Sabah):
#  1. git switch main
#  2. git pull --rebase origin main
#  3. git switch feature/xxx (kendi branch'in)
#  4. git rebase main  (main güncellemelerini al)
#  5. Çalış, commit'le, push et!
#
# ==============================================================================
