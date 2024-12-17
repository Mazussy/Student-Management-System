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
    Display dialog boxes to collect student information and add a new student record.
    Automatically generates the next available student ID.
    """
    students = read_csv(STUDENT_FILE)
    student_id = len(students) + 1  # Auto-increment ID
    
    # Collect student information through dialog boxes
    fields = {
        "name": "Enter student name:",
        "sex": "Enter student sex (Male/Female):",
        "age": "Enter student age:",
        "institution": "Enter student institution:",
        "major": "Enter student major:"
    }
    
    # Collect all required information
    info = {field: simpledialog.askstring("Add Student", prompt) 
            for field, prompt in fields.items()}
    
    # Verify all fields were filled out
    if all(info.values()):
        student = {"id": student_id, **info}
        students.append(student)
        write_csv(STUDENT_FILE, students)
        messagebox.showinfo("Success", "New student added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")


def add_course():
    """
    Display dialog boxes to collect course information and add a new course record.
    Automatically generates the next available course ID.
    """
    courses = read_csv(COURSE_FILE)
    course_id = len(courses) + 1  # Auto-increment ID
    
    # Collect course information
    fields = {
        "name": "Enter course name:",
        "credit": "Enter course credit:",
        "property": "Enter course property (Compulsory/Optional):"
    }
    
    info = {field: simpledialog.askstring("Add Course", prompt)
            for field, prompt in fields.items()}
    
    if all(info.values()):
        course = {"id": course_id, **info}
        courses.append(course)
        write_csv(COURSE_FILE, courses)
        messagebox.showinfo("Success", "New course added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")


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


def sort_entries(file_name, key):
    """
    Sort records in a file by the specified key.
    Handles numeric sorting for IDs and case-insensitive sorting for text fields.
    
    Args:
        file_name (str): Name of the file containing records to sort
        key (str): Field name to sort by
    """
    data = read_csv(file_name)
    if key == "id":
        # Sort numerically for ID field
        sorted_data = sorted(data, key=lambda x: int(x.get(key, 0)))
    else:
        # Sort alphabetically (case-insensitive) for other fields
        sorted_data = sorted(data, key=lambda x: x.get(key, "").lower())
    write_csv(file_name, sorted_data)
    messagebox.showinfo("Success", f"Data sorted by {key.capitalize()}!")


def edit_entry(file_name):
    """
    Edit an existing record identified by its RRN (Relative Record Number).
    Displays current values and allows updating each field except ID.
    
    Args:
        file_name (str): Name of the file containing the record to edit
    """
    data = read_csv(file_name)
    if not data:
        messagebox.showwarning("Error", "No entries to edit!")
        return

    data_with_rrn = calculate_rrn(data)

    # Get the RRN of the record to edit
    entry_rrn = simpledialog.askinteger("Edit Entry", "Enter the RRN of the entry to edit:")
    if not entry_rrn or entry_rrn < 1 or entry_rrn > len(data_with_rrn):
        messagebox.showwarning("Error", "Invalid RRN!")
        return

    # Edit each field except ID and RRN
    entry = data_with_rrn[entry_rrn - 1]
    for key in entry:
        if key != "id" and key != "RRN":
            new_value = simpledialog.askstring(
                "Edit Entry", 
                f"Enter new value for {key.capitalize()} (current: {entry[key]}):"
            )
            if new_value:
                entry[key] = new_value

    write_csv(file_name, data)
    messagebox.showinfo("Success", "Entry updated successfully!")


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
    root.geometry("600x500")
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
        ("Sort Students by Name", lambda: sort_entries(STUDENT_FILE, "name")),
        ("Sort Courses by Name", lambda: sort_entries(COURSE_FILE, "name")),
        ("Sort Students by ID", lambda: sort_entries(STUDENT_FILE, "id")),
        ("Sort Courses by ID", lambda: sort_entries(COURSE_FILE, "id")),
        ("Edit Student Entry", lambda: edit_entry(STUDENT_FILE)),
        ("Edit Course Entry", lambda: edit_entry(COURSE_FILE)),
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