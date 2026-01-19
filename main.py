import pygame
import math
import random
from core.world import World
from core.simulation import Simulation

WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)

DIST_RADIUS = 80
DIST_FORCE  = 0.6

BASE_RADIUS = 70
OUTER_RADIUS = 25

ATTRACTOR_FORCE = 0.4
ATTRACTOR_RADIUS = 200

HEATMAP_SCALE = 4
HEAT_DECAY = 0.97
HEAT_ADD = 25

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fade = pygame.Surface(screen.get_size())
fade.set_alpha(50)
fade.fill(BG_COLOR)

world = World(WIDTH, HEIGHT, agent_count=75)
sim = Simulation(world)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sim.step()

    screen.blit(fade, (0, 0))

    for a in world.agents:
        p = min(a.pressure, 1.0)
        
        a.local_order = 0.0

        if a.pressure > 0.5:
            jitter = a.pressure * 0.3
            a.apply_force((
                random.uniform(-jitter, jitter),
                random.uniform(-jitter, jitter)
            ))

        if p > 0.05:
            halo_radius = int(10 + 25 * p)
            alpha = int(90 * p)

            halo = pygame.Surface(
                (halo_radius * 2, halo_radius * 2),
                pygame.SRCALPHA
            )

            pygame.draw.circle(
                halo,
                (255, 120, 120, alpha),
                (halo_radius, halo_radius),
                halo_radius,
                2
            )

            screen.blit(
                halo,
                (
                    int(a.pos[0] - halo_radius),
                    int(a.pos[1] - halo_radius)
                )
            )

        neighbors = world.get_neighbors(a, a.personal_space)
        count = len(neighbors)

        if count == 0:
            a.local_order = 0.0
        else:
            vx, vy = a.vel
            speed = math.hypot(vx, vy)

            if speed < 0.01:
                a.local_order = 0.0
            else:
                nx, ny = vx / speed, vy / speed
                acc = 0.0
                valid = 0

                for n in neighbors:
                    nvx, nvy = n.vel
                    ns = math.hypot(nvx, nvy)
                    if ns < 0.01:
                        continue

                    nnx, nny = nvx / ns, nvy / ns
                    acc += nx * nnx + ny * nny
                    valid += 1

                if valid > 0:
                    a.local_order = max(0.0, acc / valid)
                else:
                    a.local_order = 0.0

        vx, vy = a.vel
        speed = (vx * vx + vy * vy) ** 0.5

        trail_layer = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        for i in range(len(a.trail) - 1):
            alpha = int(100 * (i / len(a.trail)))
            pygame.draw.line(
                trail_layer,
                (180, 180, 180, alpha),
                a.trail[i],
                a.trail[i+1],
                1
            )

        MAX_SPEED = 2.5

        MAX_NEIGHBORS = 8
        density = min(count / MAX_NEIGHBORS, 1.0)

        t = min(speed / MAX_SPEED, 1.0)

        BASE_RADIUS = 3
        MAX_RADIUS  = 7

        radius = int(
            BASE_RADIUS + (MAX_RADIUS - BASE_RADIUS) * density
        )

        color = (
            int(50 + 205 * t),       
            int(100 + 100 * (1-t)), 
            int(200 * (1-t))        
        )

        order = a.local_order

        vx, vy = a.vel
        speed = math.hypot(vx, vy)

        if order > 0.25 and speed > 0.1:
            nx, ny = vx / speed, vy / speed

            # agent'ın önünde konum
            offset = 8
            cx = a.pos[0] + nx * offset
            cy = a.pos[1] + ny * offset

            tick_len = 4 + 8 * order

            pygame.draw.line(
                screen,
                (120, 255, 180, int(150 * order)),
                (cx, cy),
                (
                    cx + nx * tick_len,
                    cy + ny * tick_len
                ),
                2
            )

        mx, my = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        for r in (BASE_RADIUS, OUTER_RADIUS):
            s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)

            alpha = 30 if mouse_down else 15
            pygame.draw.circle(
                s,
                (150, 200, 255, alpha),
                (r, r),
                r,
                2
            )
            screen.blit(s, (mx-r, my-r))

            if mouse_down:
                pulse = pygame.Surface((40, 40), pygame.SRCALPHA)
                pygame.draw.circle(
                    pulse,
                    (180, 220, 255, 120),
                    (20, 20),
                    18
                )
                screen.blit(pulse, (mx-20, my-20))

        pygame.draw.circle(
            screen,
            color,
            (int(a.pos[0]), int(a.pos[1])),
            radius
        )

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()

            for agent in world.agents:
                dx = agent.pos[0] - mx
                dy = agent.pos[1] - my
                dist = (dx*dx + dy*dy) ** 0.5

                if dist < DIST_RADIUS and dist > 1:
                    strength = (1 - dist / DIST_RADIUS) * DIST_FORCE
                    agent.apply_force((
                        dx / dist * strength,
                        dy / dist * strength
                    ))

    pygame.display.flip()

pygame.quit()