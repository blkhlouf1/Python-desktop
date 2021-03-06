from multiprocessing import Pool
import subprocess
import Pmw
import time
import os
from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import mainloop
from tkinter import font as tkFont
from tkinter import filedialog



fenster=Tk()
fenster.geometry("500x550")
fenster.title("Navigator Selector")
fenster['bg'] = '#49A'

helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
#declaration a global filename x ######
x="1"

# define a function whos returned a filename ########
def UploadAction():
    filename= filedialog.askopenfilename()
    global x
    x=filename
    label1 =Label(fenster, text=filename,bg="white")
    label1.place(x=0,y=60,width=500,height=50)

def open_profile(profilename):
 
    strin = '"C:\Program Files\Cyberfox\Cyberfox.exe"'+' -p ' + profilename + " -no-remote" + " imacros://run/?m=saber.js"
    subprocess.Popen(strin)



#create Button Open ##################

button = Button(fenster, text='Select Navigator', command=lambda :UploadAction(),font=helv36)
button.place(x=0,y=10,width=500,height=50)

# define the function callback to open the browser Site **************
def callback():

	Users = user_input.get()+counter1.get()
	user = user_input.get()
	start = counter1.get()
	stop = int(start)+15
	print(stop)
	global browser
	browser= str(x).split("/")
	print(browser)
	if (int(v1.get())==1):
		p = subprocess.Popen([str(x), "-p",Users, "-no-remote", "https://contacts.google.com/?hl=de&tab=mC"])
	if (int(v2.get()) == 1):
		subprocess.Popen([str(x), "-p",Users, "-no-remote", "https://mail.google.com/mail/u/0/#inbox"])
	if (int(v3.get()) == 1):
		for i in range (int(start),stop):
			print(i)
			strin = '"C:\Program Files\Cyberfox\Cyberfox.exe"'+' -p ' + user + str(i) + " -no-remote" + " imacros://run/?m=Profile1to200.js"
			print(strin)			
			subprocess.Popen(strin)
			time.sleep(10)
		counter1.setentry(stop+1)	
	if (int(v4.get()) == 1):
		process_cap = 4
		p = Pool(process_cap)
		for i in range (int(start),stop):
			print(i)
			p.map(open_profile, i)
			time.sleep(10)
			p.close()
			p.join()


 
#Create Input *********************

username=Label(fenster, text='Profil',font=helv36)
username.place(x=0,y=130,width=90,height=50)
user_input = Entry(fenster,font=helv36)
user_input.place(x=80,y=130,width=350,height=50)
user_input.insert(0,'su')
#Create a Counter *************************

counter1 = Pmw.Counter(fenster)
counter1.place(x=410,y=130,width=90,height=50)
counter1.setentry(0)
counter1.increment()



# initializing the choice, i.e. Python ********************
v1 = StringVar()
v1.set(0)

v2 = StringVar()
v2.set(0)

v3 = StringVar()
v3.set(0)

v4 = StringVar()
v4.set(1)



# create Checkbuttons **************************************
helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')

Checkbutton(fenster,  text="contacts",  padx = 20, variable=v1,height=2,font=helv36).place(x=0, y=210)
Checkbutton(fenster,  text="Mails",  padx = 20, variable=v2,font=helv36,height=2).place(x=140, y=210)
Checkbutton(fenster,  text="R-edited",  padx = 20, variable=v3,font=helv36,height=2).place(x=280, y=210)
Checkbutton(fenster,  text="Reporting",  padx = 20, variable=v4,font=helv36,height=2).place(x=418, y=210)



#create a Submit Button ##############
MyButton1 = Button(fenster, text="Open", width=10,command=lambda:callback(),font=helv36)
MyButton1.place(x=0,y=300,width=500,height=50)




#Kill the Browser *****************
def closeOpenedWindow() :
    global browser
    kill_me="taskkill /im " +browser[-1]+ " /f"
    os.system(kill_me)

MyButton2 = Button(fenster, text="Kill all", width=10,command=lambda:closeOpenedWindow(),font=helv36)
MyButton2.place(x=0,y=400,width=500,height=50)

#*******************


mainloop()