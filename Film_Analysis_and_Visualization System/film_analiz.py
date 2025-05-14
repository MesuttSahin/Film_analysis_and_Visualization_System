import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from collections import Counter


class FilmAnaliz:
    def __init__(self):
        self.df = pd.read_csv("netflix_titles.csv")

    def tur_filtrele(self, tur):
        filtreli = self.df[self.df["listed_in"].str.contains(tur, na=False)]
        st.dataframe(filtreli[["title", "type", "release_year"]].head(10))

    def yil_araligi(self, baslangic, bitis):
        secim = self.df[(self.df["release_year"] >= baslangic) & (self.df["release_year"] <= bitis)]
        st.dataframe(secim[["release_year", "title", "country"]].head(10))

    def ulke_filtrele(self, ulke_adi):
        secim = self.df[self.df["country"].str.contains(ulke_adi, na=False)]
        st.dataframe(secim[["title", "country"]].head(20))

    def tur_grafigi(self):
        sayim = self.df["type"].value_counts()
        sayim.plot.pie(autopct="%1.1f%%")
        plt.title("Film vs Dizi Oranı")
        st.pyplot(plt)
        plt.clf()

    def yillara_gore_bar(self):
        grafik = self.df["release_year"].value_counts().sort_index()
        grafik.plot(kind="bar", figsize=(10, 5))
        plt.xlabel("Yıl")
        plt.ylabel("İçerik Sayısı")
        plt.title("Yıllara Göre İçerik Sayısı")
        plt.tight_layout()
        st.pyplot(plt)
        plt.clf()

    def populer_turler(self):
        tur_listesi = self.df['listed_in'].dropna().str.split(', ')
        tum_turler = [tur for liste in tur_listesi for tur in liste]
        sayim = Counter(tum_turler)
        en_populer = dict(sayim.most_common(10))

        plt.bar(en_populer.keys(), en_populer.values())
        plt.xticks(rotation=45)
        plt.title("En Popüler Türler")
        st.pyplot(plt)
        plt.clf()

    def yillik_trend(self):
        movie = self.df[self.df['type'] == "Movie"]['release_year'].value_counts().sort_index()
        tv = self.df[self.df['type'] == "TV Show"]['release_year'].value_counts().sort_index()

        plt.plot(movie.index, movie.values, label="Filmler", color="red")
        plt.plot(tv.index, tv.values, label="Diziler", color="blue")
        plt.xlabel("Yıl")
        plt.ylabel("İçerik Sayısı")
        plt.legend()
        plt.title("Yıllara Göre Film & Dizi Trendleri")
        plt.grid(True)
        st.pyplot(plt)
        plt.clf()

    def baslik_arama(self, kelime):
        secim = self.df[self.df['title'].str.contains(kelime, case=False, na=False)]
        st.dataframe(secim[['title', 'type', 'release_year']].head())

    def yeni_ekle(self, title, year, country, types, listed_in):
        yeni = {
            'title': title,
            'release_year': year,
            'country': country,
            'type': types,
            'listed_in': listed_in
        }
        self.df = pd.concat([self.df, pd.DataFrame([yeni])], ignore_index=True)
        st.success("Ekleme İşlemi Başarılı!")
        self.kaydet()

    def kaydet(self):
        self.df.to_csv("netflix_titles.csv", index=False)
        st.info("Veriler Kaydedildi.")
