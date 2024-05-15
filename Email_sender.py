import smtplib   #this module is use for communicate with the smtp serverse.... which are used for send mail to one account to another..

def send_mail(to , containt,email,pas):
    
    #Here we create a variable server which holds the command of SMTP and the email service we want to use and the port number which the sevice provider uses.. like the gmail uses '587' as there port number.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  #this make the communication
    server.starttls()  #here session starts
    server.login(email, pas)
    server.sendmail(email,to,containt)
    server.close()

    print('Email sended..')



to = input("Enter the recevers mail: \n")
containt = input("Enter the containt: \n")
send_mail(to,containt)