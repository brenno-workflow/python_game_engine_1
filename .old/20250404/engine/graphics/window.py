import pyglet

# Classe da janela do jogo
class Window:
    """
    Esta classe cria a janela de execuçaõ do jogo.
    """

    # ---------- Init ----------

    # __init_ é o construtor da classe.
    def __init__(self, width=1280, height=720):
        """
        Este método roda quando o jogo é criado.
        """

        # Definir variaveis
        self.width = width
        self.height = height
        
        # Criar janela
        self.window = pyglet.window.Window(
            width=width,
            height=height,
            caption="Python Game Engine 1"
        )