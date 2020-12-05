import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

x = []
y = []
n = 10 #Number of runners.
m = 200 #length of the field
for i in range(n):
    x.append([0])
    y.append([i])
    for j in range(m):
        x[i].append(x[i][-1]+np.random.rand())
        y[i].append(y[i][-1])

fig = plt.figure(facecolor='black')
ax = plt.axes(frameon=False, xlim=(min(min(x)),max(max(x))), ylim=(min(min(y))-1,max(max(y))+1))
#ax.set_xticks(range(0,m,10))
#ax.tick_params(axis='x', colors='red')
ax.set_yticks(range(n))
ax.tick_params(axis='y', colors='red')

lines = []
for i in range(n):
    lines.append(ax.plot([], [], 'o')[0])

X, Y = [], []
def animate(i):
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
anim = anime.FuncAnimation(fig, animate, frames=m, interval=10)
plt.show()
