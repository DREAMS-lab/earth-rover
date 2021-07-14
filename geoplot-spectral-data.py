import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# -rw-rw-r-- 1 jdas jdas  35M Jul 11 15:30 2021-07-11-15-29-02.bag
# -rw-rw-r-- 1 jdas jdas  34M Jul 11 15:28 2021-07-11-15-26-40.bag
# -rw-rw-r-- 1 jdas jdas 8.2M Jul 11 15:25 2021-07-11-15-24-38.bag
# -rw-rw-r-- 1 jdas jdas 7.5M Jul 11 15:24 2021-07-11-15-23-44.bag
# -rw-rw-r-- 1 jdas jdas  11M Jul 11 15:22 2021-07-11-15-22-27.bag
# er_df_spec = pandas.read_csv('/home/jdas/earth-rover-spec-2021-07-11-15-29-02.bag.csv')
# er_df_odom = pandas.read_csv('/home/jdas/earth-rover-odom-2021-07-11-15-29-02.bag.csv')
# er_df_spec = pandas.read_csv('/home/jdas/earth-rover-spec-2021-07-11-15-26-40.bag.csv')
# er_df_odom = pandas.read_csv('/home/jdas/earth-rover-odom-2021-07-11-15-26-40.bag.csv')
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas

er_df_spec = pandas.read_csv('/home/jdas/spec-dreams-annex-2021-07-13-15-44-28.bag.csv')

spec_time_vec = er_df_spec['%time']
spec_wavelengths_vec = er_df_spec[list(map(lambda x: ('field.wavelength%s' % x), range(2048)))]
spec_intensities_vec = er_df_spec[list(map(lambda x: ('field.intensities%s' % x), range(2048)))]

top = cm.get_cmap('jet', 128)
bottom = cm.get_cmap('gray', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')

spec_wavelengths_vec_np = spec_wavelengths_vec.to_numpy()
X = spec_wavelengths_vec_np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = spec_wavelengths_vec_np[0,:]
y = range(spec_wavelengths_vec_np.shape[0])
X,Y = np.meshgrid(x,y)
ax.plot_surface(X, Y, spec_intensities_vec, facecolors=newcmp((X - X.min()) / (X.max() - X.min())),  alpha=0.7, linewidth=0, antialiased=False, shade=False)
plt.xlabel('wavelength (nm)')
plt.ylabel('sample number')
ax.set_zlabel('irradiance (uncalibrated)')

plt.show()
print('done!')


