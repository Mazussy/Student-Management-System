# Student and Course Management System

A desktop application built with Python and Tkinter that provides a comprehensive solution for managing student and course records. The system uses CSV files as a lightweight database solution, offering full CRUD (Create, Read, Update, Delete) operations for both student and course data.

## Features

The system provides an intuitive graphical interface with the following capabilities:

### Student Management
- Add new student records with details like name, sex, age, institution, and major
- View all student records in a formatted display
- Search for students by name
- Sort students by name or ID
- Edit existing student information
- Delete student records

### Course Management
- Add new course records with details like name, credit hours, and property (Compulsory/Optional)
- View all course records in a formatted display
- Search for courses by name
- Sort courses by name or ID
- Edit existing course information
- Delete course records

### File Management
- Automatic file initialization with appropriate headers
- File compaction to remove gaps after record deletion
- Relative Record Number (RRN) system for easy record identification

## Technical Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)
- CSV module (part of Python standard library)
- OS module (part of Python standard library)

## Installation

1. Clone this repository or download the source code:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

2. Ensure Python 3.x is installed on your system. You can verify this by running:
```bash
python --version
```

3. Run the application:
```bash
python main.py
```

## Usage

When you start the application, you'll see a window with multiple buttons for different operations:

1. **Adding Records**
   - Click "Add Student" or "Add Course"
   - Fill in the requested information in the dialog boxes
   - System automatically assigns an ID to new records

2. **Viewing Records**
   - Click "Show Students" or "Show Courses"
   - Records are displayed with their Relative Record Numbers (RRN)

3. **Searching Records**
   - Click "Search Student by Name" or "Search Course by Name"
   - Enter full or partial name to search
   - System displays all matching records

4. **Editing Records**
   - Click "Edit Student Entry" or "Edit Course Entry"
   - Enter the RRN of the record to edit
   - Modify the desired fields

5. **Deleting Records**
   - Click "Delete Student Entry" or "Delete Course Entry"
   - Enter the RRN of the record to delete

6. **Sorting Records**
   - Use the sort buttons to organize records by name or ID
   - Changes are saved automatically

## Data Storage

The system uses two CSV files for data storage:
- `students.csv`: Stores student records
- `courses.csv`: Stores course records

### Data Structure

**Student Records:**
```
id, name, sex, age, institution, major
```

**Course Records:**
```
id, name, credit, property
```

## Error Handling

The system includes various error checks:
- Validation for required fields
- Checks for valid RRN when editing or deleting
- File existence verification
- Data integrity checks during operations


## Changelog

### Version 1.0.0
- Initial release with basic CRUD operations
- CSV-based data storage
- Complete GUI implementation
- Search and sort functionality
- File compaction feature

