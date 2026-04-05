import pyglet
from engine.graphics.window import Window
from engine.math.time import TimeCount

# Classe principal do aplicativo do jogo
class GameApp:
    """
    Esta classe representa a aplicação do jogo.
    """

    # ---------- Init ----------

    # __init_ é o construtor da classe.
    def __init__(self):
        """
        Este método roda quando o jogo é criado.
        """

        # Definir instancias
        self.window = Window(self)
        self.time_count = TimeCount(self)
        #self.player = Player(self)
        #self.input_state = InputState()
        #self.keyboard = KeyboardBindings(self, self.input_state)

    # ---------- Update ----------

    # Atualiza o loop principal do jogo
    def update(self, dt):
        """
        Este método atualiza a lógica do jogo.
        """
        # Update
        self.time_count.update(dt) # Atualiza tempo de jogo
        #self.player_controller.update(dt) # Atualiza a posição do jogador

    # ---------- Drawn ----------

    def on_draw(self):
        self.window.window.clear()
        self.time_count.msg.draw()
        #self.player.draw()

    # ---------- Run ----------

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()