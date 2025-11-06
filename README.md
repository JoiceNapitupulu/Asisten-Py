# Asisten-Py: Asisten Suara Python dengan AI Lokal (Ollama)

Asisten-Py adalah proyek asisten virtual sederhana yang dibuat dengan Python. Asisten ini dapat merespons perintah suara, menjawab pertanyaan, memutar musik dari YouTube, dan memberikan informasi dasar seperti waktu dan tanggal. Keunikan proyek ini adalah integrasinya dengan **Ollama**, yang memungkinkannya menjalankan model bahasa besar (LLM) secara lokal untuk menjawab pertanyaan pengetahuan umum.

## ✨ Fitur Utama

* **Input Suara & Teks:** Dapat menerima perintah melalui mikrofon (suara) atau input teks langsung di terminal.
* **Respons Suara:** Memberikan umpan balik dan jawaban dalam bentuk suara (Text-to-Speech).
* **Perintah Dasar:**
    * `jam berapa`: Memberi tahu waktu saat ini.
    * `tanggal berapa`: Memberi tahu tanggal hari ini.
    * `putar [judul lagu/video]`: Mencari dan memutar video dari YouTube.
* **Integrasi AI Lokal:** Terhubung ke server Ollama untuk menjawab pertanyaan pengetahuan umum menggunakan model AI (misalnya, `deepseek-coder`).
* **Keluar:** Dapat dihentikan dengan perintah `keluar` atau `berhenti`.

## 🛠️ Teknologi yang Digunakan

* **Python 3:** Bahasa pemrograman utama.
* **speech_recognition:** Untuk pengenalan suara (Speech-to-Text).
* **pyttsx3:** Untuk sintesis suara (Text-to-Speech).
* **pywhatkit:** Untuk memutar video/musik di YouTube.
* **ollama:** Klien Python untuk berinteraksi dengan server Ollama (LLM Lokal).
* **datetime:** Modul bawaan Python untuk mendapatkan informasi waktu dan tanggal.

## 🚀 Prasyarat & Instalasi

Sebelum menjalankan proyek ini, pastikan Anda telah memenuhi prasyarat berikut:

1.  **Python 3.x:** Pastikan Python terinstal di sistem Anda.
2.  **Instalasi Library Python:**
    Instal semua library yang diperlukan menggunakan pip:
    ```bash
    pip install speechrecognition pyttsx3 pywhatkit ollama
    ```
    *Catatan: `speech_recognition` mungkin memerlukan library tambahan seperti `PyAudio` untuk akses mikrofon.*

3.  **Instalasi Server Ollama:**
    Proyek ini **memerlukan** server Ollama yang berjalan di komputer Anda.
    * Unduh dan instal Ollama dari [situs resminya](https://ollama.com/).

4.  **Unduh Model AI (Ollama):**
    Setelah Ollama terinstal, Anda perlu mengunduh model yang akan digunakan. Proyek ini dikonfigurasi untuk menggunakan `deepseek-coder:6.7b`.
    ```bash
    ollama run deepseek-coder:6.7b
    ```
    *(Anda dapat mengubah model ini di dalam file `asisten.py` pada fungsi `tanya_ai` jika Anda lebih suka model lain).*

5.  **Mikrofon:** Diperlukan untuk input perintah suara.

## 📁 Susunan Project

Struktur proyek ini sangat sederhana dan hanya terdiri dari satu file utama:

/ │ └── asisten.py # Logika utama asisten


## ▶️ Contoh Penggunaan

1.  **Jalankan Server Ollama:** Pastikan server Ollama Anda aktif.
2.  **Jalankan Asisten:** Buka terminal dan navigasikan ke direktori proyek, lalu jalankan:
    ```bash
    python asisten.py
    ```
3.  **Inisialisasi:** Program akan menginisialisasi engine TTS dan menyapa Anda.
    ```
    Menginisialisasi engine...
    [Asisten]: Halo! Asisten Python dengan otak DeepSeek aktif. Ada yang bisa saya bantu?
    ```
4.  **Berikan Perintah:** Anda dapat mengetikkan perintah Anda:

    **Contoh Perintah Dasar:**
    ```
    [Anda]: jam berapa
    [Asisten]: Sekarang jam 14:30
    ```
    ```
    [Anda]: putar oasis wonderwall
    [Asisten]: Baik, memutar oasis wonderwall di YouTube.
    (Membuka browser dan memutar video)
    ```

    **Contoh Perintah AI (Ollama):**
    ```
    [Anda]: siapa penemu bola lampu?
    [Asisten]: Menghubungi DeepSeek (Ollama)...
    [Asisten]: Penemu bola lampu pijar yang paling dikenal secara komersial adalah Thomas Alva Edison.
    ```

    **Untuk Berhenti:**
    ```
    [Anda]: keluar
    [Asisten]: Selamat tinggal! Senang bisa membantu.
    ```
    *(Jika Anda ingin menggunakan input suara, Anda perlu memodifikasi file `asisten.py` untuk mengganti `input("[Anda]: ").lower()` dengan `dengar_perintah()` di dalam loop `jalankan_asisten`)*

## 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi pada proyek ini, silakan ikuti langkah-langkah berikut:

1.  **Fork** repositori ini.
2.  Buat **Branch** baru (`git checkout -b fitur/NamaFiturBaru`).
3.  Lakukan **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur A'`).
4.  **Push** ke Branch Anda (`git push origin fitur/NamaFiturBaru`).
5.  Buka **Pull Request**.

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**. Lihat file `LICENSE` (yang perlu Anda tambahkan) untuk detail lebih lanjut.

```markdown
Copyright (c) [Tahun] [Nama Anda/Pemilik Repositori]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
