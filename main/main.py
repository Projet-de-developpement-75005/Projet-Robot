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
    
    
    
if __name__ == "__main__":
    main()