from vpython import *
import AudioAnalysis as aa
import time
import threading
from pydub.playback import play


def create_map_empty():
    """
    Build an empty heighmap as a base to build blocks on
    :return:
        arr: 2D array of VPython Box elements
    """
    cols, rows = (100, 100)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(cols):
        for j in range(rows):
            h = 1
            arr[i][j] = box(pos=vector(i, h / 2, j), length=1, width=1, height=h, color=color.cyan)
    return arr


def shift(arr):
    """
    Shifts all rows of boxs back one row
    :param
        arr: 2D Array of VPython Box elements
    :return:
        No return, this will adjust the input arr to allow for a new row to be added
    """
    for i in range(99, 0, -1):
        for j in range(99, -1, -1):
            arr[i][j].height = arr[i-1][j].height
            arr[i][j].color = arr[i - 1][j].color
            arr[i][j].pos.y = arr[i][j].height / 2


def add_new_row(arr, arr2):
    """
    Adds a new row of boxes ot the end start the 2D box map
    :param
        arr: The original 2D VPython Box array (what is displayed on screen)
        arr2: List of new height values to be added onto the start of the 2D Vpython Box array
    :return:
        No returns, updates the current output map with the new row and removes any extra rows on the end
    """
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
            arr[0][i].color = color.red
        arr[0][i].pos.y = arr[0][i].height / 2


def visualize(arr, mas):
    """
    Main driving loop for the visualization process. Takes in an AudioAnalysis object and builds terrain based
        on the output returned from the object.
    :param
        arr: 2D VPython Box array with all the box heights
        mas: AudioAnalysis object preloaded with song file
    :return:
        This will perform the audio visualization!
    """
    play_song_thread = threading.Thread(target=play, args=(mas.song,))
    play_song_thread.start()
    song_data = mas.normalize()
    for i in song_data:
        start = time.time()
        add_new_row(arr, i)
        timer = 0.5 - ((time.time() - start) % 60)
        if timer >= 0:
            time.sleep(timer)


ma = aa.AudioAnalysis("music/example_busta.mp3")
blank_map = create_map_empty()
visualize(blank_map, ma)
