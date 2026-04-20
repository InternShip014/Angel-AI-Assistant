import serial
import time
import speech_recognition as sr

PORT = 'COM6'
SEBESSEG = 115200

print(f"Csatlakozás az ESP32-höz a(z) {PORT} porton...")
try:
    esp32 = serial.Serial(PORT, SEBESSEG, timeout=1)
    time.sleep(2)
    print("Sikeres csatlakozás az ESP32-höz!")
except Exception as e:
    print(f"\nHIBA: Nem tudok csatlakozni a(z) {PORT} porthoz!")
    print("MEGOLDÁS: Zárd be az Arduino IDE-ben a Soros Monitort!")
    exit()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("\nMikrofon kalibrálása... Kérlek maradj csendben 1 másodpercig.")
    r.adjust_for_ambient_noise(source)
    print("\n>>> KÉSZEN ÁLLOK! Mondd, hogy 'turn on' vagy 'turn off' <<<")

    while True:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            # 1. VÁLTOZÁS: A nyelvet átállítottuk "en-US"-re (Amerikai angol)
            szoveg = r.recognize_google(audio, language="en-US").lower()
            print(f"Ezt hallottam: '{szoveg}'")

            # 2. VÁLTOZÁS: Angol szavakat keresünk a szövegben
            if "turn on" in szoveg or "light on" in szoveg:
                print("--> Parancs küldése: BE (1)")
                esp32.write(b'1')

            elif "turn off" in szoveg or "light off" in szoveg:
                print("--> Parancs küldése: KI (0)")
                esp32.write(b'0')

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Nem értettem tisztán, ismételd meg.")
        except sr.RequestError:
            print("Nincs internetkapcsolat.")
        except KeyboardInterrupt:
            print("\nKilépés...")
            esp32.close()
            break