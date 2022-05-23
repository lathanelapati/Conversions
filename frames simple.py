from tkinter import *
from decimal import Decimal
##round(Decimal('3.14159265359'), 3)
##Decimal('3.142')

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

def mtocm():
    meters = int(pag1_entry.get())
    
    cm =  meters*100 
    cm = str(cm)
 
    pag1_entry2.delete(0,"end")
    pag1_entry2.insert(0, cm)


def milestokm():
    miles = int(pag2_entry.get())

    km = round(miles * 1.609344,2)

    km = str(km)
    
     


    

    pag2_entry2.delete(0,"end")
    pag2_entry2.insert(0, km)


def area_of_circle():
    radius = float(pag3_entry.get())

    area = 3.171*radius*radius
    area = str(area)
    
    pag3_entry3.delete(0,"end")
    pag3_entry3.insert(0, area)

# ============= Page 1 =========

page1.config(background='teal')
pag1_label = Label(page1, text='meters to centimeters', font=('Arial', 16, 'bold'))
pag1_label.grid(row = 0, column = 2)

pag1_label = Label(page1, text='meters', font=('Arial', 15, 'bold'))
pag1_label.grid(row = 1, column = 0)

pag1_entry = Entry(page1)
pag1_entry.grid(row = 1, column = 1)

pg1_button = Button(page1, text='convert', font=('Arial', 13, 'bold'), command=mtocm) 
pg1_button.grid(row = 1, column = 2)


pag1_label2 = Label(page1, text='centimeters', font=('Arial', 15, 'bold'))
pag1_label2.grid(row = 1, column = 3)


pag1_entry2 = Entry(page1)
pag1_entry2.grid(row = 1, column = 4)

##pg1_button = Button(page1, text='convert', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))

pg1_button2 = Button(page1, text='Next', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))
pg1_button2.grid(row = 3, column = 5)

# ======== Page 2 ===========
page2.config(background='teal')
pag2_label = Label(page2, text='MilestoKm', font=('Arial', 16, 'bold'))
pag2_label.grid(row = 0, column = 3)

pag2_label = Label(page2, text='miles', font=('Arial', 15, 'bold'))
pag2_label.grid(row = 1, column = 0)

pag2_entry = Entry(page2)
pag2_entry.grid(row = 1, column = 1)

pg2_button = Button(page2, text='convert', font=('Arial', 13, 'bold'), command= milestokm)
pg2_button.grid(row = 1, column = 2)

pag2_label2 = Label(page2, text='km', font=('Arial', 15, 'bold'))
pag2_label2.grid(row = 1, column = 3)

pag2_entry2 = Entry(page2)
pag2_entry2.grid(row = 1, column = 5)


pg2_button2 = Button(page2, text='Next', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg2_button2.grid(row = 5, column = 6)

# ======== Page 3 ===========
page3.config(background='teal')
pag3_label = Label(page3, text='Area of Circle', font=('Arial', 16, 'bold'))
pag3_label.grid(row = 0, column = 3)

pag3_label = Label(page3, text='radius', font=('Arial', 15, 'bold'))
pag3_label.grid(row = 5, column = 0)

pag3_entry = Entry(page3)
pag3_entry.grid(row = 5, column = 1)

pg3_button = Button(page3, text='calculate', font=('Arial', 13, 'bold'), command=area_of_circle)
pg3_button.grid(row = 5, column = 2)

pag3_label3 = Label(page3, text='Area', font=('Arial', 15, 'bold'))
pag3_label3.grid(row = 5, column = 3)

pag3_entry3 = Entry(page3)
pag3_entry3.grid(row = 5, column = 5)





window.mainloop()
