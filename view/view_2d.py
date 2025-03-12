import tkinter as tk
from .update_affichage import update_affichage

class View2D:
    def __init__(self, arena, robot, mode_affichage=True, taille_carre=20):
        self.arena = arena
        self.robot = robot
        self.mode_affichage = mode_affichage
        self.taille_carre = taille_carre  # Taille du carré que le robot doit dessiner
        self.etape_carre = 0  # Indicateur de quelle étape du carré le robot est (0 = droite, 1 = bas, 2 = gauche, 3 = haut)
        self.vitesse = 2  # Augmenter cette valeur pour augmenter la vitesse du robot

        if self.mode_affichage:
            self.root = tk.Tk()
            self.root.title("Simulation Robot")
            self.canvas = tk.Canvas(self.root, width=self.arena.width * 5, height=self.arena.height * 5, bg="white")
            self.canvas.pack()
            self.draw_arena()

            # Créer un champ de texte pour afficher l'état du robot
            self.console_text = tk.Label(self.root, text="Console:", anchor="w", justify="left")
            self.console_text.pack(fill="both", padx=10, pady=10)

            # Créer un texte déroulant pour afficher les actions
            self.console_output = tk.Label(self.root, text="", anchor="w", justify="left", height=10)
            self.console_output.pack(fill="both", padx=10, pady=10)
            
            self.root.bind("<KeyPress>", self.key_pressed)  # Lier les touches du clavier

    def draw_arena(self):
        """Dessine l'arène, les obstacles et initialise la voiture du robot."""
        for obstacle in self.arena.obstacles:
            self.canvas.create_oval(
                obstacle.x * 5 - obstacle.radius * 5, obstacle.y * 5 - obstacle.radius * 5,
                obstacle.x * 5 + obstacle.radius * 5, obstacle.y * 5 + obstacle.radius * 5,
                fill="red"
            )

        # Taille de la voiture
        car_width = 30
        car_height = 30
        wheel_radius = 5

        body = self.canvas.create_rectangle(
            self.robot.x * 5 - car_width // 2, self.robot.y * 5 - car_height // 2,  
            self.robot.x * 5 + car_width // 2, self.robot.y * 5 + car_height // 2, 
            fill="blue"
        )

        wheels_positions = [
            (self.robot.x * 5, self.robot.y * 5 - car_width // 2),  # Avant gauche
            (self.robot.x * 5, self.robot.y * 5 + car_width // 2),  # Avant droit
        ]
        
        wheels = [
            self.canvas.create_oval(
                wx - wheel_radius, wy - wheel_radius, 
                wx + wheel_radius, wy + wheel_radius, 
                fill="black"
            ) for wx, wy in wheels_positions
        ]

        self.robot_parts = {
            "body": body,
            "wheel_0": wheels[0],
            "wheel_1": wheels[1],
        }

    def check_collision(self):
        """Vérifie si le robot va entrer en collision avec un obstacle."""
        for obstacle in self.arena.obstacles:
            distance = ((self.robot.x - obstacle.x) ** 2 + (self.robot.y - obstacle.y) ** 2) ** 0.5
            if distance <= obstacle.radius + 1:  # Collision si la distance est inférieure au rayon + 1 (distance du robot)
                return True
        return False

    def move_robot(self):
        """Déplace le robot en suivant une trajectoire carrée, mais évite les obstacles."""
        original_direction = self.etape_carre  # Sauvegarder la direction initiale avant le test de collision

        # Vérifier la direction actuelle avant de déplacer le robot
        if self.etape_carre == 0:  # Mouvement vers la droite
            if self.robot.x + self.taille_carre < self.arena.width and not self.check_collision():
                self.robot.x += self.vitesse  # Déplacer vers la droite
            else:
                self.etape_carre = (self.etape_carre + 1) % 4  # Tourner 90° vers le bas
        
        elif self.etape_carre == 1:  # Mouvement vers le bas
            if self.robot.y + self.taille_carre < self.arena.height and not self.check_collision():
                self.robot.y += self.vitesse  # Déplacer vers le bas
            else:
                self.etape_carre = (self.etape_carre + 1) % 4  # Tourner 90° vers la gauche
        
        elif self.etape_carre == 2:  # Mouvement vers la gauche
            if self.robot.x - self.taille_carre >= 0 and not self.check_collision():
                self.robot.x -= self.vitesse  # Déplacer vers la gauche
            else:
                self.etape_carre = (self.etape_carre + 1) % 4  # Tourner 90° vers le haut
        
        elif self.etape_carre == 3:  # Mouvement vers le haut
            if self.robot.y - self.taille_carre >= 0 and not self.check_collision():
                self.robot.y -= self.vitesse  # Déplacer vers le haut
            else:
                self.etape_carre = (self.etape_carre + 1) % 4  # Tourner 90° vers la droite

        # Si une collision a été détectée, changer de direction tout en maintenant la trajectoire du carré
        if original_direction != self.etape_carre:
            self.move_robot()  # Appeler de nouveau le mouvement pour continuer à éviter l'obstacle

    def key_pressed(self, event):
        """Gestion des touches du clavier pour déplacer le robot manuellement."""
        if event.keysym == "Up":
            self.robot.y -= self.vitesse  # Déplacer vers le haut
            self.update_console("Déplacement: Haut")
        elif event.keysym == "Down":
            self.robot.y += self.vitesse  # Déplacer vers le bas
            self.update_console("Déplacement: Bas")
        elif event.keysym == "Left":
            self.robot.x -= self.vitesse  # Déplacer vers la gauche
            self.update_console("Déplacement: Gauche")
        elif event.keysym == "Right":
            self.robot.x += self.vitesse  # Déplacer vers la droite
            self.update_console("Déplacement: Droite")
        
        # Mettre à jour l'affichage
        self.update()

    def update_console(self, message):
        """Met à jour la zone de texte avec les informations du robot."""
        current_text = self.console_output.cget("text")  # Obtenir le texte actuel
        updated_text = current_text + f"\n{message} | Position du robot: ({self.robot.x}, {self.robot.y})"
        self.console_output.config(text=updated_text)  # Mettre à jour le texte dans la zone de texte

    def update(self):
        """Met à jour l'affichage du robot et déplace le robot."""
        self.move_robot()  # Déplacer le robot à chaque mise à jour
        update_affichage(self.canvas, self.robot_parts, self.robot, self.mode_affichage)

    def update_periodically(self):
        """Met à jour l'affichage toutes les 100 ms."""
        self.update()
        self.root.after(100, self.update_periodically)  # Planifier la prochaine mise à jour

    def run(self):
        if self.mode_affichage:
            print("🖥️ Lancement de l'affichage graphique...")
            self.update_periodically()  # Démarrer la mise à jour continue
            self.root.mainloop()  # Lancer Tkinter
        else:
            print(" Exécution en mode console sans affichage graphique")
