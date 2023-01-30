#importar bibliotecas
from tkinter import *
from tkinter import messagebox
import database
import customtkinter as ctk
from tkinter import ttk

#criar a janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x350")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="LogoIcon.ico")

#Crregando imagem
logo = PhotoImage(file="logo.png")

#widgets
LeftFrame = Frame(jan, width=200, height=350, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=RIGHT)

RightFrame = Frame(jan, width=395, height=350, bg="Black", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)


UserEntry = ctk.CTkEntry(RightFrame, placeholder_text="Username", width=300, font=("Roboto", 16))
UserEntry.place(x=25, y=125)
UserLabel = ctk.CTkLabel(master=RightFrame, text="*O campo nome de usuário é obrigatório", text_color="green", font=("Roboto", 12)).place(x=25, y=155)


PassEntry = ctk.CTkEntry(RightFrame, placeholder_text="Password", width=300, font=("Roboto", 16), show="*")
PassEntry.place(x=25, y=185)
PassLabel = ctk.CTkLabel(master=RightFrame, text="*O senha é obrigatório", text_color="green", font=("Roboto", 12)).place(x=25, y=215)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    database.cursor.execute("""
        SELECT * FROM users
        WHERE (User = ? and Password = ?)
    """, (User, Pass))
    verifyLogin = database.cursor.fetchone()
    try:
        if (User in verifyLogin and Pass in verifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso negado")

#botões
LoginButton = ctk.CTkButton(RightFrame, text="Login", width=200,  fg_color="Gray", hover_color="LightGray", command=Login)
LoginButton.place(x=75, y=260)

def Register():

    #removendo os botões de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #inserindo campos de cadastro

    NomeEntry = ctk.CTkEntry(RightFrame, placeholder_text="Name", width=300, font=("Roboto", 16))
    NomeEntry.place(x=25, y=5)
    NomeLabel = ctk.CTkLabel(master=RightFrame, text="*O campo Name é obrigatório", text_color="green",font=("Roboto", 12))
    NomeLabel.place(x=25, y=35)

    EmailEntry = ctk.CTkEntry(RightFrame, placeholder_text="Email", width=300, font=("Roboto", 16))
    EmailEntry.place(x=25, y=65)
    EmailLabel = ctk.CTkLabel(master=RightFrame, text="*O campo Email é obrigatório", text_color="green",font=("Roboto", 12))
    EmailLabel.place(x=25, y=95)

    UserEntry = ctk.CTkEntry(RightFrame, placeholder_text="Username", width=300, font=("Roboto", 16))
    UserEntry.place(x=25, y=125)
    UserLabel = ctk.CTkLabel(master=RightFrame, text="*O campo Username é obrigatório", text_color="green",
                              font=("Roboto", 12))
    UserLabel.place(x=25, y=155)

    PassEntry = ctk.CTkEntry(RightFrame, placeholder_text="Password", width=300, font=("Roboto", 16), show="*")
    PassEntry.place(x=25, y=185)
    PassLabel = ctk.CTkLabel(master=RightFrame, text="*O campo Password é obrigatório", text_color="green",font=("Roboto", 12))
    PassLabel.place(x=25, y=215)



    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Senha = PassEntry.get()

        if (Name == "" or Email == "" and User == "" or Senha == ""):
            messagebox.showerror(title="Register error", message="Preencha todos os campos")
        else:
            database.cursor.execute("""
                            INSERT INTO users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
                            """, (Name, Email, User, Senha))
            database.conn.commit()
            messagebox.showinfo(title="Register info", message="Cadastro realizado")

    Register = ctk.CTkButton(RightFrame, text="Register", width=150, fg_color="green", hover_color="#2D9334", command=RegisterToDataBase)
    Register.place(x=100, y=300)

    def BackToLogin():
        #remover campos cadastro
        NomeEntry.place(x=5000)
        NomeLabel.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        Register.place(x=5000)
        back.place(x=5000)
        #trazer de volta os botões de login
        LoginButton.place(x=75)
        RegisterButton.place(x=100)

    back = ctk.CTkButton(RightFrame, text="Back", width=200,  fg_color="Gray", hover_color="LightGray", command=BackToLogin)
    back.place(x=75, y=260)

RegisterButton = ctk.CTkButton(RightFrame, text="Register", width=150, fg_color="green", hover_color="#2D9334",command=Register)
RegisterButton.place(x=100, y=300)


jan.mainloop()