from re import search
from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2,4))]


    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = ''
    for i in password_list:
      password+=i
    password_entry.delete(0,END)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    new_data = {
        website_entry.get() : {
            "email" : un_entry.get(),
            "password": password_entry.get(),
        }
    }

    if website_entry.get().istitle():

        if len(website_entry.get())==0 or len(password_entry.get())==0 or len(un_entry.get())==0 :
            messagebox.showerror(title="Oops",message=f"Don't leave any fields empty.")


        else:

            is_ok = messagebox.askokcancel(title=(website_entry.get()),message=f"Username/Email : {un_entry.get()} \nPassword : {password_entry.get()} \n\nClick ok to save  ")



            if is_ok:
                try:
                    with open("data.json","r") as dataFile:

                        #Reading old Data
                        data = json.load(dataFile)

                        #Updating old data with new data
                        data.update(new_data)
                    with open("data.json","w") as DataFile:

                        #Adding the data to the JSON file
                        json.dump(data,DataFile,indent=4)
                    
                        website_entry.delete(0,END)
                        un_entry.delete(0,END)
                        password_entry.delete(0,END)
                except FileNotFoundError:

                    with open("data.json","w") as data:

                        json.dump(new_data,data,indent=4)
    else:
        messagebox.showinfo(message="Only title case allowed in website name.")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
 

    except:
        messagebox.showinfo(title= "Error", message="No data found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email : {email} \nPassword : {password}")
        else:
            messagebox.showinfo(title="error" , message=f"No details for {website} exists")


    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,120,image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text=" Website : ",font=("arial",12,"normal"))
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus_set()

un_label = Label(text="Email/Username : ",font=("arial",12,"normal"))
un_label.grid(column=0,row=2)

un_entry = Entry(width=35)
un_entry.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password : ",font=("arial",12,"normal"))
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3,columnspan=1)

password_button = Button(text="Generate Password ",command=generate_password)
password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=add)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text=" search ",command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()