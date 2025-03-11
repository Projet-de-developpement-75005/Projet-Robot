

from Model import Arena, Robot, Obstacle, update_model
from controller import Controller
from view import View2D
import time
import threading


def main():
    # Création de l'arène
    arena = Arena(width=200, height=200)
    
    # Création du robot
    robot = Robot(x=50, y=50, direction=0)
    
    # Ajout d'obstacles
    obstacles = [Obstacle(100, 100, 10), Obstacle(150, 50, 5)]
    for obs in obstacles:
        arena.add_obstacle(obs)
    
    # Initialisation du contrôleur et de la vue
    controller = Controller(robot, obstacles)
    view = View2D(arena, robot, mode_affichage=True)
    
    # Fonction de mise à jour continue du modèle et de l'affichage
    def simulation():
        start_time = time.time()  # Début du chronomètre
        try:
            while True:
                controller.deplacer_robot(5)
                update_model(arena, robot)
                distance = controller.verifier_distance()
                elapsed_time = time.time() - start_time  # Temps écoulé
                
                print(f"Position : {robot}, Distance obstacle : {distance:.2f}, Temps écoulé : {elapsed_time:.2f}s")
                
                view.update()  # Mettre à jour l'affichage graphique
                time.sleep(1)  # Pause pour observer le mouvement
        except KeyboardInterrupt:
            print("\nArrêt du programme.")
    
    # Lancer la simulation en parallèle avec Tkinter
    thread = threading.Thread(target=simulation, daemon=True)
    thread.start()
    
    view.run()  # Lance l'interface graphique


if __name__ == "__main__":
    main()

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
    
    
    start_time = time.time()  # Début du chronomètre
    
    try:
        while True:
            controller.deplacer_robot(5)
            update_model(arena, robot)
            distance = controller.verifier_distance()
            timee = time.time() - start_time  # Temps écoulé

            print(f"Position : {robot}, Distance obstacle : {distance:.2f}, Temps écoulé : {timee:.2f}s")
            time.sleep(1)  # Pause pour observer le mouvement
    except KeyboardInterrupt:
        print("\nArrêt du programme.")


    # Dessiner un carré
    print("Le robot dessine un carré :")
    controller.dessiner_carre(20)

if __name__ == "__main__":
    main()