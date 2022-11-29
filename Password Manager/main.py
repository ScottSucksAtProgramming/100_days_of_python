# ---------------------------- Resources ------------------------------- #
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for letter in range(0, nr_letters)]
    number_list = [random.choice(numbers) for number in range(0, nr_numbers)]
    symbol_list = [random.choice(symbols) for symbol in range(0, nr_symbols)]
    password = letter_list + number_list + symbol_list

    random.shuffle(password)
    password = "".join(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

SPACER = "    |   "


def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

# Check to see if any of the boxes are blank, if they are, show and error and cancel function.
    if len(website) < 1 or len(username) < 1 or len(password) <1:
        messagebox.showerror(title="You fucked up", message="You have not completed all the entries.")
        return
    else:
        try:
            with open(file="./data.json", mode="r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="./data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if website in data:
                messagebox.showinfo(title="Password Exists", message="You already have a password for this website.")
                return
            else:
                # Update old data with new data
                data.update(new_data)

                with open(file="./data.json", mode="w") as data_file:
                    # Save updated data
                    json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, 'end')
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()

    try:
        with open("./data.json", mode="r") as data_file:
            data = json.load(data_file)
            username = data[website]['username']
            password = data[website]['password']
    except KeyError:
        messagebox.showerror(title="Missing Data", message=f"There is no entry for {website}.")
        website_entry.delete(0,tkinter.END)
        website_entry.focus()
    except FileNotFoundError:
        messagebox.showerror(title="No Data File", message="No data file has been created. Try saving a password first.")
    else:
        messagebox.showinfo(title="Data Found Found", message=f"Username: {username}\nPassword: {password}"
                                                              f"\nPassword copied.")
        pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
# Create the window.
window = tkinter.Tk()
window.title("Completely Secure Password Manager. Trust Me.")
window.config(padx=20, pady=50)

# Create the canvas and place the image in the center of the screen.
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create Labels and Text Entries.
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1)
# Set the cursor to be in the website entry at program launch.
website_entry.focus()

username_label = tkinter.Label(text="Username / E-mail:")
username_label.grid(column=0, row=2)
username_entry = tkinter.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
# Populate with commonly used e-mail address.
username_entry.insert(0, "SRKos@aol.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

# Create Buttons
generate_button = tkinter.Button(text="Generate Password", command=gen_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()