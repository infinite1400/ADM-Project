from tkinter import *

root=Tk()

root.geometry("1600x900")
root["bg"]=["#EBDEF0"]
mur=Label(root,text="NIT KKR",font=("ROG FONTS",70),padx=300,pady=100,bg="#EBDEF0").pack()

#frame 

fra_adm=LabelFrame(text="LOGIN",padx=150,pady=100,border=5,font=("BOLD"),bg="#85C1E9")
fra_adm.pack(padx=30)

#entry user 

user_entry=Label(fra_adm,text="Username :- ",padx=10,font=("BOLD"),bg="#85C1E9")
user_entry.grid(row=0,column=1)
user_entry_e=Entry(fra_adm,width=30,border=3)
user_entry_e.grid(row=0,column=2)


user_entry1=Label(fra_adm,text="Password :- ",padx=10,font=("BOLD"),bg="#85C1E9")
user_entry1.grid(row=1,column=1)
user_entry_e1=Entry(fra_adm,width=30,border=3)
user_entry_e1.grid(row=1,column=2)

log_but=Button(fra_adm,text="LOGIN",width=30,border=3,bg="#2ECC71").grid(row=2,column=1,columnspan=2,pady=10)
clear_but=Button(fra_adm,text="Clear",width=30,border=3,bg="#2ECC71").grid(row=3,column=1,columnspan=2,pady=5)


root.mainloop()