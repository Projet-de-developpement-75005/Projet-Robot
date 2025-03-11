# update_affichage.py
def update_affichage(canvas, robot_id, robot, mode_affichage):
    """
    Met à jour l'affichage du robot sur le canevas tkinter.
    Cette fonction déplace le robot en fonction de ses coordonnées actuelles.
    """
    if mode_affichage:
        # Supprime l'ancienne position du robot
        canvas.delete(robot_id)

        # Met à jour la position du robot
        new_x1 = robot.x - 5
        new_y1 = robot.y - 5
        new_x2 = robot.x + 5
        new_y2 = robot.y + 5

        # Redessine le robot à la nouvelle position
        robot_id = canvas.create_oval(new_x1, new_y1, new_x2, new_y2, fill="blue")

        # Redessine l'arène si nécessaire (optionnel selon votre gestion)
        # canvas.update()

        # Vous pouvez ajouter des conditions supplémentaires si vous avez besoin d'autres mises à jour
