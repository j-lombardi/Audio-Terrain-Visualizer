from pydub import AudioSegment
import audiosegment
import numpy as np
import matplotlib.pyplot as plt
from pydub.playback import play

seconds = 3 * 1000 #PyDub uses miliseconds

file_path = "music/6. Kendrick Lamar - Heroin (Ft. SZA, Jay Rock, Isaiah Rashad, & Ab Soul).mp3"
song = audiosegment.from_file(file_path)

sound_list = []
count = 0
while count <= len(song):
    sound_list.append(song[count:count + seconds])
    count += seconds

# Returns:
# np.ndarray of frequencies, np.ndarray of amount of each frequency
bins = sound_list[0].fft()[0].astype(float)

freq = sound_list[17].fft()[1].astype(float)

bin_list = []
freq_list = []
for i in sound_list:
    bin, freq = i.fft()
    bin_list.append(bin)
    freq_list.append(freq)

normal_freq = abs(freq - min(freq))/(max(freq)-min(freq))
normal_bins = abs(bins - min(bins))/(max(bins)-min(bins))
for index, value in enumerate(freq):
    print("%f | %f" %(bins[index], freq[index]))
#print(normal_freq)

print(freq.astype(float))
play(sound_list[0])
play(sound_list[17])