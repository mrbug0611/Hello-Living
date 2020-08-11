from tkinter import *
from tkinter import Toplevel
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
root.title('Graphical Login System')
photo = ImageTk.PhotoImage(file='user-login-enter-icon-person.jpg')
root.iconphoto(False, photo)

# programs register button
def register():
    global register_window
    global user_entry
    global password_entry
    
    # shows widgets on the register window
    register_window = Toplevel()
    r_top_label = Label(register_window, text='Enter details below', background='blue')
    user_label = Label(register_window, text='Username')
    user_entry = Entry(register_window)
    password_label = Label(register_window, text='Password')
    password_entry = Entry(register_window)
    save_button = Button(register_window, text='Register', padx=10, pady=10, background='blue', command=save)

    user_label.config(font=('Courier', 15))
    r_top_label.config(font=('Courier', 20))
    password_label.config(font=('Courier', 15))

    r_top_label.grid(row=0, column=0)
    user_label.grid(row=1, column=0, padx=10, pady=10)
    user_entry.grid(row=2, column=0, pady=5)
    password_label.grid(row=3, column=0, padx=10, pady=10)
    password_entry.grid(row=4, column=0, pady=5)
    save_button.grid(row=5, column=0, pady=5)


 # confirm that your username and password meets all criteria
# Then adds it to the txt file
def save():
    global user_entry
    global password_entry
    global register_window

    file_append = open('login.txt', 'a')
    file_read = open('login.txt', 'r')
    in_user = []

    for line in file_read:
        in_user = line.split()[0]

        #checks if username is already taken
        if f"('{user_entry.get()}'," in in_user:
            messagebox.showerror('Error', 'That username is already taken')
            break
    #checks username and password length
    if len(user_entry.get()) < 8 or len(password_entry.get()) < 8:
        messagebox.showerror('Error', 'Both your user name and password must be at least 8 characters long')
    
    #adds registration to txt file
    if f"('{user_entry.get()}'," not in in_user:
        if not len(user_entry.get()) < 8 or not len(password_entry.get()) < 8:
            file_append.write(f'\n{(user_entry.get(), password_entry.get())}')
            confirm_label = Label(register_window, text='You are Registered', foreground='green')
            confirm_label.config(font=('Courier', 15))
            confirm_label.grid(row=6, column=0)
            file_append.close()
            file_read.close()

# programs login button
def login():
    global login_user_entry
    global login_password_entry
    global login_window
    
    # makes login window
    login_window = Tk()
    login_top_label = Label(login_window, text='Enter Login Details')
    login_user_label = Label(login_window, text='Username')
    login_user_entry = Entry(login_window)
    login_password_label = Label(login_window, text='Login')
    login_password_entry = Entry(login_window)
    logging_in_button = Button(login_window, text='login', padx=12, pady=3, command=logging_in)

    login_top_label.config(font=('Courier', 15))
    login_user_label.config(font=('Courier', 13))
    login_password_label.config(font=('Courier', 13))

    login_top_label.grid(row=0, column=0)
    login_user_label.grid(row=1, column=0, pady=10)
    login_user_entry.grid(row=2, column=0, pady=4)
    login_password_label.grid(row=3, column=0, pady=10)
    login_password_entry.grid(row=4, column=0, pady=4)
    logging_in_button.grid(row=5, column=0, pady=10)

# confirms login
def logging_in():
    file_read = open('login.txt', 'r')
    if f"('{login_user_entry.get()}', '{login_password_entry.get()}')" in file_read.read():
        confirm_window = Toplevel()
        confirm_window_label = Label(confirm_window, text='Login Success')
        success_ok_button = Button(confirm_window, text='OK', padx=15, pady=8, command=root.quit)

        confirm_window_label.config(font=('Courier', 15))

        confirm_window_label.grid(row=0, column=0)
        success_ok_button.grid(row=1, column=0, pady=7)

    else:
        messagebox.showerror('Error', 'Your username and/or password is wrong!')

# shows the widgets in the main window when you 1st open the program. 
top_label = Label(root, text='Pick An Option', background='blue')
login_button = Button(root, text='Login', padx=50, pady=20, command=login)
register_button = Button(root, text='Register', padx=50, pady=20, command=register)

top_label.config(font=('Courier', 25))

top_label.grid(row=0, column=0)
login_button.grid(row=1, column=0, padx=10, pady=10)
register_button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
