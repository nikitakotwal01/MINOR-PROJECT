import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import messagebox

def submit_patient_info():
    name = name_entry.get()
    gender = gender_var.get()
    age = age_entry.get()
    
    # Check if name is not empty
    if not name.strip():
        messagebox.showerror("Error", "Please enter a valid name.")
        return
    
    # Check if gender is selected
    if gender == "None":
        messagebox.showerror("Error", "Please select a gender.")
        return
    
    # Check if age is a positive integer
    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age.")
        return
    
  
    
    # Create a new window for displaying output
    output_window = tk.Tk()
    output_window.title("Patient Information Output")
    output_window.geometry("600x600")  # Set window size
    
    # Display the output at the center with increased font size
    output_label = ttk.Label(output_window, text=f"Patient Name: {name}\nGender: {gender}\nAge: {age}", font=("Helvetica", 12), justify="center")
    output_label.place(relx=0.5, rely=0.5, anchor="center")
    
      # Close the current window
    root.destroy()
    # Run the disease prediction script as a subprocess
    subprocess.run(["python", "disease_predictor.py"])
    
    output_window.mainloop()

root = tk.Tk()
root.title("Patient Information")
root.geometry("400x250")  # Set window size

# Create a frame to organize the layout
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Patient Name
name_label = ttk.Label(main_frame, text="Patient Name:", font=("Helvetica", 12))
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = ttk.Entry(main_frame, style="Custom.TEntry")
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Gender
gender_label = ttk.Label(main_frame, text="Gender:", font=("Helvetica", 12))
gender_label.grid(row=1, column=0, padx=5, pady=5)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(main_frame, textvariable=gender_var, values=["None", "Male", "Female", "Other"])
gender_combobox.grid(row=1, column=1, padx=5, pady=5)
gender_combobox.current(0)  # Set default value to "None"

# Age
age_label = ttk.Label(main_frame, text="Age:", font=("Helvetica", 12))
age_label.grid(row=2, column=0, padx=5, pady=5)

age_entry = ttk.Entry(main_frame)
age_entry.grid(row=2, column=1, padx=5, pady=5)

# Submit Button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_patient_info)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Center the main frame within the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_frame.grid_rowconfigure((0, 1, 2), weight=1)
main_frame.grid_columnconfigure((0, 1), weight=1)

root.mainloop()