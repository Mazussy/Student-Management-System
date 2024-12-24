# Student and Course Management System
# This program implements a GUI-based system for managing student and course records
# using CSV files as a simple database solution. It provides CRUD operations
# (Create, Read, Update, Delete) for both students and courses.

import os
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

# Define constants for data storage
# These files will store our student and course information in CSV format
STUDENT_FILE = 'students.csv'
COURSE_FILE = 'courses.csv'

# Define the expected number of fields for each record type
# This helps ensure data consistency and proper record formatting
STUDENT_RECORD_LENGTH = 6  # Fields: id, name, sex, age, institution, major
COURSE_RECORD_LENGTH = 4   # Fields: id, name, credit, property


def initialize_files():
    """
    Ensure that the necessary CSV files exist and are properly initialized with headers.
    If the files don't exist, create them with appropriate column headers.
    """
    file_configurations = [
        (STUDENT_FILE, ['id', 'name', 'sex', 'age', 'institution', 'major']),
        (COURSE_FILE, ['id', 'name', 'credit', 'property'])
    ]
    
    for file_name, header in file_configurations:
        if not os.path.exists(file_name):
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)


def read_csv(file_name):
    """
    Read data from a CSV file and convert it to a list of dictionaries.
    Each dictionary represents one record with field names as keys.
    
    Args:
        file_name (str): Name of the CSV file to read
        
    Returns:
        list: List of dictionaries containing the CSV data
    """
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def write_csv(file_name, data):
    """
    Write a list of dictionaries to a CSV file, maintaining the field order.
    
    Args:
        file_name (str): Name of the CSV file to write to
        data (list): List of dictionaries containing the data to write
    """
    if data:
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def calculate_rrn(data):
    """
    Add Relative Record Numbers (RRN) to each record.
    RRN is used to identify records by their position in the file.
    
    Args:
        data (list): List of record dictionaries
        
    Returns:
        list: Data with added RRN field
    """
    for i, row in enumerate(data, start=1):
        row['RRN'] = i
    return data


def display_data(data):
    """
    Format data for display in the GUI, including RRN for each record.
    
    Args:
        data (list): List of record dictionaries
        
    Returns:
        str: Formatted string representation of the data
    """
    data_with_rrn = calculate_rrn(data)
    if data_with_rrn:
        return "\n".join(
            [
                f"RRN: {entry['RRN']}\n" + "\n".join(
                    [f"{key.capitalize()}: {value}" for key, value in entry.items() if key != 'RRN']
                ) + "\n" + "-" * 40
                for entry in data_with_rrn
            ]
        )
    else:
        return "No data available."


