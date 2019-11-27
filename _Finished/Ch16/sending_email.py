import smtplib

"""
If the smptlib.SMTP() call is not successful, your SMTP server might not support TLS on port 587.
In this case you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.
"""
# mail = smtplib.SMTP('smtp.gmail.com', 587)
mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# print(type(mail)) # <class 'smtplib.SMTP'>

# Sending the SMTP "Hello" message
## Checks if there's connection.
print(mail.ehlo()) # (250, b'smtp.gmail.com at your service, [212.60.107.203]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

"""
'vuvc bvzf ocev ywgo' is a Application Password.
It's a encrypted password that works on joakimfkk@gmail.com, but since this script requires it to be written out,
there's a chance that someone could get it.

Multiple App Passwords can be created, with names at:
https://myaccount.google.com/security
"""
mail.login('joakimfkk@gmail.com', 'vuvc bvzf ocev ywgo')

# The start of the email body string must begin with "Subject: \n"
# sender, recipient, subject and main body.
mail.sendmail('joakimfkk@gmail.com', 'joakimfkk@gmail.com', 'Subject: yo what the fuck.\nOH NO THIS IS A BOT.')
mail.quit()