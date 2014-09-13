import numpy as np
from matplotlib import pylab
import matplotlib.cm as cm

row_imgs = 5
col_imgs = 5

fig, axe = pylab.subplots(row_imgs,col_imgs)

img_arr = in_data.to_numpy()[0]
pylab.ion()
pylab.imshow(img_arr[0,:].reshape(28,28))
pylab.show()