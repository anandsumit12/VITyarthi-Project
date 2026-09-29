# Problem Statement: Mini Hospital Management System

## Background
In healthcare settings, managing patient information efficiently is critical for providing timely and effective care. Small clinics and local hospitals often rely on manual, paper-based records to track patient admissions, doctor assignments, and treatment progress. 

## The Problem
Manual record-keeping introduces several operational challenges:
* **Data Retrieval:** Searching for specific patient records through physical files is time-consuming.
* **Tracking Inefficiencies:** It is difficult to keep track of real-time consultation statuses (e.g., who is waiting, who is currently seeing a doctor, and who has completed their visit).
* **Resource Allocation:** Manually assigning doctors and departments can lead to confusion, overlapping appointments, or unassigned patients.
* **Data Loss:** Physical records are prone to damage, misplacement, or loss.

## The Solution
The **Mini Hospital Management System** is a digital, command-line-based solution designed to streamline the front-desk operations of a small healthcare facility. By digitizing patient records, the system provides a centralized, easy-to-navigate interface for administrative staff.

## Project Objectives
1. **Streamline Patient Registration:** Allow staff to quickly add new patients with their basic details and primary health issues.
2. **Improve Data Accessibility:** Implement a search functionality to retrieve patient details instantly using their ID or Name.
3. **Optimize Resource Assignment:** Provide a clear mechanism to assign specific doctors and medical departments to registered patients.
4. **Real-Time Status Tracking:** Enable dynamic updates to a patient's consultation status (Pending, In Progress, Completed) to optimize patient flow.

## Scope
This initial version is built as a lightweight, text-based Python application utilizing in-memory data structures. It is intended to serve as a proof-of-concept or a foundational system for small clinics. Future iterations could integrate persistent database storage (like SQLite or MySQL) and graphical user interfaces (GUI) for expanded use.
