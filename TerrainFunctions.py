from vpython import *
import AudioAnalysis as aa
import time
import threading
from pydub.playback import play

def create_map_empty():
    cols, rows = (100, 100)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(cols):
        for j in range(rows):
            h = 1
            arr[i][j] = box(pos=vector(i, h / 2, j), length=1, width=1, height=h, color=color.cyan)
    return arr

def shift(arr):
    for i in range(99, 0, -1):
        for j in range(99, -1, -1):
            arr[i][j].height = arr[i-1][j].height
            arr[i][j].color = arr[i - 1][j].color
            arr[i][j].pos.y = arr[i][j].height / 2


def add_new_row(arr, arr2):
    shift(arr)
    for i in range(0, 100):
        arr[0][i].height = arr2[i]
        if arr[0][i].height > 45:
            arr[0][i].color = color.white
        elif arr[0][i].height > 10:
            arr[0][i].color = color.green
        elif arr[0][i].height > 2:
            arr[0][i].color = color.cyan
        else:
            arr[0][i].color = color.black
        arr[0][i].pos.y = arr[0][i].height / 2


def visualize(arr, mas):
    play_song_thread = threading.Thread(target=play, args=(mas.song,))
    play_song_thread.start()
    for i in range(0, mas.length - 1):
        start = time.time()
        add_new_row(arr, mas.get_useful_values())
        time.sleep(0.5 - ((time.time() - start) % 60))


ma = aa.AudioAnalysis("music/closer, the chainsmokers..mp3")
blank_map = create_map_empty()
visualize(blank_map, ma)