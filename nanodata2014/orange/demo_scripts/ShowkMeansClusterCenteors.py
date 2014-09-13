img_arr = in_data.to_numpy()[0]
n_images = img_arr.shape[0]

import numpy as np
from matplotlib import pylab
import matplotlib.cm as cm
pylab.ion()

row_imgs = 1
col_imgs = n_images

fig, axe = pylab.subplots(row_imgs,col_imgs)



img_idx = 0
for ax in axe.flatten():
    ax.imshow(img_arr[img_idx,:].reshape(28,28),cmap=cm.gray)
    img_idx = img_idx + 1


pylab.show()