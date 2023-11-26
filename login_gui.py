from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import hashlib
import socket

# Class for the Login GUI
class Login:
    def __init__(self, root):
        # GUI Initialization
        self.root = root
        self.root.title('')
        self.root.geometry('800x600+570+200')
        self.root.resizable(False, False)
        self.root['background'] = 'gray14'

        #Login Frame
        self.Frame_login = Frame(self.root, bg='white')
        self.Frame_login.place(x=20, y=20, width=760, height=560)

        #Title & Subtitle
        self.title = Label(self.Frame_login, text='Login Here', font=('Impact', 35, 'bold'), fg='#6162FF', bg='white').place(x=90, y=30)
        self.subtitle = Label(self.Frame_login, text='Members Login Area', font=('Goudy old style', 15, 'bold'), fg='#1d1d1d', bg='white').place(x=90, y=100)

        #Username
        self.lbl_user = Label(self.Frame_login, text='Username', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white').place(x=90, y=140)
        self.username= Entry(self.Frame_login, font=('Goudy old style', 15), bg='#E7E6E6')
        self.username.place(x=90, y=170, width=320, height=35)

        #Password
        self.lbl_password = Label(self.Frame_login, text='Password', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white').place(x=90, y=210)
        self.password = Entry(self.Frame_login, font=('Goudy old style', 15), bg='#E7E6E6', show='*')
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        self.forget = Button(self.Frame_login, command=self.forgot_pass, text='Forgot Password?', bd=0, cursor='hand2', font=('Goudy old style', 12), fg='#6162FF', bg='white').place(x=90, y=280)
        self.submit = Button(self.Frame_login, text="Login", command=self.check_function, font=('Arial', 12, 'bold'), bg='#6162FF', fg='white', padx=10, pady=5, cursor='hand2', borderwidth=2,  relief=FLAT ).place(x=90, y=320, width=180, height=40)
        self.register_button = Button(self.Frame_login, text="Register", command=self.create_acc, font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', padx=10, pady=5, cursor='hand2', borderwidth=2,  relief=FLAT ).place(x=90, y=370, width=180, height=40)

        # Create Account Frame
        self.Frame_create_account = Frame(self.root, bg='white')
        self.title_create_account = Label(self.Frame_create_account, text='Create Account', font=('Impact', 35, 'bold'), fg='#6162FF', bg='white')
        self.subtitle_create_account = Label(self.Frame_create_account, text='New Members Registration', font=('Goudy old style', 15, 'bold'), fg='#1d1d1d', bg='white')
        self.lbl_user_create_account = Label(self.Frame_create_account, text='Username', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white')
        self.username_create_account = Entry(self.Frame_create_account, font=('Goudy old style', 15), bg='#E7E6E6')
        self.lbl_password_create_account = Label(self.Frame_create_account, text='Password', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white')
        self.password_create_account = Entry(self.Frame_create_account, font=('Goudy old style', 15), bg='#E7E6E6', show='*')
        self.submit_create_account = Button(self.Frame_create_account, text="Register", command=self.check_function_create_account, font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', padx=10, pady=5, cursor='hand2', borderwidth=2,  relief=FLAT )
        self.back_to_login = Button(self.Frame_create_account, text="Back to Login", command=self.redirect_login, font=('Arial', 12, 'bold'), bg='#6162FF', fg='white', padx=10, pady=5, cursor='hand2', borderwidth=2,  relief=FLAT )
    
    # Function to handle the login process
    def check_function(self):
        if self.username.get()=='' or self.password.get()=='':
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(("localhost", 9999))
                data_to_send = f"{self.username.get()}|{self.password.get()}"
                client.send(data_to_send.encode())
                message = client.recv(1024).decode()

                if message == 'True':
                    success_label_login = Label(self.Frame_login, text='Login successfull! Loading application...', font=('Goudy old style', 12), fg='green', bg='white')
                    success_label_login.place(x=90, y=320)
                    self.root.update_idletasks()
                    self.root.after(2000, lambda: self.load_config())

                elif message == 'False':
                    invalid_label_login = Label(self.Frame_login, text='Login failed! Try again...', font=('Goudy old style', 12), fg='red', bg='white')
                    invalid_label_login.place(x=90, y=320)
                    self.root.after(2000, lambda: invalid_label_login.destroy())
            except socket.error as e:
                messagebox.showerror('Connection Error', f'Unable to connect to the server. {e}', parent=self.root)

    # Function to load configuration after successful login
    def load_config(self):
        self.root.destroy()
        import settings_gui

    # Function to handle the "Forgot Password" functionality
    def forgot_pass(self):
        messagebox.showinfo('Account Recovery', 'Contact developer for password reset', parent=self.root)

    # Function to switch to the account creation view
    def create_acc(self):
        self.Frame_login.place_forget()
        self.Frame_create_account.place(x=20, y=20, width=760, height=560)
        self.title_create_account.place(x=90, y=30)
        self.subtitle_create_account.place(x=90, y=100)
        self.lbl_user_create_account.place(x=90, y=140)
        self.username_create_account.place(x=90, y=170, width=320, height=35)
        self.lbl_password_create_account.place(x=90, y=210)
        self.password_create_account.place(x=90, y=240, width=320, height=35)
        self.submit_create_account.place(x=90, y=320, width=180, height=40)
        self.back_to_login.place(x=90, y=370, width=180, height=40)

    # Function to redirect after a successful operation
    def redirect_after_success(self, label):
        label.destroy()
        self.redirect_login()
        
    # Function to switch back to the login view
    def redirect_login(self):
        self.Frame_create_account.place_forget()
        self.Frame_login.place(x=20, y=20, width=760, height=560)

    # Function to handle the account creation process
    def check_function_create_account(self):
        if self.username_create_account.get()=='' or self.password_create_account.get()=='':
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                client_username = self.username_create_account.get()
                client_password = self.password_create_account.get()

                try:
                    #Change MySQL host/user/password/database based on your personal database or create a free one at sql3.freesqldatabase.com
                    conn = mysql.connector.connect(
                        host='sql3.freesqldatabase.com',
                        user='sql3663427',
                        password='2qAN3996zk',
                        database='sql3663427'
                        )
                except Exception as e:
                    messagebox.showerror('Database Error', f'Error connecting to the database: {e}', parent=self.root)

                cur = conn.cursor()

                try:
                    cur.execute("""
                    CREATE TABLE IF NOT EXISTS userdata (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                    """)
                except Exception as e:
                    messagebox.showerror('Database Error', f'Error creating database table: {e}', parent=self.root)
                cur.execute("SELECT * FROM userdata WHERE username=%s", (client_username,))

                existing_user = cur.fetchone()

                if existing_user:
                    messagebox.showerror('Username Taken', 'Username already taken. Please choose a different username.', parent=self.root)
                    
                else:
                    client_password = hashlib.sha256(client_password.encode()).hexdigest()
                    cur.execute("INSERT INTO userdata (username, password) VALUES (%s, %s)", (client_username, client_password))
                    conn.commit()
                    success_label = Label(self.Frame_create_account, text='Account created successfully! Redirecting...', font=('Goudy old style', 12), fg='green', bg='white')
                    success_label.place(x=90, y=320)
                    self.root.after(2000, lambda: self.redirect_after_success(success_label))
            except Exception as e:
                messagebox.showerror('Database Error', f'Error accessing the database. {e}', parent=self.root)
            finally:
                if 'conn' in locals():
                    conn.close()

# Main entry point
if __name__ == '__main__':
    root = Tk()
    obj = Login(root)
    root.mainloop()