import tkinter as tk
import random
import string

def generate_password():
    password_length = int(password_length_entry.get())
    if password_length < 4:
        password_display.config(text="Password length should be at least 4 characters")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_display.config(text=f"Generated Password: {password}")

app = tk.Tk()
app.title("Password Generator")


password_length_label = tk.Label(app, text="Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(app)
password_length_entry.pack()


generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()


password_display = tk.Label(app, text="")
password_display.pack()

app.mainloop()
