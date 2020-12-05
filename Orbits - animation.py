import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

x = []
y = []
n = 80 #Number of runners.
m = 10000 #length of the field
th0 = []
dth = .1
for i in range(n):
    th0.append([0])
    x.append([0])
    y.append([i])
    for j in range(m):
        th0[i].append(th0[i][-1]+dth/(i+1))
        x[i].append((i+1)*np.cos(th0[i][-1]))
        y[i].append((i+1)*np.sin(th0[i][-1]))

fig = plt.figure(figsize=(6,6), facecolor='black')
ax = plt.axes(frameon=False, xlim=(np.min(x)-1,np.max(x)+1), ylim=(np.min(y)-1,np.max(y)+1))
ax.set_aspect('equal')

lines = []
for i in range(n):
    l = ax.plot([], [], '.', markersize=2)[0]
    lines.append(l)

X, Y = [], []
def animate(i):
    i = i*41%m
    for j in range(n):
        X.append([])
        Y.append([])
        
        xs = x[j][i]
        ys = y[j][i]
        
        X[j].append(xs)
        Y[j].append(ys)

    xlist = [X[j][-1] for j in range(n)]
    ylist = [Y[j][-1] for j in range(n)]

    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])

    return lines

anim = anime.FuncAnimation(fig, animate, interval=1, repeat=True)
plt.show()
