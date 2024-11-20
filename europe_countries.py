#https://www.youtube.com/watch?v=6Hk5KyiEktI
#1. display the european map
#2. get the coordinates of a mouse click
#3. get rgb value from said coordinates
#4. mark the country which should be guessed

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np


coordinates = []
rgb = []



def main():
    europe_map = (Image.open(r'assets\europe_map.png')) 

    print(f"Image mode: {europe_map.mode}")

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.2, hspace=0.2)

    ax.imshow(europe_map)
    ax.axis("off")

    def mouse_event(event):
        x, y = int(event.xdata), int(event.ydata)
        coordinates.append((x, y))
        rgb_value = europe_map.getpixel((x, y))
        print(f"RGB value at ({x}, {y}): {rgb_value}")
        rgb.append(rgb_value)
    

    cid = fig.canvas.mpl_connect('button_press_event', mouse_event)

    plt.show()

main()