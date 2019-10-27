import pyaudio
import numpy as np
from matplotlib import pylab as pyl
import time

RATE = 44100
CHUNK = int(RATE/20) # RATE/number of updates per second


def plotsound(stream):
    t = time.time()
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    pyl.plot(data)
    pyl.title('~~~Visuals~~~')
    pyl.grid()
    pyl.axis([0, len(data), -2 ** 16 / 2, 2 ** 16 / 2])
    pyl.savefig("03.png", dpi=50)
    pyl.close('all')

    print("took %.02f ms" % ((time.time()-t)*1000))


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    for i in range(int(20*RATE/CHUNK)):  # Do this for 10 seconds
        plotsound(stream)

    stream.stop_stream()
    stream.close()
    p.terminate()
