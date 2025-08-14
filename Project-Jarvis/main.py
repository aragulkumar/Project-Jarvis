import sounddevice as sd
import numpy as np
import queue

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

# Start live capture (16 kHz, mono)
stream = sd.InputStream(callback=callback, channels=1, samplerate=16000)
stream.start()

