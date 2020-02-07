import smtplib
sender = input("type sender email: ")
password = input("password: ")
reciver = input("reciver: ")

print("Sending the message")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password)
server.sendmail(
  sender,
  reciver,
  "this message is from python")
server.quit()
print("message is send")
