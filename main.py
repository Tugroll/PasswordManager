from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generated_password = []

let_ran = random.randint(8, 10)
num_ran = random.randint(2, 4)
sym_ran = random.randint(2, 4)

for item in range(let_ran):
    generated_password.append(random.choice(letters))
for item in range(num_ran):
    generated_password.append(random.choice(numbers))
for item in range(sym_ran):
    generated_password.append(random.choice(symbols))

random.shuffle(generated_password)

def make_the_password():
    gene_pass = ""
    for item in generated_password:
        gene_pass += item

    password_entry.insert(0,gene_pass)



#------------------Find Data in JSON------------------------------#

def find_data():
    website = website_entry.get()
    try:
        with open("password.json", mode="r") as file:
            find_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"there is no file as {file} in data base")
    else:
        if website in find_data:
            email = find_data[website]["email"]
            password = find_data[website]["password"]

            messagebox.showinfo(title="Info", message=f"Email : {email} \n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"{website} , there is no website in data base")


# ---------------------------- SAVE PASSWORD ------------------------------- #

#need to use ui_entries to encapsulate
def save_data():
    customer_data = ""
    customer_data += f"{website_entry.get()} || {email_entry.get()} || {password_entry.get()}\n"
    new_data = {
        website_entry.get():{
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }

    if len(website_entry.get()) == 0 or len(email_entry.get())== 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="You cannot leave the box blank")

    else:
        try:
            with open("password.json",mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
             with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
             data.update(new_data)
             with open("password.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0, column=1)

website_l = Label(text="Website")
website_l.grid(row=1,column=0)
website_email = Label(text="Email/Username")
website_email.grid(row=2,column=0)
website_password = Label(text="Password")
website_password.grid(row=3,column=0)

#Entries
website_entry = Entry()
website_entry.grid(row=1,column=1, sticky='ew')
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2,column=1, columnspan=2, sticky='ew')
email_entry.insert(0,"tgrlarmn5@gmail.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='ew')


#Buttons
search_button = Button(text="Search",command=find_data)
search_button.grid(row=1,column=2, sticky='ew',padx= 5,pady = 2)

generate_password_button = Button(text="Generate Password", command=make_the_password)
generate_password_button.grid(row=3, column=2, padx= 5,pady = 5)

add_button = Button(text="Add", width=36,command=save_data)
add_button.grid(row=4,column=1,columnspan=2, sticky='ew')

window.mainloop()