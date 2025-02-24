from board import Board
from diode import Diode
from button import Button
from time import sleep

board = Board()

red = Diode(board, 13)
green = Diode(board, 12)
yellow = Diode(board, 11)
while True:
    red.turn_on()
    sleep(15)
    red.turn_off()
    yellow.turn_on()
    sleep(2)
    yellow.turn_off()
    green.turn_on()
    sleep(10)
    green.turn_off()
    yellow.turn_on()
    sleep(2)
    yellow.turn_off()
