import flet as ft
import flet.canvas as cv
import time
from Muntanya import Muntanya
from Personatge import Personatge


def main(page: ft.Page):
    canvas = cv.Canvas(shapes=[], expand=True)
    personatge = Personatge("Heroi", 1, "Personatge principal", 3, ft.colors.BLUE)
    muntanya = Muntanya(5)

    muntanya.draw(canvas)
    page.add(canvas)

    t0 = current_milli_time()
    nota = 0
    while nota < 10:
        if current_milli_time() - t0 > 1000:
            canvas.clean()
            muntanya.draw(canvas)
            personatge.defineixNota(nota)
            personatge.draw(canvas)
            nota = nota + 1
            t0 = current_milli_time()
            #page.add(canvas)
            canvas.update()



def current_milli_time():
    return round(time.time() * 1000)

ft.app(main)

# Executar la app
ft.app(target=main)

