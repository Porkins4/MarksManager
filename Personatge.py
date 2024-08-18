import flet as ft
import flet.canvas as cv

class Personatge:
    def __init__(self, nom, id, notes, vides, color):
        self.nom = nom
        self.id = id
        self.notes = notes
        self.vides = vides
        self.color = color
        self.y_pos = 200  # Posició vertical inicial del personatge

    def defineixNota(self, nota):
        self.notes = nota
        # Actualitza la posició vertical del personatge en funció de la nota
        self.y_pos = 200 - nota * 10  # Ajusta el factor segons el desitjat

    def draw(self, canvas):
        paint = ft.Paint(color=self.color)
        # Dibuixa el personatge amb la nova posició vertical
        canvas.shapes.append(cv.Circle(100, self.y_pos, 20, paint=paint))  # Un cercle com a cap
        canvas.shapes.append(cv.Line(100, self.y_pos + 20, 100, self.y_pos + 70, paint=paint))  # Línia com a cos
        canvas.shapes.append(cv.Line(100, self.y_pos + 40, 80, self.y_pos + 60, paint=paint))  # Línia com a braç esquerre
        canvas.shapes.append(cv.Line(100, self.y_pos + 40, 120, self.y_pos + 60, paint=paint))  # Línia com a braç dret
        canvas.shapes.append(cv.Line(100, self.y_pos + 70, 80, self.y_pos + 90, paint=paint))  # Línia com a cama esquerra
        canvas.shapes.append(cv.Line(100, self.y_pos + 70, 120, self.y_pos + 90, paint=paint))  # Línia com a cama dreta
