import sqlite3
import  threading, time , os
class linkDb:
  def li(self):  
   cx = sqlite3.connect("EastDb.s3db")
   cu = cx.cursor()
   cu.execute("insert into mainsa(mains) values('hello srun')")
   cx.commit()
   cx.close()

  def sping(self):
   cx = sqlite3.connect("EastDb.s3db")
   cu = cx.cursor()
   cu.execute("select address from pingGo")
   ca=cu.fetchall()
   cx.commit()
   return ca
   #print("now on %s" %(ca[0]))
   #print("do %r" %(ca[0])) 116.214.12.74 222.73.174.146 103.23.108.200
   cu.close()
   
   

