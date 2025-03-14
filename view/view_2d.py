import tkinter as tk
import time

class View2D:
    def __init__(self, arena, robot, mode_affichage=True):
        self.arena = arena
        self.robot = robot
        self.mode_affichage = mode_affichage
        
        if self.mode_affichage:
            self.root = tk.Tk()
            self.root.title("Simulation Robot")
            self.canvas = tk.Canvas(self.root, width=self.arena.width, height=self.arena.height, bg="white")
            self.canvas.pack()
            self.draw_arena()
        
    def draw_arena(self):
        """Dessine l'arène, les obstacles et initialise la voiture du robot."""
        # Dessiner les obstacles
        for obstacle in self.arena.obstacles:
            self.canvas.create_oval(
                obstacle.x - obstacle.radius, obstacle.y - obstacle.radius,
                obstacle.x + obstacle.radius, obstacle.y + obstacle.radius,
                fill="red"
            )

        # Taille de la voiture
        car_width = 30
        car_height = 30
        wheel_radius = 5

        # Dessiner le corps de la voiture
        body = self.canvas.create_rectangle(
            self.robot.x - car_width // 2, self.robot.y - car_height // 2, 
            self.robot.x + car_width // 2, self.robot.y + car_height // 2,
            fill="blue"
        )

        # Dessiner les roues
        wheels_positions = [
            (self.robot.x , self.robot.y - car_width // 2),  # Avant gauche
            (self.robot.x , self.robot.y + car_width // 2),  # Avant droit
           
        ]
        
        wheels = [
            self.canvas.create_oval(
                wx - wheel_radius, wy - wheel_radius, 
                wx + wheel_radius, wy + wheel_radius, 
                fill="black"
            ) for wx, wy in wheels_positions
        ]

        # Stocker les éléments du robot
        self.robot_parts = {
            "body": body,
            "wheel_0": wheels[0],
            "wheel_1": wheels[1],
            
        }

    def update(self):
        """Met à jour l'affichage du robot sous forme de voiture."""
        update_affichage(self.canvas, self.robot_parts, self.robot, self.mode_affichage)

    def update_periodically(self):
        """Met à jour l'affichage toutes les 100 ms."""
        self.update()
        self.root.after(100, self.update_periodically)  # Planifier la prochaine mise à jour

    def run(self):
        if self.mode_affichage:
            print("🖥️ Lancement de l'affichage graphique...")
            self.update_periodically()  # Démarre la mise à jour continue
            self.root.mainloop()  # Lance Tkinter pour afficher la fenêtre
        else:
            print("Affichage graphique désactivé")
    
    def update_affichage(canvas, robot_parts, robot, mode_affichage):
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

            #Mettre à jour les roues (cercles)
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
