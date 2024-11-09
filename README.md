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

## Melakukan Migrasi & Upgrade

Migrasi & update harus dilakukan di dalam docker, karena aplikasi berjalan di dalam docker. Berikut adalah cara melakukan migrasi.

```bash
    docker-compose exec backend flask db migrate
```

## Important Note

-   Ketika docker sudah berjalan, maka perubahan secara otomatis akan terupdate di docker. Dapat dilihat melalui terminal jika aplikasi flask ter-refresh.
