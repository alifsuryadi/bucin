# Bucin Chatbot

Bucin Chatbot adalah sebuah aplikasi berbasis web yang memungkinkan Anda untuk berinteraksi dengan chatbot yang sangat romantis. Chatbot ini dibuat menggunakan Flask sebagai backend dan HTML/CSS serta JavaScript di frontend.

## Fitur

- Chat dengan bot yang penuh cinta dan perhatian.
- Penyimpanan chat lokal menggunakan `localStorage`.
- Penggunaan emoji dan custom emotes dalam chat.

## Prasyarat

Sebelum Anda menjalankan proyek ini, pastikan Anda sudah menginstal:

- Python 3.x
- pip (Package Installer for Python)
- Virtual environment (opsional, tapi direkomendasikan)
- Flask (termasuk Flask-CORS)
- dotenv (untuk mengelola variabel lingkungan)

## Instalasi

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/alifsuryadi/bucin.git
   cd bucin
   ```

2. **Buat dan aktifkan virtual environment (opsional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk MacOS/Linux
   venv\Scripts\activate  # Untuk Windows
   ```

3. **Instal dependensi yang diperlukan:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Buat file `.env` di root proyek dan tambahkan API key:**

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Pastikan struktur direktori untuk file statis sesuai:**
   ```bash
   bucin/
   ├── static/
   │   └── index.html
   └── bucin/generative_text_bucin/
       ├── __init__.py
       ├── chat.py
       └── config.py
   ```

## Menjalankan Aplikasi

1. **Jalankan aplikasi menggunakan perintah berikut:**

   ```bash
   python -m app
   ```

2. **Akses aplikasi melalui browser di alamat:**

   ```
   http://127.0.0.1:5000
   ```

3. **Mulai percakapan dengan bot:**
   - Ketik pesan Anda dan klik "Send" untuk mengirim pesan ke chatbot.
   - Klik "Clear" untuk menghapus percakapan sebelumnya.

## Troubleshooting

- **Tidak ada respon dari AI:**
  - Pastikan bahwa server Flask berjalan dengan baik tanpa error.
  - Periksa console log di browser untuk melihat apakah ada error pada JavaScript atau kegagalan fetch request.
- **Twemoji tidak terload:**
  - Jika emoji tidak muncul, pastikan koneksi internet stabil atau unduh `twemoji.min.js` dan load secara lokal.

## Catatan

- Aplikasi ini hanya untuk pengembangan. Jangan gunakan di lingkungan produksi tanpa penyesuaian lebih lanjut.
- Untuk deployment di production, pertimbangkan menggunakan WSGI server seperti Gunicorn dan mengatur proxy server seperti Nginx.

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Silakan baca file `LICENSE` untuk informasi lebih lanjut.
