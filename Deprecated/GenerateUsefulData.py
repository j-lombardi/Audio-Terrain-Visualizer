"""
 This was a test of using audiosegment to generate useful data based on a song input
"""
import audiosegment
import numpy as np


seconds = 0.5 * 1000 #PyDub uses miliseconds

file_path = ""  # insert file path of mp3 or wav song to test
song = audiosegment.from_file(file_path)
#song = song._data

sound_list = []
count = 0
while count <= len(song):
    sound_list.append(song[count:count + seconds])
    count += seconds

# Returns:
# np.ndarray of frequencies, np.ndarray of amount of each frequency
#bins = sound_list[0].fft()[0].astype(float)

#freq = sound_list[17].fft()[1].astype(float)

bin_list = []
freq_list = []
for i in sound_list:
    bins, freq = i.fft()
    freq = np.abs(freq) / len(freq)
    print(bins[len(bins) - 1], "|", freq[0])
    bin_list.append(bins)
    freq_list.append(freq)



#normal_freq = (freq - min(freq))/(max(freq)-min(freq))
#normal_bins = (bins - min(bins))/(max(bins)-min(bins)) * 1000
for index, value in enumerate(freq_list):
    print("%f | %f" %(bin_list[index], freq_list[index]))
#print(normal_freq)

#print(freq.astype(float))
