import time
import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def startBombing():
    victim=str(name.get())
    msg=str(message.get())
    num=msgCount.get()
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com/")

    time.sleep(50)
    user=driver.find_element_by_xpath('//span[@title = "'+victim+'"]')
    user.click()
    #time.sleep(40)
    msg_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    for i in range(num):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)


#GUI
root=tk.Tk()
root.title("Whatsapp Bombing")
root.geometry("500x500")
root.resizable(height=False,width=False)

headingLabel=Label(root,text="Wait for 40-50 sec to start BOOM!",font=('Helvetics',12,'bold'))
headingLabel.place(relx=.5,y=15,anchor='center')

# victim name label
Label(root,text="Enter Contact Name").place(x=105,y=80)
name=StringVar()
nameBox=Entry(root,textvariable=name).place(x=220,y=80)
#  Msg label
Label(root,text="Enter Message").place(x=120,y=150)
message=StringVar()
msgBox=Entry(root,textvariable=message).place(x=220,y=150)

Label(root,text="No Of Message").place(x=120,y=220)
msgCount=IntVar()
countBox=Entry(root,textvariable=msgCount).place(x=220,y=220)
tk.Button(root,text="Start Bombing",command=startBombing).place(relx=.5,y=300,anchor="center")
root.mainloop()