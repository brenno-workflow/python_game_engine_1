import pyglet
from pyglet.window import key

from game_state import GameState

# Classe de execucao
class Game:

    # __init__
    def __init__(self):

        # Definir instancias
        self.state = GameState()

        # Definir variaveis
        self.width = 1280
        self.height = 720
        self.elapsed_time = 0.0
        self.keys = key.KeyStateHandler()

        # Criar elementos
        self.create_window(width=self.width, height=self.height)
        self.create_time_count(width=self.width, height=self.height)
        self.create_player()

        # Definir regras
        self.window.push_handlers(self.keys, on_draw=self.on_draw)

        # Chamar update
        pyglet.clock.schedule_interval(self.update, 1 / 60)
        
    # --- Janela ---
    def create_window(self, width, height):

        # Criar janela
        self.window = pyglet.window.Window(
            caption="Python Game Engine 1",
            width=width,
            height=height
        )

    # --- Contador ---
    def create_time_count(self, width, height):

        # Criar cronometro
        self.time_count = pyglet.text.Label(
            text="Time: 0.000",
            font_name="Arial",
            font_size=20,
            x=width-(width/4),
            y=height-(height/4)
        )

    # --- Player ---
    def create_player(self, width=50, height=50):

        # Criar player
        self.player = pyglet.shapes.Rectangle(
            x=self.state.player_x,
            y=self.state.player_y,
            width=width,
            height=height,
            color=(255, 200, 80)
        )

    # --- Update ---
    def update(self, dt):

        # Somar tempo
        self.elapsed_time += dt 
        self.time_count.text = f"Time: {self.elapsed_time:.2f}"

        # Keys map
        if self.keys[key.A] or self.keys[key.LEFT]:
            self.state.player_x -= self.state.player_speed * dt
        if self.keys[key.D] or self.keys[key.RIGHT]:
            self.state.player_x += self.state.player_speed * dt
        if self.keys[key.W] or self.keys[key.UP]:
            self.state.player_y += self.state.player_speed * dt
        if self.keys[key.S] or self.keys[key.DOWN]:
            self.state.player_y -= self.state.player_speed * dt

        # Move player
        self.player.x = self.state.player_x
        self.player.y = self.state.player_y

    # --- UI ---
    def on_draw(self):
        self.window.clear()
        self.time_count.draw()
        self.player.draw()

    # --- Run ---
    def run(self):
        pyglet.app.run()