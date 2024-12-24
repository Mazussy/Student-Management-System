# Student and Course Management System

A Python-based GUI application for managing student and course records using CSV files as a simple database solution.

## Features

- **Student Management**
  - Add new students with details (name, sex, age, institution, major)
  - View all student records
  - Search students by name
  - Edit existing student records
  - Delete student records

- **Course Management**
  - Add new courses with details (name, credit, property)
  - View all course records
  - Search courses by name
  - Edit existing course records
  - Delete course records

- **File Management**
  - Automatic file initialization
  - File compaction to remove gaps
  - CSV-based data persistence

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-course-management.git
cd student-course-management
```

2. Install required dependencies:
```bash
pip install tkinter
```

## Usage

Run the application:
```bash
python main.py
```

The system will automatically create two CSV files (`students.csv` and `courses.csv`) if they don't exist.

### Data Structure

#### Students CSV Format
- id: Unique identifier
- name: Student's full name
- sex: Student's gender
- age: Student's age
- institution: Educational institution
- major: Field of study

#### Courses CSV Format
- id: Unique identifier
- name: Course name
- credit: Course credit hours
- property: Course type (Compulsory/Optional)

## Technical Details

- Built with Python's `tkinter` library for GUI
- Uses CSV files for data storage
- Implements CRUD operations (Create, Read, Update, Delete)
- Features relative record number (RRN) for record identification

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- CSV module (built into Python)
- OS module (built into Python)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name

## Acknowledgments

- Thanks to all contributors who have helped with this project
- Inspired by the need for simple student and course management systems
