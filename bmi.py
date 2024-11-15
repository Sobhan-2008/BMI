from tkinter import *

# Create the main window
win = Tk()
win.geometry('700x500')
win.configure(bg='#93ffcb')

# Function to calculate BMI and determine the weight status
def bmi():

    height = ent_high.get()
    weight = ent_weight.get()
    

    height = float(height)
    weight = float(weight)
    
    # Calculate BMI
    bmi_value = weight / (height ** 2)
    
    # Determine weight status
    if bmi_value < 18.5:
        status = 'لاغر'
    elif 18.5 <= bmi_value < 25:
        status = 'وزن نرمال'
    elif 25 <= bmi_value < 30:
        status = 'اضافه وزن'
    elif 30 <= bmi_value < 35:
        status = 'چاقی درجه 1'
    elif 35 <= bmi_value < 40:
        status = 'چاقی درجه 2'
    else:
        status = 'چاقی درجه 3 (خیلی چاق)'
    
    # Update the result label with BMI value and status
    lbl_r.config(text=f'شاخص توده بدنی: {bmi_value:.2f}\nوضعیت: {status}')

# Widgets
lbl_high = Label(win, text='قد (متر):', font='arial 25 bold',bg = '#67d9cf')
lbl_high.place(x=100, y=100)

lbl_weight = Label(win, text='وزن (کیلوگرم):', font='arial 25 bold',bg = '#67d9cf')
lbl_weight.place(x=100, y=175)

lbl_age = Label(win, text='سن (سال):', font='arial 25 bold', bg='#67d9cf')
lbl_age.place(x=100, y=250)  # Adding label for age

lbl_ui = Label(win, text='* شاخص توده بدنی *', font='arial 25 bold')
lbl_ui.place(x=250, y=20)

lbl_r = Label(win, font='arial 25 bold',bg = '#f9ffa3')
lbl_r.place(x=300, y=370)

ent_high = Entry(win, width=10, font='arial 24 bold')
ent_high.place(x=300, y=100)

ent_weight = Entry(win, width=10, font='arial 24 bold')
ent_weight.place(x=300, y=175)

ent_age = Entry(win, width=10, font='arial 24 bold')
ent_age.place(x=300, y=250)  

btn_bmi = Button(win, text='محاسبه', font='arial 30 bold',bg = '#00f27b', command=bmi)
btn_bmi.place(x=100, y=370)  


win.mainloop()
