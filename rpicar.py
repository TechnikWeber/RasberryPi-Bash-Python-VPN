import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(12,GPIO.OUT) #PWM



# Set PWM instance and their frequency
pwm12 = GPIO.PWM(12, 50)

# Start PWM with 0% Duty Cycle
pwm12.start(0)

# Starte curses
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

time.sleep(0.1)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print("Forward\r")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
                time.sleep(5)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)

            elif char == curses.KEY_DOWN:
                print("Back\r")
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                time.sleep(5)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)

            elif char == curses.KEY_RIGHT:
                print("Right\r")
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)

            elif char == curses.KEY_LEFT:
                print("Left\r")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                
            elif char == curses.KEY_BACKSPACE:
                #ESC Kalibrierung starten
                pwm12.ChangeDutyCycle(0)
                print("Disconnect the battery and press Enter\r")
                pwm12.ChangeDutyCycle(7.5)
                print("ESC und Batterie jetzt verbinden\r")
                time.sleep(10)
                pwm12.ChangeDutyCycle(2.5)
                print "Ton kommt\r"
                time.sleep(7)
                print "Warten"
                time.sleep (5)
                print "Warten...\r"
                pwm12.ChangeDutyCycle(0)
                time.sleep(2)
                print "Starte\r"
                pwm12.ChangeDutyCycle(7.5)
                time.sleep(1)
                print "Motor niedrige Drehzahl\r"
                
            elif char == 10:
                print("Return\r")
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                
             
finally:
    #Beenden
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    pwm12.stop()
    GPIO.cleanup()
    
