from Model import Arena, Robot, Obstacle, update_model
from controller import Controller
from view import View2D
import time
import threading
import queue


def main():
    # Création de l'arène
    arena = Arena(width=500, height=500)
    
    # Création du robot
    robot = Robot(x=50, y=50, direction=0)
    
    # Ajout d'obstacles
    obstacles = [Obstacle(150, 150, 10), Obstacle(150, 60, 5)]
    for obs in obstacles:
        arena.add_obstacle(obs)

    # Demande à l'utilisateur
    mode_affichage = input("Voulez-vous utiliser l'affichage graphique ? (o/n) : ").strip().lower() == 'o'
    dessiner_carre = input("Voulez-vous que le robot dessine un carré ? (o/n) : ").strip().lower() == 'o'

    # Initialisation du contrôleur et de la vue
    controller = Controller(robot, obstacles, arena)
    view = View2D(arena, robot, mode_affichage=mode_affichage)
    
    # Queue pour passer les mises à jour entre les threads
    update_queue = queue.Queue()

    if dessiner_carre:
        controller.dessiner_carre(longueur_cote=30)  # Longueur du côté du carré

    # Fonction de mise à jour continue du modèle et de l'affichage
    def simulation():
        start_time = time.time()  # Début du chronomètre
        try:
            while True:
                if not update_model(arena, robot):  
                    break  # Stoppe la boucle en cas de collision
                
                controller.deplacer_robot(5)
                update_model(arena, robot)
                distance = controller.verifier_distance()
                elapsed_time = time.time() - start_time  # Temps écoulé
                
                # Ajoutez les informations à la queue pour traitement par le thread principal
                update_queue.put((robot, distance, elapsed_time))

                time.sleep(0.3)  # Pause pour observer le mouvement

        except KeyboardInterrupt:
            print("\nArrêt du programme.")

    # Lancer la simulation dans un thread séparé
    thread = threading.Thread(target=simulation, daemon=True)
    thread.start()

    if mode_affichage:
        # Fonction pour mettre à jour l'affichage à intervalle régulier
        def update_graphique():
            if not update_queue.empty():
                try:
                    robot, distance, elapsed_time = update_queue.get_nowait()
                    print(f"Position : {robot}, Distance obstacle : {distance:.2f}, Temps écoulé : {elapsed_time:.2f}s")
                    view.update()  # Mettre à jour l'affichage graphique
                except queue.Empty:
                    pass
            
            # Planifier une nouvelle mise à jour dans 100 ms
            view.root.after(100, update_graphique)

        # Démarrer la mise à jour graphique
        update_graphique()

        # Lancer Tkinter dans le thread principal
        view.root.mainloop()

if __name__ == "__main__":
    main()
