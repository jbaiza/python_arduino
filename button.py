from element import Element

class Button(Element):
    def __init__(self, board, pin):
        super().__init__(board, pin, 'u')

    def enable_reporting(self, callback):
        self.digital.register_callback(callback)
        self.digital.enable_reporting()