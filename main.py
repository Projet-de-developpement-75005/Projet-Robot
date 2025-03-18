import time
from Model.arene import Arena
from Model.robot import Robot
from controller.controller import SquareDrawer
from view.view_2d import GUI

def main():
    # Initialisation de l'arène et du robot
    arena = Arena(width=400, height=400)
    robot = Robot(x=50, y=50, direction=0)
    
    # Création du contrôleur pour dessiner un carré
    square_controller = SquareDrawer(robot, side_length=100)
    
    # Création de l'interface graphique
    gui = GUI(arena, robot)
    
    # Boucle de simulation : on met à jour le déplacement et on redessine
    while not square_controller.is_done():
        square_controller.update()
        gui.draw()
        time.sleep(0.1)
        
    # Une fois le carré dessiné, on garde la fenêtre ouverte
    gui.mainloop()

if __name__ == "__main__":
    main()
