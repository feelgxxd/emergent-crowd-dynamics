# core/simulation.py
from rules.separation import separation
from rules.alignment import alignment
from rules.pressure import pressure
from rules.boundary import boundary_force
from rules.cohesion import cohesion
import random

class Simulation:
    def __init__(self, world):
        self.world = world

        self.sep_weight = 1.5
        self.align_weight = 0.8

    def step(self):
        for agent in self.world.agents:
            neighbors = self.world.get_neighbors(
                agent,
                agent.personal_space * 1.2
            )

            sep = separation(agent, neighbors, self.sep_weight)
            align = alignment(agent, neighbors, self.align_weight)
            
            coh = (0.0, 0.0)
            if len(neighbors) > 0:
                coh = cohesion(agent, neighbors)

            agent.apply_force(sep)
            agent.apply_force(align)
            agent.apply_force(coh)

            bound = boundary_force(agent, self.world.width, self.world.height)
            agent.apply_force(bound)
            
            p = pressure(agent, neighbors)

            agent.pressure = 1.0 - p
            print(agent.pressure)

            MIN_FLOW = 0.80

            flow = MIN_FLOW + (1.0 - MIN_FLOW) * p

            agent.vel[0] *= flow
            agent.vel[1] *= flow

            
            noise = (
                random.uniform(-0.03, 0.03),
                random.uniform(-0.03, 0.03)
            )
            agent.apply_force(noise)

        for agent in self.world.agents:
            agent.update()