# ACAD191 Project

This is the ACAD191 project workspace with a Python virtual environment setup.

## Setup Instructions

### 1. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 2. Install Dependencies

After activating the virtual environment, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Deactivate the Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## Project Structure

- `W1/` - Week 1 materials
- `venv/` - Python virtual environment (do not commit this)
- `requirements.txt` - Python package dependencies
- `.gitignore` - Git ignore rules

## Adding New Packages

To add new packages to your project:
1. Activate the virtual environment
2. Install the package: `pip install package_name`
3. Update requirements.txt: `pip freeze > requirements.txt`

## Notes

- Always activate the virtual environment before working on your project
- The virtual environment folder (`venv/`) is excluded from version control
- Keep your `requirements.txt` updated when adding new dependencies
