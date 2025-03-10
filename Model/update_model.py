
def update_model(arena, robot):
    """Met à jour la position du robot et vérifie les collisions."""
    print(f"Update: {robot}")
    for obstacle in arena.obstacles:
        if check_collision(robot, obstacle):
            print(f"⚠️ Collision détectée avec {obstacle}!")
            return
    print("✅ Aucun obstacle rencontré.")
    
def check_collision(robot, obstacle):
    """Vérifie si le robot entre en collision avec un obstacle."""
    from math import sqrt
    distance = sqrt((robot.x - obstacle.x)**2 + (robot.y - obstacle.y)**2)
    return distance < obstacle.radius


