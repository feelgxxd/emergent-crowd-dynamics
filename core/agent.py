# core/agent.py
import math
import random

class Agent:
    def __init__(self, x, y):
        self.pos = [float(x), float(y)]
        self.vel = [
            random.uniform(-0.2, 0.2),
            random.uniform(-0.2, 0.2)
        ]

        self.max_speed = 2.0
        self.personal_space = 12.0
        self.mass = 1.0
        self.pressure = 0.0

        self.trail = []

    def apply_force(self, force):
        self.vel[0] += force[0] / self.mass
        self.vel[1] += force[1] / self.mass

    def limit_speed(self):
        speed = math.hypot(self.vel[0], self.vel[1])
        if speed > self.max_speed:
            self.vel[0] = (self.vel[0] / speed) * self.max_speed
            self.vel[1] = (self.vel[1] / speed) * self.max_speed

    def update(self):
        self.limit_speed()
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.dampen()

        self.trail.append(self.pos[:])
        if len(self.trail) > 5:
            self.trail.pop(0)

    def dampen(self, factor=1.0):
        self.vel[0] *= factor
        self.vel[1] *= factor