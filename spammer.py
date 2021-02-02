import os, sys, smtplib, getpass


try:

    W = '\033[0m'  #White
    R = '\033[31m' #Red
    G = '\033[32m' #Green
    B = '\033[34m' #Blue

    os.system("clear")

    server = raw_input (G +'Mail Sunucusu Gmail/Yahoo: ' + R)

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif server == 'yahoo' or server == 'Yahoo':

        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:

        print(R + "Hata - Bu komut dosyasi sadece Gmail ve Yahoo'da calisir." + W)
        sys.exit()

    email_user = 'xeansh@gmail.com'  #raw_raw_input('Email: ')
    passwd     = 'Xeansh27015'  #getpass.getpass('Password: ')
    email_to   = raw_input( R + '\nKime: ' + B)
    subject    = raw_input( R + 'Konu: ' + B)
    body       = raw_input( R + 'Mesaj: ' + B)
    total      = input(R+ 'Gonderilecek Mail Sayisi: '+ W)

    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print("\n\n\n - Hedef : {} -\n".format(email_to))

        for i in range(1, total+1):

            msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)

            print(G + "\rMail Gonderildi - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\n-Islem Sonlandirildi-" + W)


    except KeyboardInterrupt:

        print(R + "\nError - Keyboard Interrupt" + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nError - Authentication error, Are you sure the password or the username is correct?" + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
