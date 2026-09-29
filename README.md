# VITyarthi-Project
# Mini Hospital Management System 

A lightweight, command-line-based Python application to manage patient records, assign doctors, and track consultation statuses in a small clinic or hospital setting.

## Features

This system provides an interactive menu with the following capabilities:
- **Display All Patient Details:** View a formatted list of all registered patients and their current medical and consultation details.
- **Add New Patient:** Register a new patient by entering their ID, name, age, gender, and health issue. 
- **Search Patient:** Quickly look up a patient using their unique ID or Name.
- **Assign Doctor & Department:** Allocate a specific doctor and medical department to a pending patient.
- **Update Consultation Status:** Track the patient's journey by updating their status to `Pending`, `In Progress`, or `Completed`.

## Prerequisites

- **Python 3.x** must be installed on your system. 

## How to Run

1. Save the python script to a file, for example, `hospital_management.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the script using the following command:
   ```bash
   python hospital_management.py
   ```
5. Follow the on-screen prompts to interact with the system.

## Usage Example

When you start the application, you will see the main menu:

```text
--- MINI HOSPITAL MANAGEMENT SYSTEM ---
1. Display All Patient Details
2. Add New Patient
3. Search Patient
4. Assign Doctor & Department
5. Update Consultation Status
6. Exit
Enter your choice (1-6): 
```

Type a number between 1 and 6 and press **Enter** to navigate through the application. 

## Structure 

The program relies on a central list of dictionaries (in-memory data structure) to store patient information. Please note that because there is no external database integrated, any new patients added during runtime will be cleared when the program exits.
