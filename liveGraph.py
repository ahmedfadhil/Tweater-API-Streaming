import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pullData = open("positive.txt", 'r').read()
    lines = pullData.split('\n')
    xar = []
    yar = []
    x = 0
    y = 0

    for line in lines:
        x += 1
        if "pos" in line:
            y += 1
        elif "neg" in line:
            y -= 1
        xar.append(x)
        yar.append(y)
    ax1.clear()
    ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
