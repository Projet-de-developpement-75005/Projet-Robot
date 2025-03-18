import time
import random
import math
import msvcrt  # Pour la détection de touche en mode console (Windows)
from Model.arene import Arena
from Model.robot import Robot
from controller.controller import SquareDrawer
from view.view_2d import GUI

def main():
    mode = input("Voulez-vous un affichage graphique ? (y/n): ")
    graphical = (mode.lower() == 'y')

    # Initialisation du modèle
    arena = Arena(width=400, height=400)
    robot = Robot(x=50, y=50, direction=0)
    square_controller = SquareDrawer(robot, side_length=100)
    start_time = time.time()

    if graphical:
        gui = GUI(arena, robot)
        drawing_square = False  # Indique si le dessin du carré est en cours

        def square_drawing_step():
            nonlocal drawing_square
            print("square_drawing_step appelé...")
            if not square_controller.is_done():
                square_controller.update()
                gui.draw()
                gui.window.after(100, square_drawing_step)
            else:
                drawing_square = False
                print("Carré dessiné.")

        def on_key(event):
            nonlocal drawing_square, square_controller
            print("Touche pressée :", event.keysym)
            if not drawing_square:
                print("Arrêt du déplacement aléatoire et lancement du dessin du carré...")
                # Active l'enregistrement de la trace et l'efface
                robot.trace_active = True
                robot.trace = [(robot.x, robot.y)]
                # Réinitialisation de la séquence de dessin
                square_controller.current_side = 0
                square_controller.distance_moved = 0
                square_controller.done = False
                drawing_square = True
                square_drawing_step()

        gui.window.bind("<Key>", on_key)

        def simulation_loop():
            elapsed = time.time() - start_time
            if not drawing_square:
                # Désactive la trace en mode déplacement aléatoire
                robot.trace_active = False
                # Calculer la prochaine position potentielle
                new_x = robot.x + robot.step_size * math.cos(math.radians(robot.direction))
                new_y = robot.y + robot.step_size * math.sin(math.radians(robot.direction))
                # Vérifier que la prochaine position reste dans l'arène
                if new_x < 0 or new_x > arena.width or new_y < 0 or new_y > arena.height:
                    # Si elle sort, on rebondit en inversant la direction
                    robot.rotate(180)
                else:
                    robot.move_forward(robot.step_size)
                    # Appliquer une rotation aléatoire entre -10° et 10°
                    robot.rotate(random.randint(-10, 10))
            print(f"Temps écoulé: {elapsed:.2f} s - Position: ({robot.x:.2f}, {robot.y:.2f}), Angle: {robot.direction}°")
            gui.draw()
            gui.window.after(100, simulation_loop)

        simulation_loop()
        gui.mainloop()

    else:
        print("Mode console activé. Appuyez sur une touche pour dessiner le carré.")
        while True:
            # Calcul de la position potentielle
            new_x = robot.x + robot.step_size * math.cos(math.radians(robot.direction))
            new_y = robot.y + robot.step_size * math.sin(math.radians(robot.direction))
            if new_x < 0 or new_x > arena.width or new_y < 0 or new_y > arena.height:
                robot.rotate(180)
            else:
                robot.move_forward(robot.step_size)
                robot.rotate(random.randint(-10, 10))
            elapsed = time.time() - start_time
            print(f"Temps écoulé: {elapsed:.2f} s - Position: ({robot.x:.2f}, {robot.y:.2f}), Angle: {robot.direction}°")
            time.sleep(0.1)
            if msvcrt.kbhit():
                msvcrt.getch()  # Consomme la touche
                print("Touche détectée, arrêt du déplacement aléatoire et lancement du dessin du carré...")
                # Active la trace pour le dessin du carré et l'efface
                robot.trace_active = True
                robot.trace = [(robot.x, robot.y)]
                # Réinitialisation du contrôleur pour dessiner le carré
                square_controller.current_side = 0
                square_controller.distance_moved = 0
                square_controller.done = False
                while not square_controller.is_done():
                    square_controller.update()
                    print(f"Carré en cours: Position: ({robot.x:.2f}, {robot.y:.2f}), Angle: {robot.direction}°")
                    time.sleep(0.1)
                print("Carré dessiné.")

if __name__ == "__main__":
    main()
