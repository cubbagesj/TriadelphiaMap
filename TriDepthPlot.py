# TriDepthPlot.py -
#
# Program to create a contour plot of the Triadelphia reservoir
# using bathymetry data.  The contour plot will be used to
# make a 3D carving on the X-carve

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# First read in the data to a pandas dataframe
datafilename = 'TriadelphiaBathy.csv'
data = pd.read_table(datafilename, sep=',')

# Create the contours using tricontour to triangulate the
# irregular data

levels = 10
plt.tricontourf(data.Easting, data.Northing, data.Depth, levels, cmap='binary' )
#plt.tricontour(data.Easting, data.Northing, data.Depth, levels, cmap='Greys' )

# make plot square
plt.axes().set_aspect('equal')

# Turn off axis
plt.axis('off')

# Add a scale
plt.colorbar(ticks=[0,2,4,6,8,10,12,14,16,18,20])

# You can limit the part of the lake plotted using the limits
#plt.xlim((325500, 327000))
#plt.ylim((4339980, 4340500))

# Output the image
plt.savefig('LakeBtm.png', dpi=600, bbox_inches='tight')

plt.show()
