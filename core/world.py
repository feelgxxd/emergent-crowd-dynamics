# core/world.py
import random
from core.agent import Agent

class World:
    def __init__(self, width, height, agent_count):
        self.width = width
        self.height = height
        self.agents = []

        for _ in range(agent_count):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            self.agents.append(Agent(x, y))

    def get_neighbors(self, agent, radius):
        neighbors = []
        for other in self.agents:
            if other is agent:
                continue
            dx = agent.pos[0] - other.pos[0]
            dy = agent.pos[1] - other.pos[1]
            if dx*dx + dy*dy < radius*radius:
                neighbors.append(other)
        return neighbors