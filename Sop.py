`
from csv import reader
import smtplib
import datetime
with open('project.csv','rb') as f:
    csv_reader=reader(f)
def uploading():
    print("uploading........")
    print("uploading complete...")
    print("you may check your document on ur website")


sop_initial_date=datetime.date(2020,5,5)
sop_expire_date=datetime.date(2020,5,5)
version_of_SOP=1.0
if sop_expire_date==sop_initial_date:
    sender_email='ali962001@gmail.com'
    rec_mail='mzeeshankhan3534uit@gmail.com'
    password='zeeboy123'
    message=csv_reader

    server=smtplib.SMTP('smtp.gmail.com:465')
    server.ehlo()
    server.starttls()
    server.login(rec_mail,password)
    print("login in done")
    server.sendmail(sender_email,rec_mail,message)
    print("email is sent to", rec_mail)
    server.quit()
    print('successfully send mail')
version_of_SOP+=1.0
print(version_of_SOP)