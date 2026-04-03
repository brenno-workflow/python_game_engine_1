import pyglet

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

# Update
def update(dt):
    global elapsed_time # Tomar global
    elapsed_time += dt # Somar tempo
    time_msg.text = f"Time: {elapsed_time:.2f}"


# Desenhar na janela
@window.event # registra uma função como evento da janela
def on_draw():
    window.clear() # Limpar a tela
    time_msg.draw()

# Rodar
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()