import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM1')

#Setup pins for communication with a 74HC595 shift register
latchPin = 8
clockPin = 12
dataPin = 11

#LED Byte 
byte  = [0, 0, 0, 0, 0, 0, 0, 0] #if controlling leds: 0 = led off; 1 = led on. 

#Write to shift register (depending on usage one might always flush the register with 0s bevore filling) 
def updateShiftRegister(byte): 
   board.digital[latchPin].write(0)
   for i in byte: 
       board.digital[dataPin].write(i)
       board.digital[clockPin].write(1)
       board.digital[clockPin].write(0)
   board.digital[latchPin].write(1)

#usage example (e.g. light 8 leds in predefinded patterns): 
while True: #gets written left to right, so last list element = first register output 
    byte = [0, 0, 0, 0, 1, 1, 1, 1] 
    updateShiftRegister(byte)
    time.sleep(5) 
    byte = [1, 1, 1, 1, 0, 0, 0, 0]
    updateShiftRegister(byte)
    time.sleep(5)
    byte = [1, 0, 1, 0, 1, 0, 1, 0]
    updateShiftRegister(byte)
    time.sleep(5)

