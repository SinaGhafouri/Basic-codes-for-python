import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.axis([-5,5,-3,3]);

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(-np.pi,np.pi,300)
    y = np.sin(x*4*i/20)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=1000, interval=20, blit=True)

plt.show()
