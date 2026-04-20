# 🎙️ ESP32 Voice-Controlled LED Project

This project is a simple but visually engaging example of how to control an LED connected to an **ESP32** development board using voice commands. The system uses the computer's microphone and a Python-based speech recognition script to interpret commands and forward them to the ESP32 via serial communication.

---

## 🛠️ Hardware Requirements

To build this project, you will need the following components:

* **ESP32-DEVKIT-32U** (Or any other standard ESP32 module)
* 1x **LED** (any color)
* 1x **220Ω or 330Ω resistor**
* Breadboard
* Jumper wires (male-to-male)
* Micro-USB data cable

## 🔌 Wiring Diagram

Connecting the hardware is extremely simple:

1. **LED Positive leg (Anode/Longer leg):** Connect to the **D2** (GPIO 2) pin of the ESP32.
2. **LED Negative leg (Cathode/Shorter leg):** Connect through the current-limiting **resistor** to one of the **GND** (Ground) pins on the ESP32.
3. **Power / Data connection:** Plug the ESP32 into your computer using the USB cable.

---

## 💻 Software Setup

The project consists of two parts: the C++ (Arduino) code running on the ESP32, and the Python script running on the computer.

### 1. Arduino (ESP32) Side

Upload this code to your board using the Arduino IDE. This program listens to the serial port (USB) and toggles the LED based on incoming `1` or `0` characters.