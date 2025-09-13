from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    if password_entry == "":
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
    {
        "email" : email,
        "password" : password,
    }
}

    if website == "" or password == "" or email == "":
        messagebox.showwarning(title = "Oops", message = "Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title = f"{website}", message = f"These are the details entered:\nEmail: {email}"
                                    f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            try:
                with open("PasswordManger.json", "r") as data_file:
                    data = json.load(data_file)
            
            except FileNotFoundError:
                with open("PasswordManger.json", "w") as data_file:
                    json.dump(new_data, data_file, indent = 4)
            
            else:
                data.update(new_data)
                with open("PasswordManger.json","w") as data_file:
                    json.dump(data, data_file, indent = 4)
            
            finally:
                website_entry.delete(0, END)
                website_entry.focus()
                password_entry.delete(0, END)
                email_entry.delete(0, END)
# ---------------------------- Search ------------------------------- #
def pass_search():
    website = website_entry.get()
    try:
        with open("PasswordManger.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title = "Error", message = "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title = "Error", message = "No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #
#Screen
window = Tk()
window.title("Password Manger")
window.config(padx = 50, pady = 50)

#Logo
canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column = 1, row = 0)

#Entries
website_entry = Entry(width = 41)
website_entry.grid(column = 1, row = 1)
website_entry.focus()
email_entry = Entry(width = 60)
email_entry.grid(column = 1, row = 2, columnspan = 2)
password_entry = Entry(width = 41)
password_entry.grid(column = 1, row = 3)

#Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

#Buttons
generate_button = Button(text = "Generate Password", command = generate_pass)
generate_button.grid(column = 2, row = 3)
add_button = Button(text = "Add", width = 51, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)
search_button = Button(text = "Search", width = 14, command = pass_search)
search_button.grid(column = 2, row = 1)

window.mainloop()