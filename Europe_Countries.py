from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

europe_map = (Image.open('assets\europe_map.png'))

map_plot = plt.imshow(europe_map)
plt.axis("off")


def mouse_event(event):
    print('x: {} and y: {}'.format(event.xdata, event.ydata))

fig = plt.figure(1)
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)

plt.show()