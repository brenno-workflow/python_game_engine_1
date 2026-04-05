from pyglet.window import key

# Classe principal do teclado do jogo
class KeyboardBindings:
    """
    Classe de configuração das teclas de controle do jogador.
    """

    # ---------- Init ----------

    # __init_ é o construtor da classe.
    def __init__(self, window):

        # Definir instancias
        self.window = window

        self.base = base
        self.input_state = input_state

    # ---------- Bind ----------

    # Mapa das teclas
    def bind(self):
        self.base.accept("w", self._set, ["forward", True])
        self.base.accept("w-up", self._set, ["forward", False])
        self.base.accept("s", self._set, ["backward", True])
        self.base.accept("s-up", self._set, ["backward", False])
        self.base.accept("a", self._set, ["left", True])
        self.base.accept("a-up", self._set, ["left", False])
        self.base.accept("d", self._set, ["right", True])
        self.base.accept("d-up", self._set, ["right", False])

    # ---------- Set ----------

    # Setar tecla apertada
    def _set(self, direction, value):
        setattr(self.input_state, direction, value)

# Teclas
keys = key.KeyStateHandler()
window.push_handlers(keys)