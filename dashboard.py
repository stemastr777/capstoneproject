import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import PIL

# Opening
st.title('Batubara dan Minyak Bumi Menyebabkan Harga Listrik di Indonesia Meningkat')


#komposisi_bahanbakar
st.subheader('Batubara merupakan bahan bakar pembangkit listrik yang paling berpengaruh')

df_bahanbakar = pd.read_excel('Capstone Project/bahanbakar_pembangkit_listrik.xlsx')

fig1, ax1 = plt.subplots(figsize=(5,6))
fig1.set_facecolor('white')
ax1.set_title('Komposisi Penggunaan Bahan Bakar Pembangkit Listrik\nTahun 2020 di Indonesia', fontsize=15)
patches, texts, autotexts = ax1.pie(df_bahanbakar['persentase'], labels=df_bahanbakar['Bahan Bakar'], autopct='%.0f%%', textprops={'fontsize': 15})
for i in texts:
    i.set_fontsize(12)
plt.tight_layout()

kb1,kb2 = st.columns(2)
with kb1:
    st.pyplot(fig1)
with kb2:
    st.write('''Batubara menyumbang lebih dari setengah dari keseluruhan bahan bakar pembangkit listrik pada
tahun 2020, mengalahkan minyak dan gas.''')

# harga_bahanbakar
df_coal = pd.read_excel('Capstone Project/harga_batubara.xlsx')
df_coal['tahun'] = df_coal['tahun'].astype('str')
df_coal_mean = df_coal.groupby('tahun')['harga'].mean().reset_index()

bb = plt.figure(figsize=(8,5.5))
sns.lineplot(data=df_coal_mean, x='tahun', y='harga')
plt.title('Harga Rata-Rata Batubara', fontsize=15, pad=10, loc='center')
plt.ylabel('USD/ton')
plt.grid(color='gray', linewidth=0.5, linestyle=':')
plt.ylim(ymin=0)

st.subheader('\nHarga Batubara dan Minyak Bumi Mengalami Tren Naik')
image = PIL.Image.open("Capstone Project/harga_minyak.png")
hb1, hb2 = st.columns(2)
with hb1:
    st.pyplot(bb)
    st.write('Selama tahun 2016 hingga 2021, harga batubara dunia mengalami tren naik sebesar kurang lebih 50% ')
with hb2:
    st.image(image)
    st.write('Selama 5 tahun terakhir, harga minyak bumi telah meningkat sebesar 41,22%')


# harga_listrik
st.subheader('\nTren naik pada harga listrik sektor rumah tangga')

df_listrik = pd.read_excel("Capstone Project/harga_listrik.xlsx")
df_listrik['tahun'] = df_listrik.loc[:,'tahun'].astype('str')

fig, ax = plt.subplots(figsize=(8,3.5))
sns.lineplot(data=df_listrik, x='tahun', y='harga', hue='wilayah', ax=ax)
ax.set_title('Grafik Harga Listrik Sektor Rumah Tangga di Jawa Tengah', fontsize=15, loc='center', pad=15)
plt.ylabel('Rp/kWh')
plt.grid(color='gray', linewidth=0.5, linestyle=':')
plt.ylim(ymin=0)
plt.tight_layout()
st.pyplot(fig)

st.write(
    '''Berdasarkan data harga listrik pada 5 kota yang terletak di Jawa Tengah, 
    data menunjukkan bahwa harga listrik mengalami tren naik selama 2016-2021. Meskipun sempat turun pada 
    tahun 2020, harga listrik kembali mengalami kenaikan pada tahun 2021.\n\n Ada banyak faktor yang mempengaruhi
    kenaikan ini, seperti kebijakan pemerintah, kondisi perekonomian dunia, dll. Projek ini akan berfokus pada bahan bakar
    yang digunakan untuk membangkitkan listrik.''')


# pembangkit_listrik
st.subheader('Pengalihan PLTG Menjadi PLTGU Merupakan Solusi Jangka Pendek')
df_pl = pd.read_excel('Capstone Project/Pembangkit_listrik.xlsx')

fig4 = plt.figure(figsize=(8,4))
sns.barplot(data=df_pl, x='tahun', y='energi', hue='jenis')
plt.title('Jumlah Energi yang Dihasilkan\nMenurut Jenis Pembangkit Listrik', fontsize=15, pad=10)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), shadow=True)

pl1, pl2 = st.columns([2,1])
image2 = PIL.Image.open("Capstone Project/kualitas_bahanbakar.png")
with pl1:
    st.pyplot(fig4)
with pl2:
    st.image(image2)

st.write('''
    Dilansir dari "https://web.pln.co.id/statics/uploads/2021/04/Statistik-Indonesia-2020-unaudited.pdf", 
    terdapat 66 PLTG dan 79 PLTGU yang ada di Indonesia. Pengalihan PLTG menjadi PLTGU bisa meningkatkan efisiensi
    penggunaan minyak bumi. Hal tersebut juga bisa membantu menyeimbangkan harga listrik akibat adanya lonjakan
    harga suatu jenis bahan bakar. Namun, hal ini hanya bersifat sementara.
''')

# jumlah_pengguna
st.subheader('Jumlah listrik yang didistribusikan dapat menjadi \'bom waktu\'')

df_pengguna = pd.read_excel("Capstone Project/jumlah_pengguna.xlsx")
df_pengguna['tahun'] = df_pengguna['tahun'].astype('str')
df_pengguna['jumlah'] = df_pengguna['jumlah']/1000000

fig3 = plt.figure(figsize=(8,3.5))
sns.lineplot(data=df_pengguna, x='tahun', y='jumlah')
plt.title('Jumlah Listrik yang Didistribusikan di Indonesia\n Periode 2012-2020', fontsize=15)
plt.ylim(ymin=0)
plt.ylabel('jumlah energi(juta KWh)')
plt.grid(linewidth=0.5, linestyle=":", color='darkgray')
plt.tight_layout()
st.pyplot(fig3)

st.write('''Batubara dan minyak bumi merupakan salah satu jenis bahan bakar fosil yang berarti bisa habis. Sementara itu, jumlah 
distribusi listrik ke depannya diprediksi semakin bertambah seiring bertambahnya jumlah penduduk. Hal ini diprediksi
berdasarkan grafik di atas.''')

# Closing
st.write('''
Maka dari itu, pemerintah harus segera menemukan energi alternatif yang murah,efisien, dan dapat diperbaharui.
''')
