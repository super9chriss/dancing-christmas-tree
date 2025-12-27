import sounddevice as sd
import numpy as np
import serial
import time

DEVICE = 11           
SAMPLERATE = 48000
BLOCKSIZE = 1024
SMOOTH = 0.2    
servo_value = 90      

usb = serial.Serial('COM4', 115200)  
time.sleep(2)                         

def callback(indata, frames, time_info, status):
    global servo_value
    volume = np.sqrt(np.mean(indata**2))
    target = int(volume * 1800)       
    target = max(0, min(180, target)) 
    servo_value = int(servo_value + (target - servo_value) * SMOOTH)

    usb.write(bytes([servo_value]))

with sd.InputStream(device=DEVICE, channels=2, samplerate=SAMPLERATE,
                    blocksize=BLOCKSIZE, latency='low', callback=callback):
    print("Stream gestart, speel nu muziek af...")
    input("Druk Enter om te stoppen\n")
