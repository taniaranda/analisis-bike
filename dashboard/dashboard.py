import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='dark')

all_df = pd.read_csv('https://raw.githubusercontent.com/taniaranda/analisis-bike/main/dashboard/all_data.csv')

#st.write(df)

all_df.dropna(axis=0, inplace=True)

# Streamlit Dashboard
st.header('Proyek Analysis')


# Description
st.markdown("""
Menampilkan visualisasi analisis Bike Sharing dataset.
""")

# Sidebar
st.sidebar.header('Information')
st.sidebar.image('dashboard/bikes.jpg', caption = "Bike Sharing", use_column_width=True)
about = st.sidebar.text_area('About', 'This is a visualization of a bike sharing dataset analysis')

# rental per-jam
st.subheader('Jam sewa yang tinggi')
hourly_container = st.container()
with hourly_container:
    fig_hourly, ax_hourly = plt.subplots(figsize=(11, 5))
    sns.lineplot(x="hr", y="cnt_x", data=all_df, ci=None, ax=ax_hourly)
    ax_hourly.set_title("Jam Sewa")
    ax_hourly.set_xlabel("Jam")
    ax_hourly.set_ylabel("Jumlah Rental")
    st.pyplot(fig_hourly)
with st.expander("See explanation"):
    st.write("pada line plot, dapat dilihat bahwa jam sewa sepeda tertinggi ada pada jam 4-6 sore")

# korelasi cuaca
st.subheader('jumlah rental sepeda pada cuaca yang berbeda')
weather_container = st.container()
with weather_container:
    fig_weather, ax_weather = plt.subplots(figsize=(10, 6))
    sns.barplot(x="weathersit_x", y="cnt_x", data=all_df, palette="Set3", ax=ax_weather)
    ax_weather.set_title("jumlah rental sepeda pada cuaca yang berbeda")
    ax_weather.set_xlabel("Cuaca")
    ax_weather.set_ylabel("Jumlah Rental")
    st.pyplot(fig_weather)
with st.expander("See explanation"):
    st.write("desc: 1: Clear, Few clouds, Partly cloudy, Partly cloudy, 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist, 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds, 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")
    st.write("Pada chart yang telah kita buat, dapat di simpulkan terdapat korelasi antara kondisi cuaca (weathersit) dengan jumlah sewa sepeda (cnt_daily). Pada barplotnya kita dapat simpulkan bahwa, korelasi antara cuaca dan jumlah sepeda itu ada, dimana pada saat cuacanya clear (1) maka jumlah rentalnya itu lebih banyak. Saat cuacanya berkabut atau berembun (2) maka jumlah rentalnya menurun sedikit. Saat hujan atau bersalju sedikit (3) maka jumlah rentalnya akan menurun banyak.")

