from tkinter import *
from tkinter import messagebox


curr_mon = 10
save_mon = 20
cdt_mone = 620
totl_mon = curr_mon + save_mon + cdt_mone


def increment_current_sald():
  pass

def increment_save_sald():
  pass

def increment_cdt_sald():
  pass

def reset_money():
  global curr_mon
  global save_mon
  global cdt_mone

  curr_mon = 0
  save_mon = 0
  cdt_mone = 0


root = Tk()
root.title("Peac Inc Bank Management")



Label(root, text="Saldo").grid(row=0, column=0, pady=10, padx=10)

Label(root, text="Saldo Corriente: ").grid(row=1, column=1, pady=10, padx=10)
current_sald = Label(root, text=str(curr_mon)).grid(row=1, column=2, pady=10, padx=10)
Label(root, text="Saldo Ahorros: ").grid(row=2, column=1, pady=10, padx=10)
save_sald = Label(root, text=str(save_mon)).grid(row=2, column=2, pady=10, padx=10)
Label(root, text="Saldo CDT: ").grid(row=3, column=1, pady=10, padx=10)
save_CDT = Label(root, text=str(cdt_mone)).grid(row=3, column=2, pady=10, padx=10)
Label(root, text="Total: ").grid(row=4, column=1, pady=10, padx=10)
total_sald = Label(root, text=str(totl_mon)).grid(row=4, column=2, pady=10, padx=10)


Label(root, text="Cálculos").grid(row=5, column=0, pady=10, padx=10)

btn1 = Button(root, text="Increment money", command=lambda:increment_current_sald()).grid(row=6, column=1, pady=10, padx=10)
btn2 = Button(root, text="Reset Money Salds", command=lambda:reset_money()).grid(row=6, column=2, pady=10, padx=10)



root.mainloop()