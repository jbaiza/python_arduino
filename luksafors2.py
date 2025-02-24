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
    yellow.turn_on()
    sleep(1)
    red.turn_off()
    sleep(1)
    yellow.turn_off()
    green.turn_on()
    sleep(10)
    yellow.turn_on()
    sleep(1)
    green.turn_off()
    sleep(1)
    yellow.turn_off()
