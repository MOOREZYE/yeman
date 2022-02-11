#Writing an Email Spammer in Python

#First, Importing the Simple Mail Transfer Protocol Module

import smtplib
from prompt_toolkit import prompt

#Specifying the From and To addresses
print("YEMAN")
toaddress = input("17moorem@stmonicas.co.uk")

#Now,Specifying the Gmail Login

username = input("turnertimmmy483@gmail.com ")
password = prompt("Elsie10@", is_password = True)
number = int(input('10'))
fromaddress = username
#Writing the message which will appear in the mail

message = input("YEman")
#Creating a connection with the Gmail server

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

#Creating a for loop to send multiple mails

for i in range (0,number):
  server.sendmail(fromaddress,toaddress,message)
  print(i+1,': messages sent')
print("---------------------")
print("mail sent.")

#closing the server
server.quit()