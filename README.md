# Emergent Crowd Dynamics

An agent-based simulation exploring how complex crowd behavior can emerge from simple local rules and interactions.
This project focuses on understanding collective motion, avoidance, and flow patterns without centralized control.

## 🧠 Overview

Crowd behavior in games and simulations often feels intelligent despite being driven by simple, local decision-making.

This project investigates:
- How individual agents respond to nearby agents and obstacles
- How local rules scale into global movement patterns
- How small parameter changes affect overall crowd flow

The system is designed to be easily observable, tweakable, and extendable.

## 👥 Core Concepts

- **Agents**  
  Each agent operates independently and has no knowledge of the global system.

- **Local Perception**  
  Agents sense only nearby neighbors within a limited radius.

- **Rule-Based Behavior**  
  Movement emerges from weighted steering forces such as:
  - Separation (avoid crowding)
  - Alignment (match nearby velocity)
  - Cohesion (stay with the group)

## ⚙️ How It Works

1. **Perception Phase**  
   Each agent queries nearby agents within a configurable range.

2. **Steering Calculation**  
   Steering forces are computed based on local rules and combined using weighted sums.

3. **Movement Update**  
   The resulting velocity is applied, producing smooth, continuous motion.

4. **Iteration**  
   Repeated updates produce emergent crowd-level behavior.

No agent is aware of the overall structure, coordination arises purely from interaction.

## 🧩 Technical Highlights

- Agent-based simulation architecture
- Local neighborhood queries
- Continuous vector-based movement
- Deterministic updates for reproducibility
- Clear separation between logic and visualization

## 🤔 Why I Built This

I built this project to better understand how believable crowd behavior can emerge without complex AI or global planning.
The goal was to explore systems that feel alive while remaining computationally simple a principle that applies strongly to games and interactive simulations.

## Controls
- Left click = apply local repulsion force
- Passive mouse presence influences nearby agents

Rather than scripting behavior, the system observes and visualizes how order and stress emerge from local interactions.
This project is intentionally minimal and exploratory, designed as a visual thinking tool rather than a finished product.

![GIF 19 01 2026 05-17-31](https://github.com/user-attachments/assets/b755c09a-c10b-476a-b519-8a0f7fa7e4f4)
