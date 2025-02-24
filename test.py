from board import Board
from diode import Diode
from button import Button


board = Board()

red = Diode(board, 13)
green = Diode(board, 12)

def button_pressed(value):
    if value:
        red.turn_on()
        green.turn_off()
    else:
        red.turn_off()
        green.turn_on()

button = Button(board, 10)
button.enable_reporting(button_pressed)

board.run()