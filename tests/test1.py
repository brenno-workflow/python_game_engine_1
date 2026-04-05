import pyglet
from pyglet.window import key

# Criar janela do jogo
window = pyglet.window.Window(
    caption="Python Game Engine 1",
    width=1280,
    height=720
)

# Tempo
elapsed_time = 0.0

# Tempo msg
time_msg = pyglet.text.Label(
    text="Time: 0.000",
    font_name="Arial",
    font_size=20,
    x=1000,
    y=650
)

# Teclas
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Position
pos_x = 100
pos_y = 100
speed = 200

# Player
player = pyglet.shapes.Rectangle(
    width=50,
    height=50,
    color=(255, 200, 80),
    x=pos_x,
    y=pos_y
)

# Update
def update(dt):

    # Globals
    global elapsed_time, pos_x, pos_y

    # --- Time ---

    # Somar tempo
    elapsed_time += dt 
    time_msg.text = f"Time: {elapsed_time:.2f}"

    # --- Move ---

    # Find key
    if keys[key.A] or keys[key.LEFT]:
        pos_x -= speed * dt
    if keys[key.D] or keys[key.RIGHT]:
        pos_x += speed * dt
    if keys[key.W] or keys[key.UP]:
        pos_y += speed * dt
    if keys[key.S] or keys[key.DOWN]:
        pos_y -= speed * dt

    # Position update
    player.x = pos_x
    player.y = pos_y

# Desenhar na janela
@window.event # registra uma função como evento da janela
def on_draw():
    window.clear() # Limpar a tela
    time_msg.draw()
    player.draw()

# Rodar
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()