# werent-backend

## Prasyarat

Sebelum menjalankan aplikasi, pastikan telah mendownload aplikasi berikut:

-   **Docker**

## Menjalankan Aplikasi

1. Build

    Build terlebih dahulu semua image yang diperlukan (Proses build memakan waktu yang panjang - **_akan diperbaiki kedepannya_**)

```bash
    docker-compose build --no-cache
```

2. Jalankan Aplikasi

    Jalankan perintah dibawah ini. Tunggu hingga muncul **_running on_** seperti biasa. dan bisa langsung mengunjungi alamat [http://127.0.0.1:5000](http://127.0.0.1:5000)

```bash
    docker-compose up
```

3. Menghentikan aplikasi

    Untuk menghentikan aplikasi bisa dengan cara menekan **_CTRL+C_** dan tunggu hingga proses selesai. kemudian lanjutkan dengan perintah berikut

```bash
    # setelah menekan CTRL+C

    docker-compose down
```

4. Jika ingin memulai semuanya dari awal jika terjadi error
```bash
    # hapus terlebih dahulu folder 'Migrations'
    # kemudian jalankan perintah berikut

    docker-compose down -v

    # perintah tersebuh akan menghapus semua volume, network, dan container yang ada (image tetap ada)
```


## Melakukan Migrasi & Upgrade

Migrasi & update harus dilakukan di dalam docker, karena aplikasi berjalan di dalam docker. Berikut adalah cara melakukan migrasi.

```bash
    # jalankan perintah dibawah satu per satu

    docker-compose exec backend flask db migrate -m "add migrations message"

    docker-compose exec backend flask db upgrade
```

## Melihat database melalui aplikasi lainnya

Jika ingin memeriksa data apa saja yang ada di dalam database, bisa menggunakan aplikasi seperti **_DBeaver_**. Berikut adalah data-data yang perlu diperhatikan:

-   **Server Host**: localhost
-   **Port**: 3307
-   **Database**: db
-   **Username**: root
-   **Password**: db

Seluruh informasi tersebut dapat dilihat dari **_.env.tempalte_**

## Important Note

-   Ketika docker sudah berjalan, maka perubahan secara otomatis akan terupdate di docker. Dapat dilihat melalui terminal jika aplikasi flask ter-refresh.
