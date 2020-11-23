'''
@ Author : Ishan Agrawal
Instagram : pyvisualizer
YouTube : Pyvisualizer
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ------------------
from tkinter import *
import ctypes,time
import threading as T
import smtplib
from email import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import requests
import cv2,os
from datetime import datetime
from urllib.request import urlopen
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
youremail = 'please enter your email here'
passw = "1"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
        try:                                
                        #To check the internet connection------------------------------------------------------------------------------------------------------------------------------------------------
                        stri = "https://www.google.co.in"
                        data = urlopen(stri)
                        #If this gives error loop will continue
                        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #Making the window
                        window = Tk()
                        window.title("Entry Passcode")
                        window.resizable(0,0)
                        en = StringVar()
                        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #placing the window in center of screen
                        user32 = ctypes.windll.user32
                        user32.SetProcessDPIAware()
                        [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
                        lt = [w, h]
                        a = str(lt[0]//2-202)
                        b= str(lt[1]//2-60)
                        tr = 3
                        window.geometry("405x110+"+a+"+"+b)
                        window.config(bg='black')
                        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #To check the given password and if it is wrong send email
                        def check():
                                global tr
                                if en.get()==passw:
                                        window.destroy() #exit if password is correct
                                        quit()
                                else:
                                        tr-=1
                                        if tr==0:
                                                os.system('shutdown  /s /t 1') #shutdown the pc if user is failed to give right password even after 3 attemts
                                        if tr==2:
                                        
                                            try:
                                                os.remove('image.jpg')
                                            except:
                                                pass

                                            try:
                                                    try:
                                                        videoCaptureObject = cv2.VideoCapture(1)
                                                        for i in range(3):
                                                                ret,frame = videoCaptureObject.read()
                                                                name='image.jpg'
                                                                cv2.imwrite(name,frame)

                                                        videoCaptureObject.release()
                                                        cv2.destroyAllWindows()
                                                    except :
                                                         videoCaptureObject = cv2.VideoCapture(0)                            
                                                         for i in range(3):
                                                                ret,frame = videoCaptureObject.read()
                                                                name='image.jpg'
                                                                cv2.imwrite(name,frame)

                                                         videoCaptureObject.release()
                                                         cv2.destroyAllWindows()
                                            except:
                                                    pass

                                            now = datetime.now()
                                            tm = now.strftime("%H:%M:%S")

                                            ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                                            my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
                                            test='''Unidentified Login Into Your PC Detected !!!
'''+'IP ADDRESS:'+str([my_ip])+'''
Time :- '''+tm
                                            # Prints The IP string, ex: 198.975.33.4

                                            #Look up the GeoIP information from a database for the user's ip

                                            geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
                                            geo_request = requests.get(geo_request_url)
                                            geo_data = geo_request.json()
                                            x = geo_data
                                            mail_content = test+'''
'''+'Other Info :-  ' + str(x)+'''
Image At The Time Of Login :-'''

                                            mail_content=str(mail_content)

                                            #The mail addresses and password
                                            sender_address = 'yourpc32@gmail.com'
                                            sender_pass = '@Qwe12345678'
                                            receiver_address = youremail
                                            #Setup the MIME
                                            message = MIMEMultipart()
                                            message['From'] = sender_address
                                            message['To'] = receiver_address
                                            message['Subject'] = 'Unidentified Login Alert !!!'
                                            #The subject line
                                            #The body and the attachments for the mail
                                            message.attach(MIMEText(mail_content, 'plain'))
                                            try:
                                                    attach_file_name = 'image.jpg'
                                                    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
                                                    msgImage = MIMEImage(attach_file.read())
                                                    msgImage.add_header('Content-ID', '<image1>')
                                                    message.attach(msgImage)
                                            except:
                                                pass

                                            #Create SMTP session for sending the mail
                                            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                                            session.starttls() #enable security
                                            session.login(sender_address, sender_pass) #login with mail_id and password
                                            text = message.as_string()
                                            session.sendmail(sender_address, receiver_address, text)
                                            session.quit()
                        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #Adding functions to window
                        l = Label(window,text= "Enter The Password :",bg = "black",fg="lime",font=("",12))
                        l.place(x = 30,y = 20)
                        e = Entry(window,textvariable=en,bg = "gray10",fg="lime",font=("",12))
                        e.place(x = 190,y=21)
                        b = Button(window,text="SUBMIT",bg = "gray10",fg="lime",font=("",13),width=37,command = check)
                        b.place(x = 32, y = 70)
                        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        def pop(): #Pop up the window after every 10 seconds to grab the attention of user
                                try:
                                        window.deiconify()
                                        time.sleep(10)
                                        window.withdraw()
                                        pop()
                                except:
                                        pop()
   
                        p=T.Thread(target = pop)
                        p.start()
                         #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                        #window.overrideredirect(True)
                        window.mainloop()
         #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        except:
                continue
         #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
