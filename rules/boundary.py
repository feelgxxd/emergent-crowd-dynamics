# rules/boundary.py
def boundary_force(agent, width, height, margin=50, strength=0.4):
    fx, fy = 0.0, 0.0

    if agent.pos[0] < margin:
        fx += (margin - agent.pos[0]) / margin
    elif agent.pos[0] > width - margin:
        fx -= (agent.pos[0] - (width - margin)) / margin

    if agent.pos[1] < margin:
        fy += (margin - agent.pos[1]) / margin
    elif agent.pos[1] > height - margin:
        fy -= (agent.pos[1] - (height - margin)) / margin

    return (fx * strength, fy * strength)