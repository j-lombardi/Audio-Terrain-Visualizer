import pydub
import audiosegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt
import time
from multiprocessing import Process
import threading

seconds = 3 * 1000 #PyDub uses miliseconds


def play_song(song):
    play(song)


def count_something():
    for i in range(0, 200):
        print(i)
        time.sleep(2)


def build_list(song):
    sound_list = []
    count = 0
    while count <= len(song):
        sound_list.append(song[count:count + seconds])
        count += seconds

    return sound_list


def display_graph(song_list):
    f = plt.figure()
    f.canvas.set_window_title("Test")
    for i in song_list:
        hist_bins, hist_vals = i.fft()
        hist_vals_real_normed = np.abs(hist_vals) / len(hist_vals)
        plt.plot(hist_bins / 1000, hist_vals_real_normed)
        plt.xlabel("kHz")
        plt.ylabel("dB")
        plt.show(block = False)
        #time.sleep(0.3)


if __name__=='__main__':
    file_path = "music/6. Kendrick Lamar - Heroin (Ft. SZA, Jay Rock, Isaiah Rashad, & Ab Soul).mp3"
    song = audiosegment.from_file(file_path)
    song_list = build_list(song)

    display_song_process = threading.Thread(target=display_graph(song_list))
    #count_process = threading.Thread(target=count_something)
    display_song_process.start()
    count_something()

