import tkinter as tk
import random
import string

# Function to generate a strong password
def generate_password():
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special_chars = special_chars_var.get()

    characters = ''

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        password_entry.delete(0, tk.END)  # Clear the previous password
        password_entry.insert(0, "Please select at least one option.")
        return

    if password_length < 8:
        password_entry.delete(0, tk.END)  # Clear the previous password
        password_entry.insert(0, "Password length should be at least 8 characters.")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)  # Clear the previous password
    password_entry.insert(0, password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkboxes for character options
lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Entry to display the generated password
password_entry = tk.Entry(window, readonlybackground='white')
password_entry.pack()

window.mainloop()
