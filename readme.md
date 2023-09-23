# Laporan Proyek Machine Learning - Rezaldi

## Project Overview

Anime telah menjadi fenomena global dan memiliki penggemar di seluruh dunia. Dengan ribuan judul yang tersedia, mencari anime yang sesuai dengan selera pribadi bisa menjadi tantangan. Oleh karena itu, proyek ini bertujuan untuk mengembangkan sistem rekomendasi anime yang dapat memberikan saran judul anime berdasarkan preferensi pengguna.

Proyek ini penting karena dapat membantu penggemar anime menemukan judul baru yang sesuai dengan selera penggemar anime. Dengan begitu, penggemar anime dapat lebih menikmati hobi mereka dan mungkin menemukan judul favorit baru. Selain itu, sistem rekomendasi ini juga dapat digunakan oleh platform streaming untuk meningkatkan pengalaman pengguna.
  
  Referensi: [Penerapan Collaborative Filtering, PCA dan K-Means dalam Pembangunan Sistem Rekomendasi Ongoing dan Upcoming Film Animasi Jepang](https://conference.upnvj.ac.id/index.php/senamika/article/view/1343) 

## Business Understanding

### Problem Statements

Berikut adalah beberapa pernyataan masalah:
- Bagaimana cara mengidentifikasi preferensi pengguna terhadap anime berdasarkan data yang ada?
- Bagaimana cara mengembangkan model yang dapat memprediksi anime mana yang akan disukai oleh pengguna berdasarkan preferensi mereka?
- Bagaimana cara memastikan bahwa rekomendasi yang diberikan oleh sistem relevan dan bervariasi, sehingga pengguna tidak hanya mendapatkan rekomendasi dari satu atau dua genre saja?

### Goals

Berikut adalah beberapa tujuan berdasarkan pernyataan masalah:
- Mengembangkan metode untuk mengidentifikasi preferensi pengguna terhadap anime berdasarkan data yang ada. Ini bisa melibatkan analisis data pengguna dan anime, seperti genre dan rating.
- Membangun model machine learning yang dapat memprediksi anime mana yang akan disukai oleh pengguna berdasarkan preferensi mereka. Model ini harus dapat belajar dari data historis dan membuat prediksi yang akurat untuk pengguna baru.
- Membuat sistem rekomendasi yang dapat memberikan rekomendasi yang relevan dan bervariasi kepada pengguna. Sistem ini harus dapat menyesuaikan rekomendasinya berdasarkan feedback dari pengguna.

    ### Solution Approach
    Berikut adalah beberapa pendekatan solusi yang mungkin berdasarkan tujuan yang telah ditetapkan:

    - Collaborative Filtering: Pendekatan ini melibatkan pembuatan sistem rekomendasi berdasarkan perilaku pengguna lain yang memiliki preferensi serupa. Misalnya, jika pengguna A dan B sama-sama menyukai anime X dan Y, dan pengguna A juga menyukai anime Z, maka sistem dapat merekomendasikan anime Z kepada pengguna B.
    - Content-Based Filtering: Pendekatan ini melibatkan pembuatan sistem rekomendasi berdasarkan fitur konten dari anime itu sendiri, seperti genre atau type nya. Misalnya, jika pengguna menyukai anime dengan genre aksi, maka sistem dapat merekomendasikan anime lain dengan genre yang sama.


## Data Understanding

Dataset yang digunakan dalam proyek ini adalah "Anime Recommendations Database" yang dapat diunduh dari [Kaggle](https://www.kaggle.com/CooperUnion/anime-recommendations-database). Dataset ini berisi informasi tentang anime, termasuk judul, genre, jenis, jumlah episode, rating, dan jumlah anggota komunitas yang menyukai anime tersebut.

**Deskripsi Data**

- Jumlah Baris: 12,294
- Jumlah Kolom: 7

**Variabel-variabel pada Dataset Anime Recommendations Database adalah sebagai berikut:**

1. `anime_id`: ID unik yang mengidentifikasi setiap anime di myanimelist.net.
2. `name`: (int64) Nama lengkap dari anime.
3. `genre`: (object) Daftar genre dari anime, dipisahkan oleh koma.
4. `type`: (object) Jenis anime, misalnya, TV, Movie, OVA, dll.
5. `episodes`: (object) Jumlah episode dalam anime (1 jika film).
6. `rating`: (float64) Rata-rata rating anime dari semua pengguna di myanimelist.net.
7. `members`: (int64) Jumlah anggota komunitas yang menyukai anime ini.

**Eksplorasi Awal Data**

- Data telah diunggah dan diperiksa untuk memahami informasi dasar, termasuk ukuran data dan tipe data masing-masing kolom.
- Ditemukan adanya missing values di kolom 'genre,' 'type,' 'rating,' dan 'episodes,' yang kemudian diisi atau diperbaiki sesuai dengan kebutuhan.
- Visualisasi data dilakukan untuk mengeksplorasi distribusi rating, jenis anime, hubungan antara jumlah anggota dan rating, serta penanganan outliers di kolom 'episodes' dan 'rating.'

**Eksplorasi Awal Data**


## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
