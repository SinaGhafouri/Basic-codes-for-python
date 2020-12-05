import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dt = .001
g = -9.81
b = 1 #Drag coefficient
m = 10 #Mass

v0 = 10 #Initial velocity
xf, yf = -4, 3 #Final destination.
dr = .01 #Range for final destination.

collision = False #To check if it is collided.
for theta in np.arange(90, 180, .05): #Loop for changing theta.
    vx = [v0*np.cos(theta*np.pi/180)]
    vy = [v0*np.sin(theta*np.pi/180)]
    x = [0] 
    y = [0]
    i = 0 #counter for while loop
    while True: 
        vx.append(vx[i] - b*vx[i]/m*dt)
        x.append(x[i] + vx[i+1]*dt)

        vy.append(vy[i] + g*dt - b*vy[i]/m*dt)
        y.append(y[i] + vy[i+1]*dt)

        if x[-1] >= xf-dr and x[-1] <= xf+dr and y[-1] >= yf-dr and y[-1] <= yf+dr:
            if collision == False:
                print('Collided :)')
                print('Theta = ', theta)
            collision = True

        elif y[-1]<yf-dr and vy[-1]<0 or abs(x[-1])>abs(xf)+np.sign(xf)*dr and np.sign(xf)*vx[-1]>0: break #If there is no hope for collision.

        i += 1

    if collision == True: break #If collided

if collision == False: print('Didn\'t collide :(')

plt.plot(x,y, 'r-')
plt.plot(xf, yf, 'b*')
plt.show()
    
'''Animation'''
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(min(x)-1, max(x)+1), ylim=(min(y)-1, max(y)+1))
ax.set_aspect('equal')
ax.grid()
line1, = ax.plot([], [], 'r*')
line2, = ax.plot([], [], 'b*')
line3, = ax.plot([], [], 'y-.')

def animate(i):
    r = [x[i], y[i]]
    line1.set_data(r[0], r[1])
    line2.set_data(xf, yf)
    line3.set_data(x[i::-1], y[i::-1])
    return line3, line1, line2

ani = animation.FuncAnimation(fig, animate, len(x), interval=10, blit=True)
plt.show()
