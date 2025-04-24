def get_left_x(window_width: int, object_width: int) -> float:
    """
    Retorna a posição X para o lado esquerdo da tela, levando em consideração a largura do objeto.
    O pad do jogador começa na borda esquerda (X = 0).
    """
    return 0  # O pad do jogador começa na borda esquerda


def get_right_x(window_width: int, object_width: int) -> float:
    """
    Retorna a posição X para o lado direito da tela, levando em consideração a largura do objeto.
    O pad da IA começa no lado direito.
    """
    return window_width - object_width  # O pad da IA começa no lado direito


def get_center_x(window_width: int, object_width: int) -> float:
    """
    Retorna a posição X para centralizar o objeto na tela.
    """
    return (window_width - object_width) / 2  # Centraliza o objeto horizontalmente


def get_center_y(window_height: int, object_height: int) -> float:
    """
    Retorna a posição Y para centralizar o objeto na tela.
    """
    return (window_height - object_height) / 2  # Centraliza o objeto verticalmente
