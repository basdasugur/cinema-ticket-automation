satilan_biletler = []
toplam_ciro = 0

# Sabitleri tanımlaman harika bir alışkanlık!
FIYAT_AVATAR = 100
FIYAT_TITANIC = 80
FIYAT_STAR_WARS = 90

print("--- SİNEMA GİŞE SİSTEMİ ---")

while True:
    print("\n1. Avatar (100 TL)")
    print("2. Titanic (80 TL)")
    print("3. Star Wars (90 TL)")
    print("q. Çıkış")

    secim = input("Seçiminiz: ").strip().lower()

    if secim == "q":
        print("-" * 30)
        print("SATIŞ RAPORU:")

        # 1. Önce biletleri listeliyoruz
        for film in satilan_biletler:
            print(f"- {film}")

        # 2. Döngü bittikten sonra TOPLAMI yazıyoruz (Girintiye dikkat!)
        print("-" * 30)
        print(f"TOPLAM CİRO: {toplam_ciro} TL")
        break

    # Geçersiz tuşlama kontrolü (Else yerine elif zinciri daha güvenli burada)
    elif secim not in ["1", "2", "3"]:
        print("Hatalı seçim! Lütfen 1, 2, 3 veya q giriniz.")
        continue  # Döngünün başına dön

    # --- SATIŞ MANTIĞI ---
    # Kod tekrarını önlemek için önce fiyatı ve film adını belirliyoruz
    secilen_film_fiyati = 0
    secilen_film_adi = ""

    if secim == "1":
        secilen_film_fiyati = FIYAT_AVATAR
        secilen_film_adi = "Avatar"
    elif secim == "2":
        secilen_film_fiyati = FIYAT_TITANIC
        secilen_film_adi = "Titanic"
    elif secim == "3":
        secilen_film_fiyati = FIYAT_STAR_WARS
        secilen_film_adi = "Star Wars"

    # İndirim Sorusu (Tek bir yerde soruyoruz - DRY Prensibi)
    ogrenci_mi = input(f"{secilen_film_adi} için öğrenci indirimi var mı? (e/h): ").strip().lower()

    if ogrenci_mi == "e":
        fiyat = secilen_film_fiyati * 0.8  # %20 indirim
        print(f"✅ Öğrenci indirimi uygulandı.")
    else:
        fiyat = secilen_film_fiyati  # Tam fiyat

    # Kasa ve Liste İşlemleri
    toplam_ciro += fiyat  # HATA 1 DÜZELTİLDİ: += kullanıldı
    satilan_biletler.append(secilen_film_adi)
    print(f"🎟️ {secilen_film_adi} bileti satıldı. Tutar: {int(fiyat)} TL")
