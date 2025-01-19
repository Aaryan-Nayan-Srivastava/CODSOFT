from tkinter import *
window=Tk()
#Function to click the button
def click_button(button):
    current=display.get()
    display.delete(0,END)
    display.insert(0,current+str(button))

#Function to clear the display
def clear_screen():
    display.delete(0,END)

#Function to calculate the result
def calculate():
    result=eval(display.get())
    display.delete(0,END)
    display.insert(0,str(result))
#Function to check the button
def button_check(button):
    if button not in ['C','=']:
        click_button(button)
    elif button=='C':
        clear_screen()
    else:
        calculate()


#WINDOW TITLE
window.title(" My Calculator ")
window.geometry("400x450")
#Display screen
display=Entry(window,width=29,font=('Arial',18),bd=10,insertwidth=4,bg="powder blue",justify='right')
display.grid(row=0,column=0,columnspan=4,rowspan=2)
spacer = Label(window, text="") 
spacer.grid(row=2, column=0, columnspan=4)
#Buttons
buttons=['7','8','9','/',
         '4','5','6','*',
         '1','2','3','-',
         'C','0','=','+'
        ]
row_val=3
col_val=0
for button in buttons:
    button=Button(window,text=button,padx=20,pady=20,font=('Arial',18),command= lambda button=button:button_check(button))
    button.grid(row=row_val,column=col_val)
    col_val+=1
    if(col_val>3):
        col_val=0
        row_val+=1

#Main loop
window.mainloop()
