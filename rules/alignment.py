# rules/alignment.py
import math

def alignment(agent, neighbors, weight=1.0):
    if not neighbors:
        return (0.0, 0.0)

    avg_vx = 0.0
    avg_vy = 0.0

    for other in neighbors:
        avg_vx += other.vel[0]
        avg_vy += other.vel[1]

    avg_vx /= len(neighbors)
    avg_vy /= len(neighbors)

    steer_x = avg_vx - agent.vel[0]
    steer_y = avg_vy - agent.vel[1]

    return (steer_x * weight, steer_y * weight)