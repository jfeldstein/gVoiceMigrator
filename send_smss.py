from googlevoice import Voice
from googlevoice.util import input
import csv
import time

voice = Voice()
voice.login()

friendsNumbers = csv.reader(open('numbers.csv', 'rb'))

for friend in friendsNumbers:
  name = friend[0]
  number = friend[1]
  
  message = name + ", it's Jordan Feldstein. I've got a new number: 847.282.4467. Save it, my 224 is now old. That is all, carry on :O)"
  
  voice.send_sms(number, message)
  print 'Texted ' + name
  time.sleep(3)

