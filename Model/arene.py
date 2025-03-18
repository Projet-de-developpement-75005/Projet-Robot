class Arena:
    def __init__(self, width=400, height=400, scale=1):
        """
        Initialise l'arène avec ses dimensions et un facteur de mise à l'échelle.
        """
        self.width = width
        self.height = height
        self.scale = scale
        self.objets = []  # On pourra ajouter des obstacles ou autres objets

    def add_object(self, obj):
        """Ajoute un objet à l'arène."""
        self.objets.append(obj)

    def __str__(self):
        return f"Arena({self.width}x{self.height})"
