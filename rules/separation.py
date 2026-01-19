# rules/separation.py
import math

def separation(agent, neighbors, weight=1.0):
    force_x = 0.0
    force_y = 0.0

    for other in neighbors:
        dx = agent.pos[0] - other.pos[0]
        dy = agent.pos[1] - other.pos[1]
        dist = math.hypot(dx, dy)

        if dist == 0:
            continue

        if dist < agent.personal_space:
            strength = (agent.personal_space - dist) / agent.personal_space
            force_x += (dx / dist) * strength
            force_y += (dy / dist) * strength

    return (force_x * weight, force_y * weight)