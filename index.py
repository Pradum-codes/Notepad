import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to save the contents of the text edit widget to a file
def saving_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"), ("All files","*.*")])       # Prompt the user to choose a file location to save
    if not file_location:                                              # If no file location is chosen, return
        return
    with open(file_location, "w") as file_output:                      # Open the file in write mode
        text = text_edit.get("1.0", tk.END)                            # Get the contents of the text edit widget
        file_output.write(text)                                        # Write the contents to the file
    root.title(f"Humara_Notepad - {file_location}")                    # Update the window title with the file location

# Function to open a file and display its contents in the text edit widget
def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text files","*.txt"), ("All files","*.*")])       # Prompt the user to choose a file to open
    if not file_location:                                              # If no file is chosen, return
        return
    text_edit.delete("1.0", tk.END)                                    # Clear the contents of the text edit widget
    with open(file_location, "r") as file_input:                       # Open the file in read mode
        text = file_input.read()                                       # Read the contents of the file
        text_edit.insert(tk.END, text)                                 # Insert the contents into the text edit widget
    root.title(f"Humara_Notepad - {file_location}")                    # Update the window title with the file location

# Create the main window
root = tk.Tk()
root.title("Humara_Notepad")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

# Create the text edit widget
text_edit = tk.Text(root)
text_edit.grid(row=0, column=1, sticky="nsew")

# Create the frame for buttons
frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

# Create the "OPEN FILE" button and associate it with the opening_file function
button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

# Create the "SAVE FILE" button and associate it with the saving_file function
button_save = tk.Button(frame_button, text="SAVE FILE", command=saving_file)
button_save.grid(row=1,column=0, padx=5, pady=5)

# Display the frame with buttons
frame_button.grid(row=0, column=0, sticky="ns")

# Start the main event loop
root.mainloop()
 