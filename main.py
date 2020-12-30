
# Portable password input
from getpass import getpass

from socket import *

# Encoding used to convert bytes that have binary or text data into ASCII characters
from base64 import *

# Secure Sockets Layer (used to create a secure connection between server and client)
import ssl


SenderEmail = input("Enter Your Email Address: ")
SenderPassword = getpass("Enter Your Password: ")
ReceiverEmail = input("Enter Email Destination: ")
Subject = input("Enter Email Subject: ")
EmailBody = input("Enter Email Body Message: ")

# Message included in body
msg = '{}. \r\nI love computer networks!'.format(EmailBody)
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

#Fill in start

# Creating socket called clientSocket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establishing a TCP connection with mailserver
clientSocket.connect((mailServer, mailPort))

#Fill in end

confMsg = clientSocket.recv(1024)
print (confMsg)
if confMsg[:3] != '220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'.encode()
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Account Authentication
# Fill in start
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
confMsg2 = clientSocket.recv(1024).decode()

sslClientSocket = ssl.wrap_socket(clientSocket)

EMAIL_ADDRESS = b64encode(SenderEmail.encode())
EMAIL_PASSWORD = b64encode(SenderPassword.encode())

authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd.encode())
confMsg2 = sslClientSocket.recv(1024)
print(confMsg2)

sslClientSocket.send(EMAIL_ADDRESS + "\r\n".encode())
confMsg3 = sslClientSocket.recv(1024).decode()
print(confMsg3)

sslClientSocket.send(EMAIL_PASSWORD + "\r\n".encode())
confMsg4 = sslClientSocket.recv(1024).decode()
print(confMsg4)
# Fill in end

# Send MAIL FROM command and print server response.
# Fill in start
mailfrom = "MAIL FROM: <{}>\r\n".format(SenderEmail)
sslClientSocket.send(mailfrom.encode())
confMsg5 = sslClientSocket.recv(1024).decode()
print(confMsg5)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(ReceiverEmail)
sslClientSocket.send(rcptto.encode())
confMsg6 = sslClientSocket.recv(1024).decode()
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
confMsg7 = sslClientSocket.recv(1024).decode()
print(confMsg7)
# Fill in end

# Send message data.
# Fill in start
sslClientSocket.send("Subject: {}\n\n{}".format(Subject, msg).encode())
# Fill in end

# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg.encode())
confMsg8 = sslClientSocket.recv(1024).decode()
print(confMsg8)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcommand = 'QUIT\r\n'
sslClientSocket.send(quitcommand.encode())
confMsg9 = sslClientSocket.recv(1024).decode()
print(confMsg9)

sslClientSocket.close()
print('Was successful!')
# Fill in end
