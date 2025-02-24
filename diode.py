from element import Element

class Diode(Element):
    def __init__(self, board, pin):
        super().__init__(board, pin, 'o')

    def turn_on(self):
        self.digital.write(1)

    def turn_off(self):
        self.digital.write(0)