from tkinter import *
from sq10 import linkDb
import sqlite3
import  threading, time , os

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "Input:"
        self.inputText.grid(row=0, column=0)
        
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1)

        self.pinge = Button(self)
        self.pinge["text"] = "Ping"
        self.pinge["command"]=self.saveDb
        self.pinge.grid(row=0, column=2 )

        self.ping=Button(self)
        self.ping["text"]="Go_Ping"
        self.ping["command"]=self.gping
        self.ping.grid(row=0, column=3 )

    def saveDb(self):  
        d=linkDb()
        d.li()
    def gping(self):
        i=1
        j=0
        k=[]
        q=0
        a=0
        s=linkDb()
        ka=s.sping()
        for x in ka:
         response=os.system("ping %s" %(x))
         if response ==0:
           outText = Label(self)
           outText["text"]=("%s is on " %(x))
           outText.grid(row=i, column=j)
           j+=1
           print(j)
           if j==2:
               j=0
               i+=1
         else:
             k.append(x)
        for p in k:
          outText2 = Label(self)
          outText2["text"]=("%s is down " %(p))
          outText2.grid(row=i+1+a, column=q)
          q+=1
          if q==2:
               q=0
               a+=1
             
        
         
  
if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()
