import pyfirmata2

class Board:
    def __init__(self):
        port = pyfirmata2.Arduino.AUTODETECT
        self.board = pyfirmata2.Arduino(port)
        print("Setting up the connection to the board ...")
        self.board.samplingOn(1)

    def get_pin(self, pin_def):
        return self.board.get_pin(pin_def)

    def run(self):
        print("To stop the program press return.")
        # Do nothing here. Just preventing the program from reaching the
        # exit function.
        input()

        # Close the serial connection to the Arduino
        self.board.exit()