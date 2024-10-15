from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky(texture='sky_sunset')
window.color = color.rgb(0,200,255)
player.gravity = 0.0


boxes = []

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgb(red, green, blue)
    

def add_box(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=random_color(),
        position=position,
        texture=
        load_texture('assets/sand.png')
      )
    )

for x in range(20):
  for y in range(20):
    add_box( (x, 0, y) )

def show_menu():
    menu = Entity(
        parent=camera.ui,
        model='quad',
        color=color.black66,
        scale=(2, 1.5),
        position=(0, 0)
    )  

    title = Text(
        parent=menu,
        text='menu',
        scale=2,
        position=(0, 0.3)
    )

    resume_button = Button(
        parent=menu,
        text='resume',
        position=(0, 0),
        on_click=hide_menu
    )

    quit_button = Button(
        parent=menu,
        text='Quit',
        position=(0, -0.2),
        on_click=application.quit
    )

    def hide_menu():
        menu.disable()
        mouse.locked = True
        player.enable()

    mouse.locked = False 
    player.disable()

    menu.enable()

def input(key):
    if key == 'escape':
        show_menu()       
    elif key == 'shift':
        player.speed = 2
        player.gravity = 0.1
        player.height = 1.5  # Verringert die Spielerhöhe, um das Eintauchen in den Block zu ermöglichen.
    else:
        player.speed = 6
        player.gravity = 0.5
        player.height = 2  # Setzt die Spielerhöhe auf die Standardhöhe zurück.

    # Verhindert das Abfallen von Kanten
    if player.y < -10:
        player.y = 10
        player.x = 0
        player.z = 0

    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)

app.run()


