import tkinter as tk
from tkinter import font
from tkinter import filedialog

# Define a list to store the lines
lines = []

# Define a function to add a new line
def add_line():
    line = entry.get()
    if line:
        lines.append(line)
        entry.delete(0, tk.END)
        display_lines()

# Define a function to display the lines
def display_lines():
    # Clear the current listbox
    listbox.delete(0, tk.END)
    
    # Add each line to the listbox with its corresponding line number
    for i, line in enumerate(lines):
        if i == 0:
            listbox.insert(tk.END, f"{i+1}. {line}")
        else:
            if "*" in line:
                listbox.insert(tk.END, f"{i+1}. \u0336{line[2:]}\u0336")
            else:
                listbox.insert(tk.END, f"{i+1}. {line}")

# Define a function to cross out a line and any lines before it
def cross_out_line():
    selection = listbox.curselection()
    if selection:
        selection = selection[0]
        for i in range(selection + 1):
            lines[i] = f"~~{lines[i]}~~"
        display_lines()

# Define a function to delete a line
def delete_line():
    selection = listbox.curselection()
    if selection:
        selection = selection[0]
        del lines[selection]
        display_lines()

# Define a function to load a checklist from a file
def load_checklist():
    file_path = filedialog.askopenfilename(defaultextension=".cheklist", filetypes=[("Cheklist Files", "*.cheklist")])
    if file_path:
        with open(file_path, "r") as f:
            global lines
            lines = [line.strip() for line in f.readlines()]
            display_lines()

# Define a function to save the current checklist to a file
def save_checklist():
    file_path = filedialog.asksaveasfilename(defaultextension=".cheklist", filetypes=[("Cheklist Files", "*.cheklist")])
    if file_path:
        with open(file_path, "w") as f:
            for line in lines:
                f.write(line + "\n")

# Create the GUI window
root = tk.Tk()
root.title("CheK! Todo Manager")

# Create the input field and "Add Line" button
entry = tk.Entry(root)
entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(root, text="Add Line", command=add_line)
add_button.pack(side=tk.LEFT)

# Create the listbox to display the lines
listbox_font = font.Font(family="TkFixedFont")
listbox = tk.Listbox(root, width=50, height=20, font=listbox_font)
listbox.pack(pady=10)

# Create the "Cross Out Line" button
cross_out_button = tk.Button(root, text="Cross Out Line", command=cross_out_line)
cross_out_button.pack(side=tk.LEFT, padx=10)

# Create the "Delete Line" button
delete_button = tk.Button(root, text="Delete Line", command=delete_line)
delete_button.pack(side=tk.LEFT, padx=10)

# Create the "Load Checklist" button
load_button = tk.Button(root, text="Load Checklist", command=load_checklist)
load_button.pack(side=tk.LEFT, padx=10)

# Create the "Save Checklist" button
save_button = tk.Button(root, text="Save Checklist", command=save_checklist)
save_button.pack(side=tk.LEFT, padx=10)


# Define a function to save the current checklist to a file
def save_checklist():
    # Open a file dialog to choose a file to save the checklist to
    filename = filedialog.asksaveasfilename(defaultextension=".cheklist")
    if filename:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")

# Define a function to load a checklist from a file
def load_checklist():
    # Open a file dialog to choose a file to load the checklist from
    filename = filedialog.askopenfilename(defaultextension=".cheklist")
    if filename:
        with open(filename, "r") as f:
            global lines
            lines = [line.strip() for line in f.readlines()]
            display_lines()

# Display the initial lines
display_lines()

# Start the GUI event loop
root.mainloop()

