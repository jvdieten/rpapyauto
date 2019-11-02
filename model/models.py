class Position:
    x: int
    y: int


class MouseAction(Position):

    def __init__(self, x_pos: float, y_pos: float, button: str):
        self.x = x_pos
        self.y = y_pos
        self.button = button
