import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

freq = 48000
duration = 5
rec_name = "testing.wav"

#start recording
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2, blocking=True)


#Recrod audio for the given number of seconds
sd.wait()
sf.write(rec_name, recording, freq) # Writing recorded sound in a file