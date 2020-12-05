import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.widgets import Slider

fig = plt.figure(figsize=(5,5))#,facecolor='black')
ax = p3.Axes3D(fig)
#plt.style.use('dark_background')
#ax = fig.add_subplot(111,xlim=(-1,1),ylim=(-1,1))
ax.set_xlim3d([-1,1])
ax.set_ylim3d([-1,1])
ax.set_zlim3d([-1,1])
#ax.set_aspect('equal')
#ax.grid()
line, = ax.plot([],[],'co')

'''Sliders'''
x_slider_ax = fig.add_axes([0.125 , 0 , .75 , .02])
x_slider = Slider(x_slider_ax, 'x', valmin=-1, valmax=1, valinit=0, orientation='horizontal')
x_slider.label.set_size(10)

y_slider_ax = fig.add_axes([0.125 , 0.03 , .75 , .02])
y_slider = Slider(y_slider_ax, 'y', valmin=-1, valmax=1, valinit=0, orientation='horizontal')
y_slider.label.set_size(10)

z_slider_ax = fig.add_axes([.125 , .06 , .75 , .02])
z_slider = Slider(z_slider_ax, 'z', valmin=-1, valmax=1, valinit=0, orientation='horizontal')
z_slider.label.set_size(10)

'''Animation'''
x,y,z = [],[],[]
def animate(i):

    x.append(x_slider.val)
    y.append(y_slider.val)
    z.append(z_slider.val)

    line.set_data(x[-1],y[-1])
    line.set_3d_properties(z[-1])

    return line,

anim = animation.FuncAnimation(fig,animate,frames=10,interval=1)
plt.show()
