class SquareDrawer:
    def __init__(self, robot, side_length=100):
        """
        Initialise le contrôleur pour dessiner un carré avec le robot.
        
        Args:
            robot (Robot): instance du robot à déplacer.
            side_length (int): longueur d'un côté du carré.
        """
        self.robot = robot
        self.side_length = side_length
        self.current_side = 0
        self.distance_moved = 0
        self.step = 5  # Correspond au pas de déplacement lors du dessin du carré
        self.done = False

    def update(self):
        """
        Met à jour le dessin : si le côté n'est pas complet, avance ;
        sinon, effectue une rotation de 90° pour passer au côté suivant.
        """
        if self.done:
            return

        if self.distance_moved < self.side_length:
            self.robot.move_forward(self.step)
            self.distance_moved += self.step
        else:
            self.robot.rotate(90)
            self.distance_moved = 0
            self.current_side += 1
            if self.current_side >= 4:
                self.done = True

    def is_done(self):
        """Retourne True si le dessin du carré est terminé."""
        return self.done
