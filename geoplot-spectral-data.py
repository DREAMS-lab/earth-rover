import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas

import os

directory = r'/root/PycharmProjects/earth-rover/'
names = ['spectrometer', 'odometery',]
for filename in os.listdir(directory):
    print(filename)

    if filename.startswith("spectrometer") and filename.endswith(".csv"):
        print(filename)
        er_df_spec = pandas.read_csv(filename)
        fig = plt.figure()

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