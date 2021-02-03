import os, sys, smtplib, getpass
from auth import *

try:

    W = '\033[0m'  #White
    R = '\033[31m' #Red
    G = '\033[32m' #Green
    B = '\033[34m' #Blue

    os.system("clear")

    server = raw_input (G +'Mail Server Gmail/Yahoo: ' + R)

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif server == 'yahoo' or server == 'Yahoo':

        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:

        print(R + "Error - This script only works in Gmail and Yahoo." + W)
        sys.exit()

    email_user = auth.email_user
    passwd     = auth.email_user
    email_to   = raw_input( R + '\nTo: ' + B)
    subject    = raw_input( R + 'Subject: ' + B)
    body       = raw_input( R + 'Message: ' + B)
    total      = input(R+ 'Amount of Sendings'+ B)

    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print("\n\n\n - Target : {} -\n".format(email_to))

        for i in range(1, total+1):

            msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)

            print(G + "\rMail Sent - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\n-Process Terminated-" + W)


    except KeyboardInterrupt:

        print(R + "\nError - Keyboard Interrupt" + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nError - Authentication error, Are you sure the password or the username is correct?" + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
