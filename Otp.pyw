from tkinter import *
import random
from tkinter import messagebox

import requests
root=Tk()




def getvals():
    global otp
    otp = random.randint(1000, 9999)

    print(otp)


    x=numbervalue.get()


    requests.get(f"https://www.fast2sms.com/dev/bulkV2?authorization=aEmAkOIoKy06Xtv85GnSFJP34DzcueTULVgpQYqjR9ldWfxsr2pfOdLFmZEDgvXziThU3u7tbBwr2C18&route=s&sender_id=CHKSMS&message=2&variables_values={otp}%7C&flash=0&numbers={x}")
    Label(root, text="Enter OTP : ", font="lucida 10 bold",pady=10).grid(row=3,column=1)
    otpvalue=StringVar()
    def value():

     t=otpvalue.get()
     y=int(t)


     if y==otp:
         messagebox.showinfo("Info","Succesfully Verified")
     else:

         messagebox.showerror("error","Please Enter correct otp")

    Entry(root,textvariable=otpvalue).grid(row=3,column=2)
    Button(root,text="submit",command=value).grid(row=4,column=2)


root.geometry("500x400")
root.title("OTP SYSTEM")
Label(root,text="OTP SYSTEM",font="lucida 15 bold").grid(row=0,column=2)
number=Label(root,text="Enter Your Number : ",font="lucida 10 bold")
number.grid(row=1,column=1)
numbervalue=StringVar()



numberentry=Entry(root,textvariable=numbervalue)

numberentry.grid(row=1,column=2)
Button(root,text="GET OTP",command=getvals).grid(row=2,column=2)

root.mainloop()