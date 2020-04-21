from tkinter import filedialog
from vpython import *
from tkinter import *
import TerrainFunctions as T

root = Tk()
root.withdraw()                             # Hides tkinter window
file_path = filedialog.askopenfilename()    # Opens File menu dialog
root.destroy()                              # terminate tkinter window


def change_base_color(m):
    """
    Drop down menu to change base_color
    """
    val = m.selected
    if val == 'blue':
        T.base_color = color.blue
    elif val == 'red':
        T.base_color = color.red
    elif val == 'brown':
        T.base_color = T.brown
    elif val == 'green':
        T.base_color = color.green
    elif val == 'orange':
        T.base_color = color.orange
    elif val == 'purple':
        T.base_color = color.purple
    elif val == 'yellow':
        T.base_color = color.yellow
    elif val == 'white':
        T.base_color = color.white


menu(label='base color', choices=['blue', 'red', 'brown', 'green', 'orange', 'purple', 'yellow', 'white'],
     index=0, bind=change_base_color)


def change_ground_color(m):
    """
    Drop down menu to change ground_color
    """
    val = m.selected
    if val == 'brown':
        T.ground_color = T.brown
    elif val == 'blue':
        T.ground_color = color.blue
    elif val == 'red':
        T.ground_color = color.red
    elif val == 'green':
        T.ground_color = color.green
    elif val == 'orange':
        T.ground_color = color.orange
    elif val == 'purple':
        T.ground_color = color.purple
    elif val == 'yellow':
        T.ground_color = color.yellow
    elif val == 'white':
        T.ground_color = color.white


menu(label='ground color', choices=['brown', 'blue', 'red', 'green', 'orange', 'purple', 'yellow', 'white'],
     index=1, bind=change_ground_color)


def change_mid_color(m):
    """
    Drop down menu to change mid_color
    """
    val = m.selected
    if val == 'green':
        T.mid_color = color.green
    elif val == 'blue':
        T.mid_color = color.blue
    elif val == 'red':
        T.mid_color = color.red
    elif val == 'brown':
        T.mid_color = T.brown
    elif val == 'orange':
        T.mid_color = color.orange
    elif val == 'purple':
        T.mid_color = color.purple
    elif val == 'yellow':
        T.mid_color = color.yellow
    elif val == 'white':
        T.mid_color = color.white


menu(label='mid color', choices=['green', 'blue', 'red', 'brown', 'orange', 'purple', 'yellow', 'white'],
     index=0, bind=change_mid_color)


def change_peak_color(m):
    """
    Drop down menu to change peak_color
    """
    val = m.selected
    if val == 'white':
        T.peak_color = color.white
    elif val == 'blue':
        T.peak_color = color.blue
    elif val == 'red':
        T.peak_color = color.red
    elif val == 'brown':
        T.peak_color = T.brown
    elif val == 'green':
        T.peak_color = color.green
    elif val == 'orange':
        T.peak_color = color.orange
    elif val == 'purple':
        T.peak_color = color.purple
    elif val == 'yellow':
        T.peak_color = color.yellow


menu(label='peak color', choices=['white', 'blue', 'red', 'brown', 'green', 'orange', 'purple', 'yellow'],
     index=3, bind=change_peak_color)

if __name__ == '__main__':
    T.perform_3d_generation(file_path)
