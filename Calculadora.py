from tkinter import *

root = Tk()

root.title("Calculator")

index = 0

#Functions

#Funtion to see numbers in order
def get_numbers(n):
    global index
    display.insert(index, n)
    index+=1

#Functions to see operators
def get_operations(operator):
    global index
    operator_lenght = len(operator)
    display.insert(index, operator)
    index+=operator_lenght

#Function to delete all of things on the valors.
def clean_display():
    display.delete(0, END)

#Function to delete one of things on the valors.
def clean_one():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clean_display()
        display.insert(0, display_new_state)
    else:
        clean_display()

#Function to do the operations.
def calculate():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clean_display()
        display.insert(0,result)
    except:
        clean_display()
        display.insert(0, 'Error')



#For start the programm
display = Entry(root)

#For view what numbers you introduce in your calculator.
display.grid(row = 1, columnspan=6, sticky=W+E)

#Numeric Buttons
Button(root, text="1", command=lambda:get_numbers(1)).grid(row = 2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:get_numbers(2)).grid(row = 2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row = 2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row = 3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row = 3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row = 3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row = 4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row = 4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row = 4, column=2, sticky=W+E)

#Buttons for help

Button(root, text="AC", command=lambda:clean_display()).grid(row = 5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:get_numbers(0)).grid(row = 5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:get_operations("%")).grid(row = 5, column=2, sticky=W+E)

#Operators
Button(root, text="+", command=lambda:get_operations("+")).grid(row = 2, column= 3, sticky=W+E)
Button(root, text="-", command=lambda:get_operations("-")).grid(row = 3, column= 3, sticky=W+E)
Button(root, text="*", command=lambda:get_operations("*")).grid(row = 4, column= 3, sticky=W+E)
Button(root, text="/", command=lambda:get_operations("/")).grid(row = 5, column= 3, sticky=W+E)

Button(root, text="<-",command=lambda:clean_one()).grid(row = 2, column= 4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda:get_operations("**")).grid(row = 3, column= 4, sticky=W+E)
Button(root, text="^2", command=lambda:get_operations("**2")).grid(row = 3, column= 5, sticky=W+E)
Button(root, text="(", command=lambda:get_operations("(")).grid(row = 4, column= 4, sticky=W+E)
Button(root, text=")", command=lambda:get_operations(")")).grid(row = 4, column= 5, sticky=W+E)
Button(root, text="=", command=lambda:calculate()).grid(row = 5, column= 4, sticky=W+E, columnspan=2)

#For finish the programm.
root.mainloop()