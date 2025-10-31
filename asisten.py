import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import sys
import ollama  

#Inisialisasi Engine
print("Menginisialisasi engine...")
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
except Exception as e:
    print(f"Error inisialisasi pyttsx3: {e}")
    sys.exit()

#Fungsi Bicara
def bicara(teks):
    """Fungsi untuk membuat asisten berbicara."""
    print(f"[Asisten]: {teks}")
    try:
        engine.say(teks)
        engine.runAndWait()
    except Exception as e:
        print(f"Error saat berbicara: {e}")

#Fungsi Mendengar
def dengar_perintah():
    """Fungsi untuk mendengarkan perintah dari mikrofon."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Asisten]: Mendengarkan...")
        try:
            r.adjust_for_ambient_noise(source, duration=1) 
        except Exception as e:
            print(f"Error akses mikrofon: {e}. Pastikan mikrofon terhubung.")
            return ""
            
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("[Asisten]: Mengenali...")
        perintah = r.recognize_google(audio, language='id-ID')
        print(f"[Anda]: {perintah}\n")
        return perintah.lower()
    except sr.UnknownValueError:
        print("[Asisten]: Maaf, saya tidak mengerti apa yang Anda katakan.")
        return ""
    except sr.RequestError as e:
        print(f"[Asisten]: Tidak bisa terhubung ke layanan Google STT; {e}")
        return ""
    except Exception as e:
        print(f"Error pengenalan suara: {e}")
        return ""

#Fungsi untuk bertanya ke AI (Ollama)
def tanya_ai(perintah_teks):
    """Mengirim perintah teks ke Ollama dan mendapatkan respons."""
    print(f"[Asisten]: Menghubungi DeepSeek (Ollama)...")
    try:
        # Menggunakan ollama.chat untuk percakapan
        response = ollama.chat(
            model='deepseek-coder:6.7b',  # <-- PASTIKAN NAMA MODEL INI BENAR
            messages=[
                {'role': 'system', 'content': 'Kamu adalah asisten AI yang membantu dalam bahasa Indonesia. Jawab dengan singkat dan jelas.'},
                {'role': 'user', 'content': perintah_teks}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error saat menghubungi Ollama: {e}")
        print("Pastikan server Ollama Anda berjalan (misal: 'ollama run deepseek-coder:6.7b')")
        return "Maaf, saya tidak bisa terhubung ke model AI lokal saya."

#Fungsi Logika Utama
def jalankan_asisten():
    """Fungsi utama untuk menjalankan loop asisten."""
    bicara("Halo! Asisten Python dengan otak DeepSeek aktif. Ada yang bisa saya bantu?")

    while True:
        perintah = dengar_perintah()

        if not perintah: 
            continue
        
        if 'jam berapa' in perintah:
            waktu = datetime.datetime.now().strftime('%H:%M')
            bicara(f"Sekarang jam {waktu}")

        elif 'tanggal berapa' in perintah:
            tanggal = datetime.datetime.now().strftime('%d %B %Y')
            bicara(f"Hari ini tanggal {tanggal}")
        
        elif 'putar' in perintah:
            lagu = perintah.replace('putar', '').strip()
            bicara(f"Baik, memutar {lagu} di YouTube.")
            pywhatkit.playonyt(lagu)

        elif 'keluar' in perintah or 'berhenti' in perintah:
            bicara("Selamat tinggal! Senang bisa membantu.")
            sys.exit()

        # --- Perintah Pengetahuan (AI) ---
        # Jika bukan perintah aksi di atas, kirim ke Ollama
        else:
            jawaban_ai = tanya_ai(perintah)
            bicara(jawaban_ai)

#Mulai Program
if __name__ == "__main__":
    jalankan_asisten()