from engine.core.game_app import GameApp

# Ponto de entrada principal do aplicativo
def run():
    """
    Este é o ponto de entrada principal do aplicativo.
    """

    # Inicia o aplicativo do jogo
    app = GameApp()

    # Loop para manter o aplicativo em execução
    app.run()