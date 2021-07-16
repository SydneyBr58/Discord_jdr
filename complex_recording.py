import io
import numpy as np
from queue import Queue
from scipy.io.wavfile import write
import sounddevice as sd
import soundfile as sf
import time


fs = 48000
buffersize = 50

global q
q = Queue(maxsize=0)
temp_audio = io.BytesIO()

def basic():
    ###file = 'rick.wav'
    duration = 30
    fs = 48000
    temp_audio = io.BytesIO()
    # Record for 15 seconds
    print('Recording started')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, device=14, dtype=np.int16)
    sd.wait()
    print('Recording over')

    #write(temp_audio, fs, myrecording)
    #write('rick16.wav', fs, myrecording)

    
    #WORKS
    data, fs = sf.read(temp_audio)
    sd.play(data, fs)
    sd.wait()
    

def callback(indata, frames, time, status):
    """Add recording to the queue in wav format """
    # write(temp_audio, fs, indata.copy())
    
    audio_file.write(data=indata.copy(), samplerate=fs)
    q.put(audio_file)


def test():
    global fs
    fs = 48000
    buffersize = 50
    temp_audio = io.BytesIO()
    global q
    q = Queue(maxsize=0)
    print('Started')
    t_end = time.time() + 5
    while time.time() < t_end:
        with sf.SoundFile(temp_audio, mode='w', samplerate=fs,
                      channels=2, format='wav') as audio_file:
            with sd.InputStream(samplerate=fs, channels=2, callback=callback, device=14):
                #print('Added to queue - ',time.time())
                pass
        
    print('Recording finished')
    while True:
        audio = q.get_nowait()
        data, fs = sf.read(audio)
        sd.play(data, fs, device=8)
        sd.wait()

basic()
'''
try:
    #truc
except KeyboardInterrupt:
    print('Recording over')
'''
print('The END')