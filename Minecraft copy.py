from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky(texture='sky_sunset')

boxes = []


def add_box(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=color.white,
        position=position,
        texture=
        load_texture('assets/Fliesen.jpg')
      )
    )

    class Inventory(Entity):
        def __init__(self):
            super().__init__( 
            parent = camera.ui,
            model = 'quad',
            scale = (.5, .8),
            origin = (-.5, .5),
            position = (-.3,.4),
            texture = 'white_cube',
            texture_scale = (5,8),
            color = color.dark_gray
            )

            self.item_parent = Entity(parent=self, scale=(1/5,1/8))

        def find_free_spot(self):
            taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
            for y in range(8):
              for x in range(5):
                if not (x,-y) in taken_spots:
                    return (x,-y)
            
            
        def append(self, item):
                icon = Draggable(
                    parent = inventory.item_parent,
                    model = 'quad',
                    texture = item,
                    color = color.white,
                    origin = (-.5,.5),
                    color = color.random_color(),
                    position = self.find_free_spot(),
                    z = -0.1
                name = item.replace('_','').title()
                icon.Tooltip = Tooltip(name)
                icon.tooltip.backround.color = color.color(0,0,0,.8))
               
                
            

                inventory = Inventory()
                for i in range(7):
                    inventory.append('test item')

    

   
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
    global player
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


