from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

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
        texture='grass'
      )
    )

for x in range(20):
  for y in range(20):
    add_box( (x, 0, y) )

sneaking = False

def update():
    global sneaking
    global escape

    if held_keys['shift']:
        sneaking = True
        player.speed = 2
        player.gravity = 0.0
        player.height = 1.5  # Verringert die Spielerhöhe, um das Eintauchen in den Block zu ermöglichen.
    else:
        sneaking = False
        player.speed = 6
        player.gravity = 0.5
        player.height = 2  # Setzt die Spielerhöhe auf die Standardhöhe zurück.

    # Verhindert das Abfallen von Kanten
    if player.y < -10:
        player.y = 10
        player.x = 0
        player.z = 0

    if not sneaking or (sneaking and player.grounded):
            if held_keys['space']:
                player.y += 0.5

    for box in boxes:
        if box.hovered:
            if held_keys["right mouse down"]:
                if not sneaking:
                    add_box(box.position + mouse.normal)
            if held_keys["left mouse down"]:
                if not sneaking:
                  boxes.remove(box)
                  destroy(box)
                else:
                    add_box(box.position + mouse.normal)

       

app.run()


