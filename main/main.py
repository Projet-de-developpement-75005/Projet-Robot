from model import Arena, Robot, Obstacle, update_model
from controller import Controller

def main():
    # Création de l'arène
    arena = Arena(width=200, height=200)
    
    # Création du robot
    robot = Robot(x=50, y=50, direction=0)
    
    # Ajout d'obstacles
    obstacles = [Obstacle(100, 100, 10), Obstacle(150, 50, 5)]
    for obs in obstacles:
        arena.add_obstacle(obs)
    
    # Initialisation du contrôleur
    controller = Controller(robot, obstacles)
    
    # Affichage initial
    print(arena)
    print(robot)
    
    # Déplacements
    controller.deplacer_robot(30)
    print(f"Après déplacement : {robot}")
    
    # Vérification des collisions
    update_model(arena, robot)
    
    # Tourner et avancer
    controller.tourner_robot(45)
    controller.deplacer_robot(20)
    print(f"Après rotation et déplacement : {robot}")
    update_model(arena, robot)
    
    # Vérification de la distance au premier obstacle
    distance = controller.verifier_distance()
    print(f"Distance au plus proche obstacle : {distance:.2f}")
    
    # Dessiner un carré
    print("Le robot dessine un carré :")
    controller.dessiner_carre(20)
    
    
if __name__ == "__main__":
    main()