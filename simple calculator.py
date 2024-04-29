# Python program to create a simple root 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
expression = "" 


# Function to update expression 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialize the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def C(): 
	global expression 
	expression = "" 
	equation.set("") 

def AC():
	global expression
	expression =""
	equation.set("")



# Driver code 
if __name__ == "__main__": 
	# create a root window 
	root = Tk() 

	# set the background colour of root window 
	root.configure(background="grey")
	# set the title of root window 
	root.title("Simple Calculator") 

	# set the configuration of root window 
	root.geometry("430x280") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(root,justify = RIGHT, textvariable=equation,bd=9,bg="grey",font=("ariel,20"),borderwidth=14) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=80, ipadx=90)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(root, text=' 1 ', fg='white', bg='black', 
					command=lambda: press(1), height=2, width=14) 
	button1.grid(row=2, column=0) 

	button2 = Button(root, text=' 2 ', fg='white', bg='black', 
					command=lambda: press(2), height=2, width=14) 
	button2.grid(row=2, column=1) 

	button3 = Button(root, text=' 3 ', fg='white', bg='black', 
					command=lambda: press(3), height=2, width=14) 
	button3.grid(row=2, column=2) 

	button4 = Button(root, text=' 4 ', fg='white', bg='black', 
					command=lambda: press(4), height=2, width=14) 
	button4.grid(row=3, column=0) 

	button5 = Button(root, text=' 5 ', fg='white', bg='black', 
					command=lambda: press(5), height=2, width=14) 
	button5.grid(row=3, column=1) 

	button6 = Button(root, text=' 6 ', fg='white', bg='black', 
					command=lambda: press(6), height=2, width=14) 
	button6.grid(row=3, column=2) 

	button7 = Button(root, text=' 7 ', fg='white', bg='black', 
					command=lambda: press(7), height=2, width=14) 
	button7.grid(row=4, column=0) 

	button8 = Button(root, text=' 8 ', fg='white', bg='black', 
					command=lambda: press(8), height=2, width=14) 
	button8.grid(row=4, column=1) 

	button9 = Button(root, text=' 9 ', fg='white', bg='black', 
					command=lambda: press(9), height=2, width=14) 
	button9.grid(row=4, column=2) 

	button0 = Button(root, text=' 0 ', fg='white', bg='black', 
					command=lambda: press(0), height=2, width=14) 
	button0.grid(row=5, column=0)

	buttonx = Button(root, text=' ( ', fg='white', bg='black', 
					command=lambda: press('('), height=2, width=14) 
	buttonx.grid(row=6, column=2)

	buttony = Button(root, text=' ) ', fg='white', bg='black', 
					command=lambda: press (')'), height=2, width=14) 
	buttony.grid(row=6, column=3)

	plus = Button(root, text=' + ', fg='white', bg='black', 
				command=lambda: press("+"), height=2, width=14) 
	plus.grid(row=2, column=3) 

	minus = Button(root, text=' - ', fg='white', bg='black', 
				command=lambda: press("-"), height=2, width=14) 
	minus.grid(row=3, column=3) 

	multiply = Button(root, text=' * ', fg='white', bg='black', 
					command=lambda: press("*"), height=2, width=14) 
	multiply.grid(row=4, column=3) 

	divide = Button(root, text=' / ', fg='white', bg='black', 
					command=lambda: press("/"), height=2, width=14) 
	divide.grid(row=5, column=3) 

	equal = Button(root, text=' = ', fg='white', bg='red', 
				command=equalpress, height=2, width=14) 
	equal.grid(row=5, column=2) 

	C = Button(root, text='C', fg='white', bg='black', 
				command=C, height=2, width=14) 
	C.grid(row=5, column='1') 

	AC = Button(root, text='AC', fg='white', bg='black', 
				command=AC, height=2, width=14) 
	AC.grid(row=6, column='1')
	
		 
	Decimal= Button(root, text='.', fg='white', bg='black', 
					command=lambda: press('.'), height=2, width=14) 
	Decimal.grid(row=6, column=0)

	 
	# start the root 
	root.mainloop() 

