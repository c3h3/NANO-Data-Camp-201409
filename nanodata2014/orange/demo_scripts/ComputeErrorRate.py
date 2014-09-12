import numpy as np

err_arr = in_data.to_numpy()[0]
err_rate = np.abs(err_arr[:,0] - err_arr[:,1]).sum() / err_arr.shape[0]
print "err_rate = ",err_rate
