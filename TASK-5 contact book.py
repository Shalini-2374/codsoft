import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Initialize data file
data_file = 'contacts.json'

def load_contacts():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(data_file, 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = simpledialog.askstring("Add Contact", "Name:")
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return
    phone = simpledialog.askstring("Add Contact", "Phone Number:")
    email = simpledialog.askstring("Add Contact", "Email:")
    address = simpledialog.askstring("Add Contact", "Address:")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    update_contact_list()

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone']:
            contact_list.insert(tk.END, f"{name} - {info['phone']}")

def update_contact():
    name = contact_list.get(tk.ANCHOR).split(' - ')[0]
    if not name:
        messagebox.showerror("Error", "Please select a contact to update")
        return
    phone = simpledialog.askstring("Update Contact", "New Phone Number:", initialvalue=contacts[name]['phone'])
    email = simpledialog.askstring("Update Contact", "New Email:", initialvalue=contacts[name]['email'])
    address = simpledialog.askstring("Update Contact", "New Address:", initialvalue=contacts[name]['address'])
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    update_contact_list()

def delete_contact():
    name = contact_list.get(tk.ANCHOR).split(' - ')[0]
    if name:
        result = messagebox.askquestion("Delete", "Are you sure you want to delete this contact?")
        if result == 'yes':
            del contacts[name]
            save_contacts(contacts)
            update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

# Main window
root = tk.Tk()
root.title("Contact Manager")

# Initialize contacts
contacts = load_contacts()

# Layout
contact_list = tk.Listbox(root, height=12, width=50)
contact_list.grid(row=0, column=0, columnspan=3, rowspan=6, padx=10, pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=3, rowspan=6)

contact_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=contact_list.yview)

# Buttons
add_button = tk.Button(root, text="Add Contact", width=12, command=add_contact)
add_button.grid(row=0, column=4)

view_button = tk.Button(root, text="View Contacts", width=12, command=view_contacts)
view_button.grid(row=1, column=4)

search_button = tk.Button(root, text="Search Contact", width=12, command=search_contact)
search_button.grid(row=2, column=4)

update_button = tk.Button(root, text="Update Contact", width=12, command=update_contact)
update_button.grid(row=3, column=4)

delete_button = tk.Button(root, text="Delete Contact", width=12, command=delete_contact)
delete_button.grid(row=4, column=4)

# Initial contact list update
update_contact_list()

# Start the GUI event loop
root.mainloop()
