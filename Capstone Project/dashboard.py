import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Opening
st.title('Batubara menyebabkan kenaikan Harga Listrik Sektor Rumah Tangga di Jawa Tengah')
st.subheader('Tren naik pada harga listrik sektor rumah tangga pada tahun 2016-2021 di Jawa Tengah')

# harga_listrik
df_listrik = pd.read_excel("D:\TetrisProgram\Capstone Project\harga_listrik.xlsx")
df_listrik['tahun'] = df_listrik.loc[:,'tahun'].astype('str')


fig, ax = plt.subplots(figsize=(8,4))
sns.lineplot(data=df_listrik, x='tahun', y='harga', hue='wilayah', ax=ax)
ax.set_title('Nilai Rp/KWh Listrik Rumah Tangga di Jawa Tengah menurut unit PLN', fontsize=15, loc='center', pad=15)
plt.ylabel('Harga listrik (Rp/KWh)')
plt.grid(color='gray', linewidth=0.5, linestyle=':')
plt.ylim(ymin=0)
plt.tight_layout()
st.pyplot(fig)

st.write(
    '''Berdasarkan data harga listrik pada 5 kota yang terletak di Jawa Tengah, 
    data menunjukkan bahwa harga listrik mengalami tren naik selama 2016-2021. Meskipun sempat turun pada 
    tahun 2020, harga listrik kembali mengalami kenaikan pada tahun 2021.''')

# bahan_bakar_listrik
st.subheader('Batubara merupakan bahan bakar pembangkit listrik yang paling berpengaruh')

df_bahanbakar = pd.read_excel('D:\TetrisProgram\Capstone Project\\bahanbakar_pembangkit_listrik.xlsx')
fig1, ax1 = plt.subplots(figsize=(5,6))
fig1.set_facecolor('white')
ax1.set_title('Komposisi Penggunaan Bahan Bakar Pembangkit Listrik\nTahun 2020 di Indonesia', fontsize=15)
patches, texts, autotexts = ax1.pie(df_bahanbakar['persentase'], labels=df_bahanbakar['Bahan Bakar'], autopct='%.0f%%', textprops={'fontsize': 15})
for i in texts:
    i.set_fontsize(12)
plt.tight_layout()


# harga_batubara
df_coal = pd.read_excel('D:\TetrisProgram\Capstone Project\harga_batubara.xlsx')
df_coal['tahun'] = df_coal['tahun'].astype('str')
df_coal_mean = df_coal.groupby('tahun')['harga'].mean().reset_index()

fig2 = plt.figure(figsize=(8,4))
sns.lineplot(data=df_coal_mean, x='tahun', y='harga')
plt.title('Harga Rata-Rata Batubara per Ton(dalam USD)', fontsize=15, pad=10, loc='center')
plt.ylabel('Harga batubara (USD/ton)')
plt.grid(color='gray', linewidth=0.5, linestyle=':')
plt.ylim(ymin=0)

graf2, graf1 = st.columns([3,2])
with graf2:
    st.pyplot(fig2)
with graf1:
    st.pyplot(fig1)

st.write('''Pada tahun 2017 dan 2021, harga batubara meningkat. Pada tahun tersebut pula, harga listrik di kelima 
kota di Jawa Tengah meningkat. Hal ini menunjukkan bahwa batubara mempengaruhi harga listrik. Hal ini diperkuat 
oleh data di sebelah kiri. Batubara menyumbang lebih dari setengah dari keseluruhan bahan bakar pembangkit listrik.
''')
# jumlah_pengguna
st.subheader('Jumlah listrik yang didistribusikan dapat menjadi \'bom waktu\'')

df_pengguna = pd.read_excel("D:\TetrisProgram\Capstone Project\jumlah_pengguna.xlsx")
df_pengguna = df_pengguna.loc[df_pengguna['unit'].isin(['Semarang','Surakarta','Pekalongan','Magelang','Purwokerto'])]
df_pengguna['tahun'] = df_pengguna['tahun'].astype('str')
df_pengguna['jumlah_energi'] = df_pengguna['jumlah_energi']/1000000

fig3 = plt.figure(figsize=(8,3))
sns.lineplot(data=df_pengguna, x='tahun', y='jumlah_energi', hue='unit')
plt.title('Jumlah Listrik yang Didistribusikan di Jawa Tengah\n Periode 2016-2021 ', fontsize=15)
plt.ylabel('jumlah energi yang terjual(juta KWh)')
plt.grid(linewidth=0.5, linestyle=":", color='darkgray')
st.pyplot(fig3)
st.write('''Batubara merupakan salah satu jenis bahan bakar fosil yang berarti bisa habis. Sementara itu, jumlah 
distribusi listrik ke depannya diprediksi semakin bertambah seiring bertambahnya jumlah penduduk.\n\nMaka dari itu,
pemerintah harus segera mencari sumber energi alternatif yang lebih efisien dan murah agar harga listrik tidak menjadi
gangguan bagi masyarakat.''')
