import pyglet

# Classe da contagem do jogo
class TimeCount:
    """
    Esta classe cria um cronometro no jogo.
    """

    # ---------- Init ----------

    # __init_ é o construtor da classe.
    def __init__(self):
        """
        Este método roda quando a classe é criado.
        """
        
        # Definir variaveis
        self.elapsed_time = 0.0
        self.msg = pyglet.text.Label(
            text="Time: 0.000",
            font_name="Arial",
            font_size=20,
            x=1000,
            y=650
        )

    # ---------- Update ----------

    # Update
    def update(self, dt:float):
        """
        Atualiza a contagem de tempo
        """

        # Somar tempo
        self.elapsed_time += dt 
        self.msg.text = f"Time: {self.elapsed_time:.2f}"
