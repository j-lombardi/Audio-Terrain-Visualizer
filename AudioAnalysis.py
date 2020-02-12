import audiosegment
import numpy as np


class AudioAnalysis:
    def __init__(self, filepath):
        self.song = audiosegment.from_file(filepath)    # Song file loaded in with AudioSegment
        self.length = len(self.song)                    # Length of song (in seconds)
        self.seconds = 0.5 * 1000                       # Used for time from milliseconds to seconds
        self.song_time_posistion = 0                    # Tracker of posistion in time

    @staticmethod
    def get_fft(song_bite):
        """
        Performs a fourier transform on a portion of the song and returns the data generated
        :param
            song_bite: AudioSegment song object to deconstruct
        :return
            bin: List of all of the frequencies
            freq: List of amplitude of the frequencies at each bin
                !!!(these two refers to each other; bin[3] refers to freq[3])!!!
        """
        bins, freq = song_bite.fft()
        freq = np.abs(freq) / len(freq)
        return bins, freq

    def get_next_splice(self):
        """

        :return
            splice:
        """
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
