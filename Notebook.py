#!/usr/bin/env python
# coding: utf-8

# # Recommended-anime
# ## Dataset: https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

# # Import library

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# # Data Understanding

# ## Deskripsi Data

# In[4]:


df_anime = pd.read_csv('anime.csv')


# In[5]:


# Lihat 5 baris pertama dari dataset
print(df_anime.head())


# In[6]:


# Ukuran Data
print(f'Jumlah Baris: {df_anime.shape[0]}')
print(f'Jumlah Kolom: {df_anime.shape[1]}')


# In[7]:


# Fitur Data
print(f'Fitur: {df_anime.columns.tolist()}')


# Berikut adalah penjelasan singkat tentang fitur-fitur tersebut:
# 
# - `anime_id`: ID unik dari myanimelist.net yang mengidentifikasi anime.
# - `name`: Nama lengkap anime.
# - `genre`: Daftar genre untuk anime ini, dipisahkan oleh koma.
# - `type`: Jenis anime (misalnya, film, TV, OVA, dll.).
# - `episodes`: Jumlah episode dalam acara ini (1 jika film).
# - `rating`: Rata-rata rating dari semua pengguna di database myanimelist.net.
# - `members`: Jumlah anggota komunitas yang berada dalam "grup" anime ini.

# In[8]:


# Tipe Data
print(f'Tipe Data:\n{df_anime.dtypes}')


# ## Eksplorasi Awal

# In[9]:


# Ubah episodes ke numerik dan handle error dengan mengubahnya menjadi NaN
df_anime['episodes'] = pd.to_numeric(df_anime['episodes'], errors='coerce')

# Mengisi NaN dengan 0 atau nilai yang diinginkan
df_anime['episodes'] = df_anime['episodes'].fillna(0)

# Mengubah tipe data menjadi int64
df_anime['episodes'] = df_anime['episodes'].astype('int64')


# In[10]:


# Lihat statistik deskriptif dari dataset
print(df_anime.describe())


# In[11]:


# Missing Values
print("\nMissing Values:")
print(df_anime.isnull().sum())


# di beberapa kolom terjadi missing values

# In[12]:


# Mengisi missing values pada kolom 'genre' dengan 'Unknown'
df_anime['genre'] = df_anime['genre'].fillna('Unknown')


# In[13]:


# Mengisi missing values pada kolom 'type' dengan modus (nilai yang paling sering muncul)
df_anime['type'] = df_anime['type'].fillna(df_anime['type'].mode()[0])


# In[14]:


# Mengisi missing values pada kolom 'rating' dengan median
df_anime['rating'] = df_anime['rating'].fillna(df_anime['rating'].median())


# In[15]:


# Cek kembali missing values
print(df_anime.isnull().sum())


# Missing values sudah diperbaiki

# ## Visualisasi Data

# In[16]:


# Histogram untuk kolom 'rating'
plt.figure(figsize=(10,5))
plt.hist(df_anime['rating'].dropna(), bins=50, alpha=0.5, color='g')
plt.title('Distribusi Rating')
plt.xlabel('Rating')
plt.ylabel('Frekuensi')
plt.show()


# Histogram tersebut menunjukkan distribusi rating anime dalam dataset. Dari histogram tersebut, dapat melihat bahwa rating paling umum berada di sekitar 6 hingga 8. Terdapat juga beberapa anime dengan rating di bawah 6 dan di atas 8, tetapi jumlahnya lebih sedikit. Ini menunjukkan bahwa sebagian besar anime memiliki rating yang cukup tinggi, dengan sebagian kecil yang memiliki rating sangat tinggi atau sangat rendah. 

# In[17]:


# Bar plot untuk kolom 'type'
plt.figure(figsize=(10,5))
df_anime['type'].value_counts().plot(kind='bar')
plt.title('Distribusi Tipe Anime')
plt.xlabel('Tipe')
plt.ylabel('Frekuensi')
plt.show()


# Grafik batang tersebut menunjukkan distribusi tipe anime dalam dataset. Dari grafik tersebut, dapat melihat bahwa tipe anime yang paling umum adalah TV, diikuti oleh OVA dan Movie. Tipe anime Special dan ONA memiliki jumlah yang lebih sedikit, sementara Music adalah tipe anime dengan jumlah terkecil. Ini menunjukkan bahwa sebagian besar anime dalam dataset adalah tipe TV, OVA, atau Movie.

# In[18]:


# Scatter plot antara 'members' dan 'rating'
plt.figure(figsize=(10,5))
plt.scatter(df_anime['members'], df_anime['rating'], alpha=0.5)
plt.title('Hubungan antara Members dan Rating')
plt.xlabel('Members')
plt.ylabel('Rating')
plt.show()


# Grafik scatter plot tersebut menunjukkan hubungan antara jumlah anggota (`members`) dan rating anime. Dari grafik tersebut, dapat melihat bahwa sebagian besar data terkonsentrasi di area dengan jumlah anggota rendah dan rating tinggi. Ini menunjukkan bahwa sebagian besar anime memiliki rating yang cukup tinggi meskipun jumlah anggotanya relatif rendah.

# In[19]:


# Buat boxplot untuk kolom 'episodes'
plt.figure(figsize=(10,5))
plt.boxplot(df_anime['episodes'].dropna())
plt.title('Boxplot episodes Anime')
plt.ylabel('Rating')
plt.show()


# Dari boxplot yang Anda tunjukkan, tampaknya ada beberapa outliers dalam kolom `episodes`.

# In[20]:


# Hitung Q1, Q3, dan IQR untuk kolom 'episodes'
Q1 = df_anime['episodes'].quantile(0.25)
Q3 = df_anime['episodes'].quantile(0.75)
IQR = Q3 - Q1

# Tentukan batas bawah dan batas atas untuk outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Ganti outliers dengan NaN
df_anime['episodes'] = np.where((df_anime['episodes'] < lower_bound) | (df_anime['episodes'] > upper_bound), np.nan, df_anime['episodes'])

# Mengisi NaN dengan median
df_anime['episodes'] = df_anime['episodes'].fillna(df_anime['episodes'].median())


# Outliers di kolom episodes sudah diperbaiki

# In[21]:


# Buat boxplot untuk kolom 'rating'
plt.figure(figsize=(10,5))
plt.boxplot(df_anime['rating'].dropna())
plt.title('Boxplot Rating Anime')
plt.ylabel('Rating')
plt.show()


# Dari boxplot yang Anda tunjukkan, tampaknya ada beberapa outliers dalam kolom `rating`.

# In[22]:


# Hitung Q1, Q3, dan IQR untuk kolom 'rating'
Q1 = df_anime['rating'].quantile(0.25)
Q3 = df_anime['rating'].quantile(0.75)
IQR = Q3 - Q1

# Tentukan batas bawah dan batas atas untuk outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Ganti outliers dengan NaN
df_anime['rating'] = np.where((df_anime['rating'] < lower_bound) | (df_anime['rating'] > upper_bound), np.nan, df_anime['rating'])

# Mengisi NaN dengan median
df_anime['rating'] = df_anime['rating'].fillna(df_anime['rating'].median())


# Outliers di kolom rating sudah diperbaiki

# In[4]:


pip install nbconvert


# In[2]:


get_ipython().system('jupyter nbconvert --to script Notebook.ipynb')

