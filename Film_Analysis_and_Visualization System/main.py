import streamlit as st
from film_analiz import FilmAnaliz

st.set_page_config(page_title="Netflix Film Analiz", layout="centered")

analiz = FilmAnaliz()

st.title("🎬 Netflix Film & Dizi Analizi")

menu = st.sidebar.selectbox("İşlem Seçiniz", [
    "Tür Filtrele", "Yıl Aralığına Göre", "Ülkeye Göre Filtrele",
    "Yıllara Göre Bar Grafik", "Film/Dizi Oranı", "Popüler Türler",
    "Yıllık Trend (Çizgi Grafik)", "Başlığa Göre Arama", "Yeni İçerik Ekle"
])

if menu == "Tür Filtrele":
    tur = st.text_input("Tür giriniz (örnek: Drama, Comedy):")
    if st.button("Filtrele"):
        st.write("Filtrelenen Sonuçlar:")
        analiz.tur_filtrele(tur)

elif menu == "Yıl Aralığına Göre":
    baslangic = st.number_input("Başlangıç Yılı", 1950, 2025, 2000)
    bitis = st.number_input("Bitiş Yılı", 1950, 2025, 2020)
    if st.button("Göster"):
        analiz.yil_araligi(baslangic, bitis)

elif menu == "Ülkeye Göre Filtrele":
    ulke = st.text_input("Ülke giriniz (örnek: Turkey, India):")
    if st.button("Filtrele"):
        analiz.ulke_filtrele(ulke)

elif menu == "Yıllara Göre Bar Grafik":
    st.write("Yıllara göre içerik sayısı:")
    analiz.yillara_gore_bar()

elif menu == "Film/Dizi Oranı":
    analiz.tur_grafigi()

elif menu == "Popüler Türler":
    analiz.populer_turler()

elif menu == "Yıllık Trend (Çizgi Grafik)":
    analiz.yillik_trend()

elif menu == "Başlığa Göre Arama":
    kelime = st.text_input("Başlıkta geçen kelime:")
    if st.button("Ara"):
        analiz.baslik_arama(kelime)

elif menu == "Yeni İçerik Ekle":
    title = st.text_input("İçerik Başlığı")
    year = st.number_input("Yayın Yılı", min_value=1900, max_value=2025, value=2020)
    country = st.text_input("Ülke")
    types = st.selectbox("Tür", ["Movie", "TV Show"])
    listed_in = st.text_input("Kategori (örnek: Drama, Action)")
    if st.button("Ekle"):
        analiz.yeni_ekle(title, year, country, types, listed_in)