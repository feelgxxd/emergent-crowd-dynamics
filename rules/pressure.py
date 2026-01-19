# rules/pressure.py
import math

def pressure(agent, neighbors):
    if not neighbors:
        return 1.0

    count = 0
    for n in neighbors:
        dx = agent.pos[0] - n.pos[0]
        dy = agent.pos[1] - n.pos[1]
        dist = math.hypot(dx, dy)

        if dist < agent.personal_space:
            count += 1

    MAX_PRESSURE_NEIGHBORS = 6

    p = 1.0 - min(count / MAX_PRESSURE_NEIGHBORS, 1.0)

    return p