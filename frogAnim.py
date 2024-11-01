import matplotlib.pyplot as plt
import matplotlib.animation as animation

from frog import initialize, move

# parameters
xInit = [0, 500]
yInit = [0, 1000]

xBounds = [0, 1000]
yBounds = [0, 1000]
num_points = 1000
radius = 25
num_frames = 100

# initialize points
points = [initialize(xInit, yInit) for _ in range(num_points)]

# set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(xBounds)
ax.set_ylim(yBounds)
scat = ax.scatter([p[0] for p in points], [p[1] for p in points])

# plot a rectangle around the initial particle area
box = plt.Rectangle(
    (xInit[0], yInit[0]),
    xInit[1] - xInit[0],
    yInit[1] - yInit[0],
    fill=None,
    edgecolor="r",
)
ax.add_patch(box)


def update(frame):
    global points
    points = [move(xBounds, yBounds, p, radius) for p in points]
    scat.set_offsets(points)
    return (scat,)


# create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# show animation
plt.show()
