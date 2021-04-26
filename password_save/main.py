# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
import pyperclip
import json





def generatee():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    l1=[password_list.append(random.choice(letters)) for char in range(nr_letters)]

    l2=[password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    l3=[password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.insert(0,password)
    pyperclip.copy(password)



# # ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_web.get()
    print(website)
    email = entry_email.get()
    password = entry_password.get()
    new_data_json = {
        website:{
            "email" : email,
            "password" : password
        }
    }

    if len(email) == 0 or len(password)==0 or len(website) ==0:
        messagebox.showinfo(title="error", message="please fill all labels")
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
    #                                                           f"Password: {password} \n Is it ok to save?")
    #     if is_ok:
    else:
        try:
            with open("data.json",mode="r") as file:
                #Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data_json, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data_json)
            with open("data.json", mode="w") as file:
                #saving updated data
                json.dump(data, file, indent=4)
                # file.write(f"{website.title()} | {email} | {password}\n")
        finally:
            entry_web.delete(0, END)
            entry_password.delete(0, END)
#--------- search ------------------------------------------->
def search():
    website = entry_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Password Manager")
window.config(padx = 100, pady = 100)
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(row=1,column=0)

entry_web = Entry(width=34)
entry_web.grid(column=1, row=1)
entry_web.focus()


email_user_label = Label(text="Email/username:")
email_user_label.grid(column=0, row=2)

entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan =2 )
entry_email.insert(0,"bharani@gmail.com")
entry_email.focus()

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

entry_password = Entry(width=33)
entry_password.grid(column=1,row=3)
entry_password.focus()

Gen_password_label = Button(text="Generate Password", width =14,command = generatee)
Gen_password_label.grid(column=2, row=3)

search_button = Button(text = "search", width =14, command = search)
search_button.grid(column=2, row=1)

add_label = Button(text="Add", width = 44, command = add_data)
add_label.grid(column=1, row=4, columnspan=2)





window.mainloop()

