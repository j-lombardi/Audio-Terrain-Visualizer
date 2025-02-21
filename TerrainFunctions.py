from vpython import *
import AudioAnalysis as aa
import time
import threading
from pydub.playback import play

# Define global color options
brown = vec(0.545, 0.27, 0.074)
base_color = color.blue
ground_color = brown
mid_color = color.green
peak_color = color.white

# Setting camera up
scene.autoscale = True
scene.camera.rotate(angle=55)
scene.camera.pos = vector(132, 15, 46)
scene.width = 1280
scene.height = 800


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
            arr[i][j] = box(pos=vector(i, h / 2, j), axis=vector(10,1,15), length=1, width=1, height=h, color=color.cyan)
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

        if arr[0][i].height > 12:
            arr[0][i].color = peak_color
        elif arr[0][i].height > 6:
            arr[0][i].color = mid_color
        elif arr[0][i].height > 3:
            arr[0][i].color = ground_color
        else:
            arr[0][i].color = base_color

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
    song_data = mas.normalize()
    play_song_thread.start()

    # Visualize a new row every 0.5 seconds
    for i in song_data:
        start = time.time()
        add_new_row(arr, i)
        timer = 0.5 - ((time.time() - start) % 60)  # buffer loop in case it runs too fast
        if timer >= 0:
            time.sleep(timer)


def perform_3d_generation(file_path):
    """
    Main driver to combine all functionality of terrain generation and audio analysis.
    :param file_path: File path of local mp3 or wav song file
    """
    ma = aa.AudioAnalysis(file_path)
    blank_map = create_map_empty()
    visualize(blank_map, ma)
