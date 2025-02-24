import pyfirmata2

class Simulation:
    def __init__(self, pin_def):
        self.pin_def = pin_def

    def write(self, value):
        if value == 1:
            print(f"{self.pin_def}: ON")
        else:
            print(f"{self.pin_def}: OFF")

class Board:
    def __init__(self):
        try:
            port = pyfirmata2.Arduino.AUTODETECT
            self.board = pyfirmata2.Arduino(port)
            print("Setting up the connection to the board ...")
            self.board.samplingOn(1)
        except:
            self.simulate = True

    def get_pin(self, pin_def):
        if self.simulate:
            return Simulation(pin_def)
        else:
            return self.board.get_pin(pin_def)

    def run(self):
        print("To stop the program press return.")
        # Do nothing here. Just preventing the program from reaching the
        # exit function.
        input()

        # Close the serial connection to the Arduino
        self.board.exit()