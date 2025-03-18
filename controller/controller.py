class SquareDrawer:
    def __init__(self, robot, side_length=100):
        """
        Constructeur qui initialise le contrôleur pour dessiner un carré.
        
        Args:
            robot (Robot): instance du robot à déplacer.
            side_length (int): longueur d'un côté du carré.
        """
        self.robot = robot
        self.side_length = side_length
        self.current_side = 0
        self.distance_moved = 0
        self.step = 5  # Pas de déplacement à chaque mise à jour

        self.done = False

    def update(self):
        """
        Met à jour la commande : si la distance parcourue sur le côté actuel 
        est inférieure à la longueur désirée, avance ; sinon, effectue une rotation de 90°.
        """
        if self.done:
            return

        # Avancer si le côté n'est pas encore complet
        if self.distance_moved < self.side_length:
            self.robot.move_forward(self.step)
            self.distance_moved += self.step
        else:
            # Terminé un côté, on tourne de 90 degrés et on réinitialise
            self.robot.rotate(90)
            self.distance_moved = 0
            self.current_side += 1
            if self.current_side >= 4:
                self.done = True

    def is_done(self):
        """
        Retourne True si le carré est entièrement dessiné.
        """
        return self.done
