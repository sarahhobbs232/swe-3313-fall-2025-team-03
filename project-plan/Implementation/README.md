# Implementation

This document provides step-by-step instructions for configuring, installing, and running the **Eternal Elixirs** web application.  
The application is fully cross-platform (Windows, macOS, Linux) and runs **entirely from the terminal** — no IDE is required.

All dependencies are installed using `requirements.txt`.

---

## Environment Setup

### 1. Install Python 3.10 or Higher

Open a terminal (Command Prompt on Windows, Terminal on macOS) and verify Python is installed:

```bash
python --version
```
or (Windows):
```bash
py --version
```
If Python is not installed, download it from:
https://www.python.org/downloads/

Windows users:
During installation, be sure to check:

```pgsql
✅ Add Python to PATH
```
---
### 2. Navigate to the Project Directory
From the terminal, navigate to the project folder:

```bash
cd <path_to_project_directory>
```
Example (Windows):
```bash
cd C:\Users\kylep\OneDrive\Desktop\EternalElixers
```
Example (macOS):
```bash
cd ~/Desktop/EternalElixers
```
3. Create a Virtual Environment
```bash
python -m venv venv
```
(Use py instead of python if required on your system.)

4. Activate the Virtual Environment
Windows:
```bash
venv\Scripts\activate
```
macOS / Linux:
```bash
source venv/bin/activate
```
When activation is successful, (venv) will appear in your terminal prompt.

5. Install Project Dependencies
All required libraries (Flask, etc.) are installed automatically using:
```bash
pip install -r requirements.txt
```
Data Storage Setup
This project uses SQLite, which is included with Python and requires no additional installation.

When the application starts:
- The SQLite database is created automatically if it does not exist
- The schema and seed data are loaded from EternalElixers.sql
No manual database configuration is required.

How to Start the Application
Ensure the virtual environment is activated, then run:
```bash
python app.py
```
The terminal will display a local server address similar to:
```cpp
http://127.0.0.1:5000
```
Copy this URL and open it in a web browser to use the application.
---
Troubleshooting
Python Command Not Found
- Reinstall Python from python.org
- Ensure Python is added to PATH (Windows)
---
Virtual Environment Will Not Activate (macOS)
Run:
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```
---
Dependency Installation Errors
Upgrade pip and retry:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
---
Application Starts but No Data Appears
Ensure EternalElixers.sql is located in the same directory as app.py.
---
Port Already in Use
If port 5000 is unavailable, run:
```bash
python app.py --port 5001
```
