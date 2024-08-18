import flet as ft
import flet.canvas as cv

class Muntanya:
    def __init__(self, parades):
        self.parades = parades

    def draw(self, canvas):
        paint = ft.Paint(color=ft.colors.BROWN)
        canvas.shapes.append(cv.Path([cv.Path.MoveTo(50, 300), cv.Path.LineTo(150, 100), cv.Path.LineTo(250, 300)],
                                     paint=paint))  # Dibuix d'una muntanya