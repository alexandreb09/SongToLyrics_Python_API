from io import StringIO
import pandas as pd


TESTDATA = StringIO("""
     Flag                  Timestamp
1   begin  2019-10-25 09:39:39.914889
2     end  2019-10-25 09:41:09.103102
3   begin  2019-10-25 10:39:58.352073
4     end  2019-10-25 10:40:06.266782
5   begin  2019-10-25 16:35:22.485574
6     end  2019-10-27 09:50:31.713192
7   begin  2019-10-26 16:35:22.485574
8     end   2019-10-27 09:50:31.713192
9   begin  2019-10-29 14:04:33.095633
10    end  2019-10-29 14:05:07.639344
11  begin  2019-10-29 14:13:07.924966
12    end  2019-10-29 14:13:08.888890
""")

# df = pd.read_csv(TESTDATA, sep=r"\s{2,}")


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D                 
from mpl_toolkits.mplot3d import proj3d                 
import matplotlib.pylab as pl

fig=pl.figure()
ax = Axes3D(fig)

x=[0.02554897, 0.02587839, 0.02623991, 0.02663096, 0.02704882, 0.02749103, 0.02795535, 0.02844018, 0.02894404, 0.02946527, 0.03000235] 
y=[0.04739086, 0.0460989,  0.04481555, 0.04354088, 0.04227474, 0.04101689, 0.03976702, 0.03852497, 0.03729052, 0.0360633,  0.03484293] 
z=[1.05764017e-18, 1.57788964e-18, 2.00281370e-18, 2.40500994e-18, 2.80239565e-18, 3.19420769e-18, 3.58001701e-18, 3.96024361e-18, 4.33484911e-18, 4.70364652e-18, 5.06672528e-18] 


x_point = 0.02577341
y_point = 0.04400918
z_point = 0.0001368

ax.azim = 95  # y rotation (default=270)
ax.elev = 23 # x rotation (default=0)

ax.scatter(x_point, y_point, z_point, color='green')
ax.plot3D(x,y,z)

plt.show()