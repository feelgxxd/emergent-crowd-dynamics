# rules/cohesion.py
def cohesion(agent, neighbors, weight=0.05, min_neighbors=2):
    if len(neighbors) == 0:
        return (0.0, 0.0)

    if len(neighbors) < min_neighbors:
        cx = sum(n.pos[0] for n in neighbors) / len(neighbors)
        cy = sum(n.pos[1] for n in neighbors) / len(neighbors)

        dx = cx - agent.pos[0]
        dy = cy - agent.pos[1]

        return (dx * weight, dy * weight)

    return (0.0, 0.0)