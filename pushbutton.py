import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(8, GPIO.OUT)  #LED to GPIO24

def push1():

     while True:
         button_state = GPIO.input(23)
         if button_state == False:	
             GPIO.output(24, True)
             sendMessage1("Respective person has been a victim to accident.He/She needs help")
             push2()
         else:
             GPIO.output(24, False)

def push2():

     while True:
         button_state = GPIO.input(25)
         if button_state == False:
             GPIO.output(8, True)
             sendMessage2("He/She is safe..Don't worry")
             push1()
         else:
             GPIO.output(8, False)


def sendMessage1(helpMessage):
   fromaddr = "pepitalacoco@gmail.com"
   toaddr = "ankurat1314@gmail.com"
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = "Help Message"
   body = helpMessage
   msg.attach(MIMEText(body, 'plain'))
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login("pepitalacoco@gmail.com", "01464776cse15")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()

def sendMessage2(safetyMessage):
   fromaddr = "pepitalacoco@gmail.com"
   toaddr = "ankurat1314@gmail.com"
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = "Safety Information"
   body = safetyMessage
   msg.attach(MIMEText(body, 'plain'))
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login("pepitalacoco@gmail.com", "01464776cse15")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()


try:
 push1()
except:
 GPIO.cleanup()