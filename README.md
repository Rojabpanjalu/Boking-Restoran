# 🍽️ Booking Meja Restoran – UAS Pemrograman Python

Website sederhana untuk melakukan pemesanan meja restoran secara online, dibuat menggunakan **FastAPI (Backend)** dan **Streamlit (Frontend)**.

---

## 📌 Fitur Utama

- ✅ Formulir pemesanan meja (nama, tanggal, jam, jumlah orang)
- ✅ Simpan data booking ke file `data.json`
- ✅ Lihat riwayat semua pemesanan
- ✅ UI sederhana dan mudah digunakan
- ✅ Integrasi client-server via REST API (POST & GET)

---

## 🛠️ Teknologi yang Digunakan

- Python 3.x
- FastAPI
- Uvicorn (server backend)
- Streamlit (UI web)
- JSON (sebagai database sementara)

---

## 📂 Struktur Folder

```
restaurant-booking/
├── main.py         ← Backend API FastAPI
├── app.py          ← Frontend UI Streamlit
├── data.json       ← File penyimpanan booking
└── README.md       ← Dokumentasi ini
```

---

## 🚀 Cara Menjalankan

### 1. Install Library (sekali saja)
```bash
pip install fastapi uvicorn streamlit
```

### 2. Jalankan Backend FastAPI
```bash
uvicorn main:app --reload
```
→ Aktif di `http://localhost:8000`

### 3. Jalankan Frontend Streamlit (di terminal terpisah)
```bash
streamlit run app.py
```
→ Aktif di `http://localhost:8501`

---

## 🧪 Contoh Input Form

- Nama: Raka Santosa
- Tanggal: 2025-07-25
- Jam: 18:00
- Jumlah orang: 4

---

## 📌 Penjelasan Endpoint API

- `GET /bookings` → Menampilkan semua data booking
- `POST /bookings` → Menyimpan data booking baru

---

## 📞 Kontak Pengembang

- 👨‍💻 Nama: [Nama Kamu]
- 💻 NIM: [NIM Kamu]
- 📚 Universitas: AMIKOM Yogyakarta

---

> *Project ini dibuat sebagai Ujian Akhir Semester Mata Kuliah Pemrograman Python 2025.*
