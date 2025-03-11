def update_affichage(canvas, robot_parts, robot, mode_affichage):
    """
    Met à jour l'affichage du robot sous forme d'une voiture avec 4 roues.
    """
    if mode_affichage:
        x, y = robot.x, robot.y
        car_width = 30
        car_height = 30
        wheel_radius = 5

        # Mettre à jour le corps de la voiture (rectangle)
        canvas.coords(
            robot_parts["body"], 
            x - car_width // 2, y - car_height // 2, 
            x + car_width // 2, y + car_height // 2
        )

        # Mettre à jour les roues (cercles)
        wheels_positions = [
            (x , y - car_width // 2),  # Avant gauche
            (x , y + car_width // 2),  # Avant droit
            
        ]
        
        for i, (wx, wy) in enumerate(wheels_positions):
            wheel_key = "wheel_left" if i == 0 else "wheel_right"
            canvas.coords(
                robot_parts[f"wheel_{i}"], 
                wx - wheel_radius, wy - wheel_radius, 
                wx + wheel_radius, wy + wheel_radius
            )
