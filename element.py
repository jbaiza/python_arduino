class Element:
    def __init__(self, board, pin, input_type):
        self.board = board
        self.digital = board.get_pin(f"d:{pin}:{input_type}")