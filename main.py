from tkinter import *
import random, string
import pyperclip
import mysql.connector
import datetime

def viewPasswords():
    print("test")

def storeToDatabase():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sayyam123",
        database="passwordgen"
    )
    if pass_str.get() == '':
        pass_str.set("Set a Password")
        return
    if field_name.get() == '':
        field_name.set("Set a field name first")
        return
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    csr = conn.cursor()
    query = "insert into passwords (fieldname,password,timestamp) values (%s,%s,%s)"
    fields = (field_name.get(),pass_str.get(),date)
    csr.execute(query,fields)
    conn.commit()
    print("Password saved : ",field_name.get(),pass_str.get(),date)
    print(csr.rowcount, "record inserted.")

def copyPassword():
    pyperclip.copy(pass_str.get())


def generator():
    password = ''

    if pass_len.get() < 4:
        pass_str.set("Select length >= 4 ")
        return

    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    password = ''.join(random.sample(password, len(password)))
    pass_str.set(password)


root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("SECURE PASSWORD GENERATOR")
root.iconbitmap(r'passgenlogo.ico')

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Generate a secure password', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack(side="top",expand = YES)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack(side="top",expand = YES)


pass_str = StringVar()
Button(root, text="GENERATE PASSWORD", command=generator).pack(pady=5,side="top",expand = YES)

Entry(root, textvariable=pass_str).pack(side="top",expand = YES)
Button(root, text='COPY TO CLIPBOARD', command=copyPassword).pack(pady=5,side="top",expand = YES)

save_label = Label(root, text='LABEL FOR PASSSWORD', font='arial 10 bold').pack(side="top",expand = YES)

field_name = StringVar()
Entry(root, textvariable=field_name).pack(side="top",expand = YES)
Button(root, text='STORE TO DATABASE', command=storeToDatabase).pack(pady=5,side="top",expand = YES)

Button(root, text='VIEW STORED PASSWORDS', command=viewPasswords).pack(pady=5,side="top",expand = YES)

root.mainloop()