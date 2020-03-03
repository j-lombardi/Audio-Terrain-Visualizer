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
        Splices the music from the current position through SELF.SECONDS, then updates position
        :return
            splice: A cut of the song from self.SONG_TIME_POSITION through self.SONG_TIME_POSITION + self.SECONDS
        """
        splice = self.song[self.song_time_posistion:self.song_time_posistion + self.seconds]
        self.song_time_posistion += self.seconds
        return splice

    def get_useful_values(self):
        """
        Normalizes the data returned from freq in get_fft in order to make data more useful
        Steps for normalization:
            1) Slice full fft freq list into even sized lists
            2) Average out each of those list slices
            3) Append the averaged value to average_array
        :return
            average_array: List of averaged values reducing the huge freq array down to a much smaller list
        """
        bins, freq = self.get_fft(self.get_next_splice())
        n_elements_per_slice = 220
        average_array = []

        for i in range(0, len(freq), n_elements_per_slice):
            slice_from_index = i
            slice_to_index = slice_from_index + n_elements_per_slice
            average_array.append(np.log(np.mean(freq[slice_from_index:slice_to_index])))
        return average_array

    def get_useful_values_by_splice(self, segment):
        """
        Normalizes the data returned from freq in get_fft in order to make data more useful
        Steps for normalization:
            1) Slice full fft freq list into even sized lists
            2) Average out each of those list slices
            3) Append the averaged value to average_array
        :return
            average_array: List of averaged values reducing the huge freq array down to a much smaller list
        """

        '''
        SUB BASS:   20 to 60 Hz     (Deep bass, felt more than it is heard)
        BASS:       60 to 250 Hz    (Describes how fat/thin the sound is. Most in 90-200 range, 250ish for warm feel)
        LOW MID:    250 to 500 Hz   (Low order harmonics, viewed as bass presence range)
        MIDRANGE:   500 to 2 kHz    (Prominence of instrumentation in mix, high mids mean tinny sounds)
        UPPER MID:  2 kHz to 4 kHz  (Very sensitive for human hearing, vocals usually in this range. Like a fire alarm)
        PRESENCE:   4 kHz to 6 kHz  (Center for treble sounds in stereo systems)
        BRILLIANCE  6 kHz to 20 kHz (Totally harmonics, responsible for sparkle and air of sound)
        '''

        bins, freq = self.get_fft(segment)

        sub_bass = freq[0:60]
        bass = freq[60:250]
        low_mid = freq[250:500]
        midrange = freq[500:2000]
        upper_mid = freq[2000:4000]
        presence = freq[4000:6000]
        brilliance = freq[6000:]

        sub_bass = self.average_freq_list(sub_bass)
        bass = self.average_freq_list(bass)
        low_mid = self.average_freq_list(low_mid)
        midrange = self.average_freq_list(midrange)
        upper_mid = self.average_freq_list(upper_mid)
        presence = self.average_freq_list(presence)
        brilliance = self.average_freq_list(brilliance)

        full_list = sub_bass + bass + low_mid + midrange + upper_mid + presence + brilliance


        return full_list


    def normalize(self):
        fft_song_list = self.preload_song()
        #min_val = min(map(min, fft_song_list))
        #max_val = max(map(max, fft_song_list))
        #for x_count, segment in enumerate(fft_song_list):
        #    for y_count, value in enumerate(segment):
        #        fft_song_list[x_count][y_count] = (((value - min_val) / (max_val - min_val)) * 10)
        return fft_song_list


    def average_freq_list(self, freq):
        n_elements_per_slice = round(len(freq) / 15)

        if n_elements_per_slice is 0:
            return [0]*15

        average_array = []
        for i in range(0, len(freq), n_elements_per_slice):
            slice_from_index = i
            slice_to_index = slice_from_index + n_elements_per_slice
            average_array.append(np.abs(np.log(np.mean(freq[slice_from_index:slice_to_index]))))
        return average_array

    def preload_song(self):
        song_list = self.splice_entire_song()
        fft_song_list = []
        for segment in song_list:
            fft_song_list.append(self.get_useful_values_by_splice(segment))
        return fft_song_list

    def splice_entire_song(self):
        """
        Splices the music up in its entirety and returns a list of all of the various splices. Splices are of
        size/duration SELF.SECONDS
        :return
            song_list: The entire song cut into smaller portions of SELF.SECONDS duration
        """
        song_list = []
        count = 0
        while count <= self.length:
            song_list.append(self.song[count:count + self.seconds])
            count += self.seconds
        return song_list
