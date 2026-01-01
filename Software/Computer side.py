import serial
import sounddevice as sd
import numpy as np
import time
import random

SERIAL_PORT = 'COM4'
BAUD_RATE = 115200
MIN_HOEK = 80
MAX_HOEK = 100
RUST_HOEK = 90
SENSITIVITY = 20       
DREMPELWAARDE = 2.0    


try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
    time.sleep(2)
    print(f"Verbonden met {SERIAL_PORT}")
except Exception as e:
    print(f"Kon geen verbinding maken: {e}")
    exit()

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status)
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm < DREMPELWAARDE:
        angle = RUST_HOEK
    else:
        uitslag = int(volume_norm * SENSITIVITY)
        richting = random.choice([-1, 1])
        angle = RUST_HOEK + (uitslag * richting)
        angle = max(MIN_HOEK, min(angle, MAX_HOEK))
    try:
        ser.write(f"{angle}\n".encode())
    except:
        pass

try:
       with sd.InputStream(callback=audio_callback, blocksize=2048): 
        while True:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nGestopt.")
    ser.write(f"{RUST_HOEK}\n".encode())
    ser.close()