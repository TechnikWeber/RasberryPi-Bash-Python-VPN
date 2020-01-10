import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import RPi.GPIO as GPIO
import time

#Set GPIO pins to use BCM pin numbers
GPIO.setmode(GPIO.BCM)
 
#Set digital pin 17(BCM) to an input
GPIO.setup(17, GPIO.IN)
 
#Set digital pin 17(BCM) to an input and enable the pullup 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
#Event to detect button press
GPIO.add_event_detect(17, GPIO.FALLING)


while True:
    if GPIO.event_detected(17):

	#print "Email sent"
        
	senderEmail = "EMAIL!!!HERE"
	empfangsEmail = "EMAIL!!!HERE"
	msg = MIMEMultipart()
	msg['From'] = senderEmail
	msg['To'] = empfangsEmail
	msg['Subject'] = "Alarmanlage ausgeloest"

	emailText = "Alarmanlage <b>ausgeloest</b>"
	msg.attach(MIMEText(emailText, 'html'))

	server = smtplib.SMTP('smtp.strato.de', 587) # Die Server Daten
	server.starttls()
	server.login(senderEmail, "PW!!!HERE") # Das Passwort
	text = msg.as_string()
	server.sendmail(senderEmail, empfangsEmail, text)
	server.quit()
 
    time.sleep(10)
