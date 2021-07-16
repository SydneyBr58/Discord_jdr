import io
import numpy as np
from queue import Queue
from scipy.io.wavfile import write
import sounddevice as sd
import soundfile as sf
import time

""" Disclaimer : cela a l'air bête d'enregistrer au format numpy array -> wav -> numpy array -> lecture
quand on pourrait ne pas faire de conversion. Mais c'est uniquement pour tester l'enregistrement.
=> Discord peut lire des fichiers .wav donc cela doit être le format généré
 """


def test():
    global fs
    fs = 48000
    buffersize = 50
    
    global q
    q = Queue(maxsize=0)
    print('Started')
    duration = 5
    t_end = time.time() + 15
    while time.time() < t_end:
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, device=14) # records for 'duration' second
        sd.wait() # wait until the recording is over (else, moves on directly)
        q.put(myrecording) # add the recording to the queue
 
    print('Recording finished')
    
    while q.empty() is False:
        audio = q.get() # get first element from queue
        temp_audio = io.BytesIO() # creates empty bite object => to have a .wav object in memory (too slow too write to disk) 
        write(temp_audio, fs, audio) # convert 'audio' (numpy array) into .wav
        data, fs = sf.read(temp_audio) # convert .wav to numpy array
        sd.play(data, fs) # read numpy array (that's how the audio is encoded)
        sd.wait()


try:
    test()
except KeyboardInterrupt:
    print('Recording over')

print('The END')