# Description: This file contains the GUI code for the Whatsapp Automation Bot
import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
import time
import csv
import script as sc
class App:
    
    def __init__(self, root):
        self.click1 = False
        self.click2 = False
        self.click3 = False
        self.filename = ""
        #setting title
        root.title("WHatsapp Automation Bot -- @HamzaahSyed")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GMessage_686=tk.Text(root)
        self.GMessage_686["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GMessage_686["font"] = ft
        self.GMessage_686["fg"] = "#333333"
        self.GMessage_686.place(x=30,y=350,width=532,height=125)

        GLabel_606=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_606["font"] = ft
        GLabel_606["fg"] = "#333333"
        GLabel_606["justify"] = "center"
        GLabel_606["text"] = "Whatsapp Automation Bot"
        GLabel_606.place(x=170,y=10,width=222,height=30)

        GLabel_397=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_397["font"] = ft
        GLabel_397["fg"] = "#333333"
        GLabel_397["justify"] = "center"
        GLabel_397["text"] = "Enter Text Below!"
        GLabel_397.place(x=10,y=60,width=266,height=34)


        self.GLineEdit_294=tk.Text(root)
        self.GLineEdit_294["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_294["font"] = ft
        self.GLineEdit_294["fg"] = "#333333"
        self.GLineEdit_294.place(x=10,y=90,width=278,height=233)

        GLabel_662=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_662["font"] = ft
        GLabel_662["fg"] = "#333333"
        GLabel_662["justify"] = "center"
        GLabel_662["text"] = "Step 1 :"
        GLabel_662.place(x=290,y=90,width=70,height=25)

        open_wapp=tk.Button(root)
        open_wapp["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        open_wapp["font"] = ft
        open_wapp["fg"] = "#000000"
        open_wapp["justify"] = "center"
        open_wapp["text"] = "Open Whatsapp"
        open_wapp.place(x=370,y=90,width=110,height=30)
        open_wapp["command"] = self.open_wapp_command

        GLabel_412=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_412["font"] = ft
        GLabel_412["fg"] = "#333333"
        GLabel_412["justify"] = "center"
        GLabel_412["text"] = "Step 2 "
        GLabel_412.place(x=290,y=140,width=70,height=25)

        log_ques=tk.Button(root)
        log_ques["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        log_ques["font"] = ft
        log_ques["fg"] = "#000000"
        log_ques["justify"] = "center"
        log_ques["text"] = "Done Scanning"
        log_ques.place(x=370,y=140,width=111,height=30)
        log_ques["command"] = self.log_ques_command

        GLabel_884=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_884["font"] = ft
        GLabel_884["fg"] = "#333333"
        GLabel_884["justify"] = "center"
        GLabel_884["text"] = "Step 3 "
        GLabel_884.place(x=290,y=190,width=70,height=25)

        choose=tk.Button(root)
        choose["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        choose["font"] = ft
        choose["fg"] = "#000000"
        choose["justify"] = "center"
        choose["text"] = "Choose CSV"
        choose.place(x=370,y=190,width=113,height=30)
        choose["command"] = self.choose_command

        start=tk.Button(root)
        start["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        start["font"] = ft
        start["fg"] = "#000000"
        start["justify"] = "center"
        start["text"] = "Start!"
        start.place(x=290,y=230,width=218,height=76)
        start["command"] = self.start_command

        logout=tk.Button(root)
        logout["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        logout["font"] = ft
        logout["fg"] = "#000000"
        logout["justify"] = "center"
        logout["text"] = "Logout!"
        logout.place(x=520,y=230,width=75,height=75)
        logout["command"] = self.logout_command

    def go_end(self):
        self.GMessage_686.see("end")
        pass

    def open_wapp_command(self):
        self.GMessage_686.insert(tk.END, "\nWhatsapp will open in a new window!")
        self.go_end()
        time.sleep(2)
        self.GMessage_686.insert(tk.END, "\nPlease scan the QR code!")
        self.go_end()
        time.sleep(2)
        sc.open_whatsapp()
        time.sleep(2)
        self.GMessage_686.insert(tk.END, "\nWhatsapp is now open!")
        self.go_end()
        time.sleep(2)
        self.GMessage_686.insert(tk.END, "\nClick on the done scanning button!")
        self.go_end()
        self.click1 = True
        pass
    


    def log_ques_command(self):
        if self.click1 == False:
            self.GMessage_686.insert(tk.END, "\nPlease click on the 'Open Whatsapp' button first!")
            self.go_end()
            return
        else:
            self.GMessage_686.insert(tk.END, "\nMinimizing Chrome!")
            self.go_end()
            sc.minimize_whatsapp()
            time.sleep(2)
            self.GMessage_686.insert(tk.END, "\nGood, Whatsapp is open now!")
            time.sleep(2)
            self.GMessage_686.insert(tk.END, "\nClick on the 'Choose CSV' button to choose the csv file!")
            self.go_end()
            self.click2 = True
            pass


    def choose_command(self):
        if self.click2 == False:
            self.GMessage_686.insert(tk.END, "\nPlease click on the 'Done Scanning' button first!")
            self.go_end()
            print(self.GLineEdit_294.get(1.0,'end-1c'))
            return
        else:
            self.filename = askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.go_end()
            self.GMessage_686.insert(tk.END, "\nCSV file has been chosen!")
            self.go_end()
            self.GMessage_686.insert(tk.END, f"\n{self.filename}")
            self.go_end()
            self.click3 = True


    def start_command(self):
        if self.click3 == False:
            self.GMessage_686.insert(tk.END, "\nPlease click on the 'Choose CSV' button first!")
            self.go_end()
            return
        elif self.GLineEdit_294.get(1.0,'end-1c') == "":
            self.GMessage_686.insert(tk.END, "\nPlease enter a message first!")
            self.go_end()
            return
        else:
            if self.filename == "":
                self.GMessage_686.insert(tk.END, "\nPlease choose a CSV file first!")
                self.go_end()
                return
            else:
                self.GMessage_686.insert(tk.END, "\nPlease wait while the messages are being sent!")
                self.go_end()
                message = self.GLineEdit_294.get(1.0,'end-1c')
                with open(self.filename, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        phone_number = row[0]
                        self.GMessage_686.insert(tk.END, f"\n{sc.send_whatsapp_message(phone_number, message)}")
                        self.go_end()
                    

   



    def logout_command(self):
        if self.click1 == False:
            self.GMessage_686.insert(tk.END, "\nYou are not logged in!")
            self.go_end()
            return
        else:
            self.GMessage_686.insert(tk.END, "\nLogging out!")
            self.go_end()
            sc.logout()
            self.GMessage_686.insert(tk.END, "\nLogged out!")
            self.go_end()
            self.GMessage_686.insert(tk.END, "\nYou can now Close the application or login again!")
            self.go_end()
            self.click1 = False
            self.click2 = False
            self.click3 = False
            self.filename = ""
            pass
           
  

