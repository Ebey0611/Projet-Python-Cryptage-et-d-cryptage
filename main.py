class ArbreB:
    def __init__(self, s_arbreg, s_arbred, valeur):
        self.s_arbreg = s_arbreg
        self.s_arbred = s_arbred
        self.valeur = valeur

    def est_vide(self):
        return self.valeur is None and self.s_arbreg is None and self.s_arbred is None

    def recherche(self, e):
        if self.est_vide():
            return False

        elif e == self.valeur:
            return True

        elif self.s_arbreg is not None:
            if self.s_arbreg.recherche(e):
                return True

        elif self.s_arbred is not None:
            if self.s_arbred.recherche(e):
                return True

        return False
    
    def insertion(self, val) :
        pass
    
    def dessiner_arbre(self, canvas, x, y, rayon):
        canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill="white", width=2)
        canvas.create_text(x, y, text=str(self.valeur))

        # Dessiner le sous-arbre gauche
        if self.s_arbreg is not None:
            x_gauche = x - 3*rayon
            y_gauche = y + 3*rayon
            canvas.create_line(x, y+rayon, x_gauche+rayon, y_gauche-rayon, width=2)
            self.s_arbreg.dessiner_arbre(canvas, x_gauche, y_gauche, rayon)

        # Dessiner le sous-arbre droit
        if self.s_arbred is not None:
            x_droit = x + 3*rayon
            y_droit = y + 3*rayon
            canvas.create_line(x, y+rayon, x_droit-rayon, y_droit-rayon, width=2)
            self.s_arbred.dessiner_arbre(canvas, x_droit, y_droit, rayon)

class Sommet(ArbreB) :
    def __init__(self, s_arbreg, s_arbred, valeur, label):
        super().__init__(s_arbreg, s_arbred, valeur)
        self.label = label

    def modification(self, new_label) :
        self.label = new_label
