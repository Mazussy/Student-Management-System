# CSV-Based Record Management System

A Python GUI application demonstrating efficient file organization and record management using CSV files as a database solution.

## Features

- CSV-based data persistence with automatic file initialization
- CRUD operations (Create, Read, Update, Delete) for record management
- Record tracking using Relative Record Numbers (RRN)
- File compaction functionality to maintain data integrity
- Search functionality with case-insensitive partial matching
- Tkinter-based GUI for easy interaction

## Technical Implementation

### File Structure
```
├── main.py
├── data/
│   ├── students.csv
│   └── courses.csv
```

### Data Management
- Automatic CSV file creation with predefined headers
- Record identification using auto-incremented IDs
- Gap management through file compaction
- Dictionary-based CSV reading/writing for efficient data handling

## Installation

```bash
git clone https://github.com/yourusername/record-management.git
cd record-management
python main.py
```

## Requirements
- Python 3.x
- tkinter (included in standard Python installation)

## License
MIT License

## Author
Your Name