def add_student():
    """
    Display a single window with entry fields for all student information 
    and add a new student record.
    """
    def save_student():
        # Collect data from entry fields
        info = {
            "name": name_entry.get(),
            "sex": sex_entry.get(),
            "age": age_entry.get(),
            "institution": institution_entry.get(),
            "major": major_entry.get(),
        }
        
        if all(info.values()):  # Ensure all fields are filled
            students = read_csv(STUDENT_FILE)
            student_id = len(students) + 1  # Auto-increment ID
            student = {"id": student_id, **info}
            students.append(student)
            write_csv(STUDENT_FILE, students)
            messagebox.showinfo("Success", "New student added successfully!")
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    # Create a new window for adding student details
    add_window = tk.Toplevel()
    add_window.title("Add Student")
    add_window.geometry("600x500")
    
    # Add entry fields for student details
    tk.Label(add_window, text="Enter Student Details", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Label(add_window, text="Name:").pack()
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack(pady=5)
    
    tk.Label(add_window, text="Sex (Male/Female):").pack()
    sex_entry = tk.Entry(add_window, width=30)
    sex_entry.pack(pady=5)
    
    tk.Label(add_window, text="Age:").pack()
    age_entry = tk.Entry(add_window, width=30)
    age_entry.pack(pady=5)
    
    tk.Label(add_window, text="Institution:").pack()
    institution_entry = tk.Entry(add_window, width=30)
    institution_entry.pack(pady=5)
    
    tk.Label(add_window, text="Major:").pack()
    major_entry = tk.Entry(add_window, width=30)
    major_entry.pack(pady=5)
    
    # Add Save button
    tk.Button(add_window, text="Save", command=save_student, bg="#4caf50", fg="white").pack(pady=20)


def add_course():
    """
    Display a single window with entry fields for all course information 
    and add a new course record.
    """
    def save_course():
        # Collect data from entry fields
        info = {
            "name": name_entry.get(),
            "credit": credit_entry.get(),
            "property": property_entry.get(),
        }
        
        if all(info.values()):  # Ensure all fields are filled
            courses = read_csv(COURSE_FILE)
            course_id = len(courses) + 1  # Auto-increment ID
            course = {"id": course_id, **info}
            courses.append(course)
            write_csv(COURSE_FILE, courses)
            messagebox.showinfo("Success", "New course added successfully!")
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    # Create a new window for adding course details
    add_window = tk.Toplevel()
    add_window.title("Add Course")
    add_window.geometry("600x500")
    
    # Add entry fields for course details
    tk.Label(add_window, text="Enter Course Details", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Label(add_window, text="Name:").pack()
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack(pady=5)
    
    tk.Label(add_window, text="Credit:").pack()
    credit_entry = tk.Entry(add_window, width=30)
    credit_entry.pack(pady=5)
    
    tk.Label(add_window, text="Property (Compulsory/Optional):").pack()
    property_entry = tk.Entry(add_window, width=30)
    property_entry.pack(pady=5)
    
    # Add Save button
    tk.Button(add_window, text="Save", command=save_course, bg="#4caf50", fg="white").pack(pady=20)



def show_students():
    """Display all student records in a formatted message box."""
    students = read_csv(STUDENT_FILE)
    result = display_data(students)
    messagebox.showinfo("Student Information", result)


def show_courses():
    """Display all course records in a formatted message box."""
    courses = read_csv(COURSE_FILE)
    result = display_data(courses)
    messagebox.showinfo("Course Information", result)


def search_student():
    """
    Search for students by name (case-insensitive partial match).
    Displays all matching records in a message box.
    """
    name = simpledialog.askstring("Search Student", "Enter student name to search:")
    if name:
        students = read_csv(STUDENT_FILE)
        results = [entry for entry in students if name.lower() in entry["name"].lower()]
        result = display_data(results)
        messagebox.showinfo("Search Results", result if results else f"No match found for '{name}'.")


def search_course():
    """
    Search for courses by name (case-insensitive partial match).
    Displays all matching records in a message box.
    """
    name = simpledialog.askstring("Search Course", "Enter course name to search:")
    if name:
        courses = read_csv(COURSE_FILE)
        results = [entry for entry in courses if name.lower() in entry["name"].lower()]
        result = display_data(results)
        messagebox.showinfo("Search Results", result if results else f"No match found for '{name}'.")


def edit_entry(file_name, record_type):
    """
    Edit an existing record identified by its RRN (Relative Record Number).
    Display a single window with all fields for editing.
    
    Args:
        file_name (str): Name of the file containing the record to edit
        record_type (str): Type of record ("student" or "course") for field labels
    """
    data = read_csv(file_name)
    if not data:
        messagebox.showwarning("Error", f"No {record_type}s to edit!")
        return

    data_with_rrn = calculate_rrn(data)

    # Get the RRN of the record to edit
    entry_rrn = simpledialog.askinteger("Edit Entry", f"Enter the RRN of the {record_type} to edit:")
    if not entry_rrn or entry_rrn < 1 or entry_rrn > len(data_with_rrn):
        messagebox.showwarning("Error", "Invalid RRN!")
        return

    # Get the record to edit
    entry = data_with_rrn[entry_rrn - 1]

    def save_changes():
        for key, widget in entries.items():
            if key != "id" and widget.get():
                entry[key] = widget.get()
        write_csv(file_name, data)
        messagebox.showinfo("Success", f"{record_type.capitalize()} updated successfully!")
        edit_window.destroy()

    # Create the edit window
    edit_window = tk.Toplevel()
    edit_window.title(f"Edit {record_type.capitalize()} Entry")
    edit_window.geometry("600x500")

    tk.Label(edit_window, text=f"Edit {record_type.capitalize()} Details", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Create entry fields for all editable fields
    entries = {}
    for key, value in entry.items():
        if key != "RRN":  # RRN is not editable
            tk.Label(edit_window, text=f"{key.capitalize()}:").pack(pady=5)
            entry_widget = tk.Entry(edit_window, width=30)
            entry_widget.insert(0, value)  # Pre-fill with current value
            entry_widget.pack(pady=5)
            entries[key] = entry_widget

    # Add Save button
    tk.Button(edit_window, text="Save", command=save_changes, bg="#4caf50", fg="white").pack(pady=20)

def delete_entry(file_name):
    """
    Delete a record identified by its RRN (Relative Record Number).
    
    Args:
        file_name (str): Name of the file containing the record to delete
    """
    data = read_csv(file_name)
    if not data:
        messagebox.showwarning("Error", "No entries to delete!")
        return

    data_with_rrn = calculate_rrn(data)

    # Get the RRN of the record to delete
    entry_rrn = simpledialog.askinteger("Delete Entry", "Enter the RRN of the entry to delete:")
    if not entry_rrn or entry_rrn < 1 or entry_rrn > len(data_with_rrn):
        messagebox.showwarning("Error", "Invalid RRN!")
        return

    # Remove the record and save
    data.pop(entry_rrn - 1)
    write_csv(file_name, data)
    messagebox.showinfo("Success", "Entry deleted successfully!")


def compact_file(file_name):
    """
    Remove any gaps in the file that might have been created by deletions.
    This ensures continuous record numbering and optimal file organization.
    
    Args:
        file_name (str): Name of the file to compact
    """
    data = read_csv(file_name)
    write_csv(file_name, data)
    messagebox.showinfo("Success", "File compacted and gaps removed!")


def main():
    """
    Main function that sets up the GUI and creates all necessary buttons
    for interacting with the student and course management system.
    """
    initialize_files()

    # Create and configure the main window
    root = tk.Tk()
    root.title("Student and Course Management System")
    root.geometry("900x800")
    root.configure(bg="#f5f5f5")

    # Add title label
    tk.Label(root, text="Student and Course Management System", 
             font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

    # Define common button styles
    button_style = {
        "width": 25,
        "font": ("Helvetica", 12),
        "bg": "#4caf50",
        "fg": "white",
        "relief": "raised",
        "bd": 3
    }

    # Create all operation buttons
    buttons = [
        ("Show Students", show_students),
        ("Add Student", add_student),
        ("Show Courses", show_courses),
        ("Add Course", add_course),
        ("Search Student by Name", search_student),
        ("Search Course by Name", search_course),
        ("Edit Student Entry", lambda: edit_entry(STUDENT_FILE, "student")),
        ("Edit Course Entry", lambda: edit_entry(COURSE_FILE, "course")),

        ("Delete Student Entry", lambda: delete_entry(STUDENT_FILE)),
        ("Delete Course Entry", lambda: delete_entry(COURSE_FILE)),
        ("Compact Students File", lambda: compact_file(STUDENT_FILE)),
        ("Compact Courses File", lambda: compact_file(COURSE_FILE)),
        ("Exit", root.quit)
    ]

    # Create and pack all buttons
    for text, command in buttons:
        tk.Button(root, text=text, command=command, **button_style).pack(pady=5)

    # Start the application
    root.mainloop()


if __name__ == "__main__":
    main()
