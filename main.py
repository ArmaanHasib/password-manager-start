from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#password_entry = None

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Hey, do not leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
                # Updating new data
                data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Writing new data
                json.dump(new_data, data_file, indent=4)


        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()




# ------------------------- FIND PASSWORD ----------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading Old Data
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"Details for {website} Not Found")
            # for key, value in data.items():
            #     if key == website:
            #         password = value["password"]
            #         email = value["email"]
            #         messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found")








# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/ Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entry

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "armaanhasib@yahoo.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)



# Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, columnspan=2)








window.mainloop()

