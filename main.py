import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# File names for storing data
STUDENT_FILE = 'students.json'
COURSE_FILE = 'courses.json'

def initialize_files():
    """Ensure JSON files exist and initialize them if empty."""
    for file in [STUDENT_FILE, COURSE_FILE]:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                json.dump([], f)

def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def write_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def display_data(data):
    if data:
        return "\n".join(
            ["\n".join([f"{key.capitalize()}: {value}" for key, value in entry.items()]) + "\n" + "-" * 40 for entry in data]
        )
    else:
        return "No data available."

def add_student():
    students = read_json(STUDENT_FILE)
    student_id = len(students) + 1
    name = simpledialog.askstring("Add Student", "Enter student name:")
    sex = simpledialog.askstring("Add Student", "Enter student sex (Male/Female):")
    age = simpledialog.askstring("Add Student", "Enter student age:")
    institution = simpledialog.askstring("Add Student", "Enter student institution:")
    major = simpledialog.askstring("Add Student", "Enter student major:")

    if name and sex and age and institution and major:
        student = {
            "id": student_id,
            "name": name,
            "sex": sex,
            "age": age,
            "institution": institution,
            "major": major
        }
        students.append(student)
        write_json(STUDENT_FILE, students)
        messagebox.showinfo("Success", "New student added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def add_course():
    courses = read_json(COURSE_FILE)
    course_id = len(courses) + 1
    name = simpledialog.askstring("Add Course", "Enter course name:")
    credit = simpledialog.askstring("Add Course", "Enter course credit:")
    property = simpledialog.askstring("Add Course", "Enter course property (Compulsory/Optional):")

    if name and credit and property:
        course = {
            "id": course_id,
            "name": name,
            "credit": credit,
            "property": property
        }
        courses.append(course)
        write_json(COURSE_FILE, courses)
        messagebox.showinfo("Success", "New course added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def show_students():
    students = read_json(STUDENT_FILE)
    result = display_data(students)
    messagebox.showinfo("Student Information", result)

def show_courses():
    courses = read_json(COURSE_FILE)
    result = display_data(courses)
    messagebox.showinfo("Course Information", result)

def search_student():
    name = simpledialog.askstring("Search Student", "Enter student name to search:")
    if name:
        students = read_json(STUDENT_FILE)
        results = [entry for entry in students if name.lower() in entry["name"].lower()]
        result = display_data(results)
        messagebox.showinfo("Search Results", result if results else f"No match found for '{name}'.")

def search_course():
    name = simpledialog.askstring("Search Course", "Enter course name to search:")
    if name:
        courses = read_json(COURSE_FILE)
        results = [entry for entry in courses if name.lower() in entry["name"].lower()]
        result = display_data(results)
        messagebox.showinfo("Search Results", result if results else f"No match found for '{name}'.")

def sort_entries(file_name, key):
    data = read_json(file_name)
    if key == "id":
        sorted_data = sorted(data, key=lambda x: x.get(key, 0))  # Numeric sort for ID
    else:
        sorted_data = sorted(data, key=lambda x: x.get(key, "").lower())
    write_json(file_name, sorted_data)
    messagebox.showinfo("Success", f"Data sorted by {key.capitalize()}!")

def edit_entry(file_name):
    data = read_json(file_name)
    if not data:
        messagebox.showwarning("Error", "No entries to edit!")
        return

    entry_id = simpledialog.askinteger("Edit Entry", "Enter the ID of the entry to edit:")
    if not entry_id or entry_id < 1 or entry_id > len(data):
        messagebox.showwarning("Error", "Invalid ID!")
        return

    entry = data[entry_id - 1]
    for key in entry:
        if key != "id":  # ID should not be edited
            new_value = simpledialog.askstring("Edit Entry", f"Enter new value for {key.capitalize()} (current: {entry[key]}):")
            if new_value:
                entry[key] = new_value

    write_json(file_name, data)
    messagebox.showinfo("Success", "Entry updated successfully!")

def main():
    initialize_files()

    root = tk.Tk()
    root.title("Student and Course Management System")
    root.geometry("600x500")
    root.configure(bg="#f5f5f5")

    tk.Label(root, text="Student and Course Management System", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

    button_style = {"width": 25, "font": ("Helvetica", 12), "bg": "#4caf50", "fg": "white", "relief": "raised", "bd": 3}

    tk.Button(root, text="Show Students", command=show_students, **button_style).pack(pady=5)
    tk.Button(root, text="Add Student", command=add_student, **button_style).pack(pady=5)
    tk.Button(root, text="Show Courses", command=show_courses, **button_style).pack(pady=5)
    tk.Button(root, text="Add Course", command=add_course, **button_style).pack(pady=5)
    tk.Button(root, text="Search Student by Name", command=search_student, **button_style).pack(pady=5)
    tk.Button(root, text="Search Course by Name", command=search_course, **button_style).pack(pady=5)
    tk.Button(root, text="Sort Students by Name", command=lambda: sort_entries(STUDENT_FILE, "name"), **button_style).pack(pady=5)
    tk.Button(root, text="Sort Courses by Name", command=lambda: sort_entries(COURSE_FILE, "name"), **button_style).pack(pady=5)
    tk.Button(root, text="Sort Students by ID", command=lambda: sort_entries(STUDENT_FILE, "id"), **button_style).pack(pady=5)
    tk.Button(root, text="Sort Courses by ID", command=lambda: sort_entries(COURSE_FILE, "id"), **button_style).pack(pady=5)
    tk.Button(root, text="Edit Student Entry", command=lambda: edit_entry(STUDENT_FILE), **button_style).pack(pady=5)
    tk.Button(root, text="Edit Course Entry", command=lambda: edit_entry(COURSE_FILE), **button_style).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, **button_style).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
