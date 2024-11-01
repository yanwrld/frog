import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from collections import defaultdict

class Particle:
    def __init__(self, x_width, y_width, mass, temperature, random_walk_strength):
        self.x = random.uniform(0, x_width)
        self.y = random.uniform(0, y_width/2)
        self.mass = mass
        self.bounds = (0, x_width, 0, y_width)
        self.random_walk_strength = random_walk_strength

    def move(self):
        theta = random.uniform(0, 2 * math.pi)
        random_magnitude = random.uniform(0, self.random_walk_strength)
        
        self.x += random_magnitude * math.cos(theta)
        self.y += random_magnitude * math.sin(theta)

        if self.x <= self.bounds[0] or self.x >= self.bounds[1]:
            self.x = max(self.bounds[0], min(self.x, self.bounds[1]))
        if self.y <= self.bounds[2] or self.y >= self.bounds[3]:
            self.y = max(self.bounds[2], min(self.y, self.bounds[3]))

def apply_gravity(p1, p2, gravitational_constant):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dist = math.sqrt(dx**2 + dy**2)
    if dist < 1e-5:
        return
    force = gravitational_constant * p1.mass * p2.mass / dist**2
    fx = force * dx / dist
    fy = force * dy / dist
    p1.x += fx / p1.mass
    p1.y += fy / p1.mass
    p2.x -= fx / p2.mass
    p2.y -= fy / p2.mass

def check_collision(p1, p2):
    # Implementation of collision check
    pass

def resolve_collision(p1, p2):
    # Implementation of collision resolution
    pass

# Spatial partitioning function using a grid-based approach
def partition_particles(particles, cell_size):
    grid = defaultdict(list)
    for p in particles:
        cell_x = int(p.x // cell_size)
        cell_y = int(p.y // cell_size)
        grid[(cell_x, cell_y)].append(p)
    return grid

def simulate(particles, gravitational_constant, cell_size):
    grid = partition_particles(particles, cell_size)
    for cell, cell_particles in grid.items():
        for i, p1 in enumerate(cell_particles):
            for j, p2 in enumerate(cell_particles):
                if i < j:
                    apply_gravity(p1, p2, gravitational_constant)
                    if check_collision(p1, p2):
                        resolve_collision(p1, p2)
            p1.move()
            
        # Check neighboring cells for interactions
        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in neighbor_offsets:
            neighbor_cell = (cell[0] + dx, cell[1] + dy)
            if neighbor_cell in grid:
                for p1 in cell_particles:
                    for p2 in grid[neighbor_cell]:
                        if p1 is not p2:
                            apply_gravity(p1, p2, gravitational_constant)
                            if check_collision(p1, p2):
                                resolve_collision(p1, p2)

# Simulation setup
num_particles = 1000
temperature = 3000
mass = 1
gravitational_constant = 2
random_walk_strength = 50
bounds = [0, 10000, 0, 10000]
cell_size = 10  # Size of each cell for spatial partitioning

particles = [Particle(bounds[1], bounds[3], mass, temperature, random_walk_strength) for _ in range(num_particles)]

# Animation setup
fig, ax = plt.subplots()
ax.set_xlim(bounds[0], bounds[1])
ax.set_ylim(bounds[2], bounds[3])
scat = ax.scatter([p.x for p in particles], [p.y for p in particles])

def update(frame):
    simulate(particles, gravitational_constant, cell_size)
    scat.set_offsets([[p.x, p.y] for p in particles])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=200, interval=10, blit=True)
plt.show()