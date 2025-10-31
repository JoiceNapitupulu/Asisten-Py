import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys

# --- 1. Inisialisasi Engine ---
print("Menginisialisasi engine...")
try:
    engine = pyttsx3.init()
    # Atur suara (opsional, coba ganti '0' atau '1' untuk suara berbeda)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
except Exception as e:
    print(f"Error inisialisasi pyttsx3: {e}")
    print("Mungkin perlu menginstal Microsoft Speech Platform?")
    sys.exit()

# --- 2. Fungsi Bicara ---
def bicara(teks):
    """Fungsi untuk membuat asisten berbicara."""
    print(f"[Asisten]: {teks}")
    try:
        engine.say(teks)
        engine.runAndWait()
    except Exception as e:
        print(f"Error saat berbicara: {e}")

# --- 3. Fungsi Mendengar ---
def dengar_perintah():
    """Fungsi untuk mendengarkan perintah dari mikrofon."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Asisten]: Mendengarkan...")
        # Sesuaikan dengan kebisingan latar belakang
        try:
            r.adjust_for_ambient_noise(source, duration=1) 
        except Exception as e:
            print(f"Error akses mikrofon: {e}. Pastikan mikrofon terhubung.")
            return ""
            
        r.pause_threshold = 1 # Jeda 1 detik sebelum dianggap selesai
        audio = r.listen(source)

    try:
        print("[Asisten]: Mengenali...")
        # Menggunakan Google Web Speech API (membutuhkan internet)
        perintah = r.recognize_google(audio, language='id-ID')
        print(f"[Anda]: {perintah}\n")
        return perintah.lower()
    except sr.UnknownValueError:
        # Ini terjadi jika Google tidak mengerti apa yang Anda katakan
        print("[Asisten]: Maaf, saya tidak mengerti apa yang Anda katakan.")
        return ""
    except sr.RequestError as e:
        # Ini terjadi jika tidak ada koneksi ke Google API
        print(f"[Asisten]: Tidak bisa terhubung ke layanan Google; {e}")
        return ""
    except Exception as e:
        print(f"Error pengenalan suara: {e}")
        return ""

# --- 4. Fungsi Logika Utama ---
def jalankan_asisten():
    """Fungsi utama untuk menjalankan loop asisten."""
    bicara("Halo! Asisten Python Anda aktif. Ada yang bisa saya bantu?")

    while True:
        perintah = dengar_perintah()

        if 'jam berapa' in perintah:
            waktu = datetime.datetime.now().strftime('%H:%M')
            bicara(f"Sekarang jam {waktu}")

        elif 'tanggal berapa' in perintah:
            tanggal = datetime.datetime.now().strftime('%d %B %Y')
            bicara(f"Hari ini tanggal {tanggal}")

        elif 'cari' in perintah or 'apa itu' in perintah:
            subjek = perintah.replace('cari', '').replace('apa itu', '').strip()
            bicara(f"Mencari {subjek}...")
            try:
                # Mengatur bahasa Wikipedia ke Indonesia
                wikipedia.set_lang("id")
                # Mengambil 2 kalimat ringkasan
                info = wikipedia.summary(subjek, sentences=2)
                bicara(f"Menurut Wikipedia, {info}")
            except wikipedia.exceptions.PageError:
                bicara(f"Maaf, saya tidak menemukan {subjek} di Wikipedia. Mencari di Google.")
                pywhatkit.search(subjek)
            except Exception as e:
                bicara(f"Maaf, terjadi kesalahan: {e}")

        elif 'putar' in perintah:
            lagu = perintah.replace('putar', '').strip()
            bicara(f"Memutar {lagu} di YouTube.")
            pywhatkit.playonyt(lagu)

        elif 'keluar' in perintah or 'berhenti' in perintah:
            bicara("Selamat tinggal! Senang bisa membantu.")
            sys.exit()
        
        elif perintah: # Jika perintah terdeteksi tapi tidak dikenali
            bicara("Perintah tidak dikenali. Silakan coba lagi.")

# --- 5. Mulai Program ---
if __name__ == "__main__":
    jalankan_asisten()