import serial
import time
import speech_recognition as sr

PORT = 'COM6'
SEBESSEG = 115200

print(f"Csatlakozás az ESP32-höz a(z) {PORT} porton...")
try:
    # Létrehozzuk a kapcsolatot
    esp32 = serial.Serial(PORT, SEBESSEG, timeout=1)
    time.sleep(2)  # Várunk picit, amíg az ESP32 újraindul a csatlakozáskor
    print("Sikeres csatlakozás az ESP32-höz!")
except Exception as e:
    print(f"\nHIBA: Nem tudok csatlakozni a(z) {PORT} porthoz!")
    print("MEGOLDÁS: Zárd be az Arduino IDE-ben a Soros Monitort (Serial Monitor), mert lefoglalja a kábelt!")
    exit()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("\nMikrofon kalibrálása... Kérlek maradj csendben 1 másodpercig.")
    r.adjust_for_ambient_noise(source)
    print("\n>>> KÉSZEN ÁLLOK! Mondd, hogy 'felkapcsol' vagy 'lekapcsol' <<<")

    while True:
        try:
            # Várjuk a hangot
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            # Értelmezzük magyarul
            szoveg = r.recognize_google(audio, language="hu-HU").lower()
            print(f"Ezt hallottam: '{szoveg}'")

            # Parancsok küldése
            if "felkapcsol" in szoveg or "bekapcsol" in szoveg:
                print("--> Parancs küldése: BE (1)")
                esp32.write(b'1')

            elif "lekapcsol" in szoveg or "kikapcsol" in szoveg:
                print("--> Parancs küldése: KI (0)")
                esp32.write(b'0')

        except sr.WaitTimeoutError:
            pass  # Nem volt hang, újra fülel
        except sr.UnknownValueError:
            print("Nem értettem tisztán, ismételd meg.")
        except sr.RequestError:
            print("Nincs internetkapcsolat.")
        except KeyboardInterrupt:
            print("\nKilépés...")
            esp32.close()
            break