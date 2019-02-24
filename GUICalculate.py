from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# this is a function for store a programe

def calprofit():
    at = int(alltank.get())
    # .get() is a pulling data out from box
    cal_sell = at * 30
    cal_cost = at * 20
    profit = cal_sell - cal_cost
    rolex = (profit * 1000000) // 350000
    textshow = 'ได้กำไรจากการขายรถถัง {:,d} ล้านบาท\n'.format(profit)
    textshow2 = 'ซื้อนาฬิกาได้ทั้งหมด {:,d} เรือน'.format(rolex)
    messagebox.showinfo('My Profit',textshow+textshow2)

GUI = Tk()
GUI.geometry('500x500+100+100')
GUI.title('Tank Profit Calculation')

#Button 1 is Old Button
#BCal = Button(GUI,text='Calculate')
#BCal.pack()

#Text box for enter the value
#StringVar is box that can flexible value

bg = PhotoImage(file='tank.png').subsample(4)

tankpic = ttk.Label(GUI, image=bg)
tankpic.pack(pady=20)

#text show for user
tanktext = ttk.Label(GUI, text='กรุณากรอกจำนวนรถถังที่ต้องการขาย\nขายคันละ 30 ล้าน กำไรคันละ 10 ล้าน',font=('Angsana New',20))
tanktext.pack()

alltank = StringVar()

ETank = ttk.Entry(GUI,textvariable = alltank,font=('Angsana New',20))
ETank.pack(pady=20)

#Button 2 is New Button
#Just add ttk before Button
BCal2 = ttk.Button(GUI,text='Calculate',command=calprofit)
BCal2.pack(ipadx=20,ipady=10)

GUI.mainloop()








