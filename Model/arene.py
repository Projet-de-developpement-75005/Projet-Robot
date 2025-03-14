class Arena:
    def __init__(self, width=100, height=100):
        """Initialise l'arène avec des dimensions et une liste d'obstacles."""
        self.width = width
        self.height = height
        self.obstacles = []

    def add_obstacle(self, obstacle):
        """Ajoute un obstacle à l'arène."""
        self.obstacles.append(obstacle)

    def __str__(self):
        return f"Arena({self.width}x{self.height}, {len(self.obstacles)} obstacles)"
    def update_model(arena, robot):
        """Met à jour la position du robot, modifie la direction et vérifie les collisions."""
        print(f"Update: {robot}")
    
        # Si une collision est détectée, change la direction du robot
        for obstacle in arena.obstacles:
            if check_collision(robot, obstacle):
                print(f"⚠️ Collision détectée avec {obstacle}!")
                # Modifier la direction du robot pour l'éviter
                robot.direction = (robot.direction + 90) % 360  # Tourne de 90° (par exemple)
                print(f"Nouvelle direction du robot après la collision : {robot.direction}°")
                return False

        print("✅ Aucun obstacle rencontré.")
        return True

    def check_collision(robot, obstacle):
        """Vérifie si le robot entre en collision avec un obstacle."""
        from math import sqrt
        distance = sqrt((robot.x - obstacle.x)**2 + (robot.y - obstacle.y)**2)
        return distance < obstacle.radius