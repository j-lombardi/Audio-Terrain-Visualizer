import audiosegment
import numpy as np

class AudioAnalysis:
    def __init__(self, filepath):
        self.song = audiosegment.from_file(filepath)
        self.length = len(self.song)
        self.seconds = 0.5 * 1000 # AudioSegments handle times in milliseconds, this is to convert when needed
        self.song_time_posistion = 0

    @staticmethod
    def get_fft(song_bite):
        bin, freq = song_bite.fft()
        freq = np.abs(freq) / len(freq)
        return bin, freq

    def get_next_splice(self):
        splice = self.song[self.song_time_posistion:self.song_time_posistion + self.seconds]
        self.song_time_posistion += self.seconds
        return splice

    def get_useful_values(self):
        bins, freq = self.get_fft(self.get_next_splice())
        n_elements_per_slice = 220
        average_array = []
        for i in range(0, len(freq), n_elements_per_slice):
            slice_from_index = i
            slice_to_index = slice_from_index + n_elements_per_slice
            average_array.append(np.mean(freq[slice_from_index:slice_to_index]))
        return average_array

    def splice_entire_song(self):
        song_list = []
        count = 0
        while count <= self.length:
            song_list.append(self.song[count:count + self.seconds])
            count += self.seconds
        return song_list


ma = AudioAnalysis("music/1. Kendrick Lamar - Gang Member.mp3")
for i in range(0, 10):
    print(ma.get_useful_values())
