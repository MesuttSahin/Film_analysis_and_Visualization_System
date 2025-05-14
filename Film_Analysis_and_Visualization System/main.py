from film_analiz import FilmAnaliz

film_sinifi = FilmAnaliz()

while True:
    print("""
    --- Netflix Analiz Sistemine Hoş Geldiniz ---

    1. Belirli türdeki filmleri listele
    2. Belirli yıl aralığında çıkanları listele
    3. Ülkeye göre filtrele
    4. İçerik türü dağılımı grafiğini çiz
    5. Yıllara göre içerik artışı grafiği
    6. Popüler türleri listele
    7. Yıllık trend grafiği
    8. Başlık Arama
    9. Veri Ekle
    6. Programı kapat

    """)
    secim = int(input())
    if secim==1:
        film_sinifi.tur_filtrele(input("Tür: "))
    elif secim==2:
        film_sinifi.yil_araligi(int(input("Başlangıç: ")),int(input("Bitiş: ")))
    elif secim==3:
        film_sinifi.ulke_filtrele(input("Ülke Adı: "))
    elif secim==4:
        film_sinifi.tur_grafigi()
    elif secim==5:
        film_sinifi.yillara_gore_bar()
    elif secim==6:
        film_sinifi.populer_turler()
    elif secim==7:
        film_sinifi.yillik_trend()
    elif secim==8:
        film_sinifi.baslik_arama(input("Başlık: "))
    elif secim==9:
        film_sinifi.yeni_ekle(input("Başlık: "),int(input("Yıl: ")),input("Ülke: "),input("Tür: "),input("Liste türü: "))
    elif secim==10:
        break
    else:
        print("Lütfen geçerli seçim yapınız....")
