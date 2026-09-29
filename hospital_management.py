patients = []

patients.append({
    "id": "101",
    "name": "Sumit Anand",
    "age": "21",
    "gender": "Male",
    "issue": "fever & cold",
    "doctor": "Dr. Sharma",
    "dept": "General Physician",
    "status": "Completed"
})

patients.append({
    "id": "102",
    "name": "Piyush kant",
    "age": "19",
    "gender": "Female",
    "issue": "Skin Allergy",
    "doctor": "Dr. Kapoor",
    "dept": "Dermatology",
    "status": "In Progress"
})

patients.append({
    "id": "103",
    "name": "Dharmendra",
    "age": "22",
    "gender": "Male",
    "issue": "Joint Pain",
    "doctor": "Not Assigned",
    "dept": "Not Assigned",
    "status": "Pending"
})

run = True

while run == True:
    print("\n--- MINI HOSPITAL MANAGEMENT SYSTEM ---")
    print("1. Display All Patient Details")
    print("2. Add New Patient")
    print("3. Search Patient")
    print("4. Assign Doctor & Department")
    print("5. Update Consultation Status")
    print("6. Exit")
    
    ch = input("Enter your choice (1-6): ")
    
    if ch == '1':
        print("\n--- ALL PATIENT RECORDS ---")
        if len(patients) == 0:
            print("No records found in the hospital system!")
        else:
            for p in patients:
                print("ID         :", p["id"])
                print("Name       :", p["name"])
                print("Age/Gender :", p["age"], "/", p["gender"])
                print("Issue      :", p["issue"])
                print("Doctor     :", p["doctor"])
                print("Department :", p["dept"])
                print("Status     :", p["status"])
                print("-" * 35)
                
    # Option 2: Add new patient record
    elif ch == '2':
        print("\n--- ADD NEW PATIENT ---")
        p_id = input("Enter Patient ID: ")
        
        # Check if ID already exists
        duplicate = False
        for p in patients:
            if p["id"] == p_id:
                duplicate = True
                break
                
        if duplicate == True:
            print("Patient ID already exists! Try another ID.")
        else:
            p_name = input("Enter Patient Name: ")
            p_age = input("Enter Age: ")
            p_gender = input("Enter Gender: ")
            p_issue = input("Enter Health Issue / Symptom: ")
            
            # Default values for newly added patient
            new_p = {
                "id": p_id,
                "name": p_name,
                "age": p_age,
                "gender": p_gender,
                "issue": p_issue,
                "doctor": "Not Assigned",
                "dept": "Not Assigned",
                "status": "Pending"
            }
            patients.append(new_p)
            print("Patient added successfully!!")
            
    # Option 3: Search patient by ID or Name
    elif ch == '3':
        print("\n--- SEARCH PATIENT ---")
        search_term = input("Enter Patient ID or Name to search: ")
        found = False
        
        for p in patients:
            if search_term.lower() in p["id"].lower() or search_term.lower() in p["name"].lower():
                print("\nMatch Found!")
                print("ID         :", p["id"])
                print("Name       :", p["name"])
                print("Age/Gender :", p["age"], "/", p["gender"])
                print("Issue      :", p["issue"])
                print("Doctor     :", p["doctor"])
                print("Department :", p["dept"])
                print("Status     :", p["status"])
                print("-" * 35)
                found = True
                
        if found == False:
            print("No matching patient record found.")
            
    # Option 4: Doctor and Department Assignment
    elif ch == '4':
        print("\n--- ASSIGN DOCTOR & DEPARTMENT ---")
        p_id = input("Enter Patient ID to assign doctor: ")
        found = False
        
        for p in patients:
            if p["id"] == p_id:
                found = True
                print("Selected Patient:", p["name"], "(Issue:", p["issue"], ")")
                doc_name = input("Enter Doctor Name: ")
                dept_name = input("Enter Department Name: ")
                
                p["doctor"] = doc_name
                p["dept"] = dept_name
                print("Doctor and Department assigned successfully!")
                break
                
        if found == False:
            print("Wrong Patient ID!")
            
    # Option 5: Update Consultation Status
    elif ch == '5':
        print("\n--- UPDATE CONSULTATION STATUS ---")
        p_id = input("Enter Patient ID: ")
        found = False
        
        for p in patients:
            if p["id"] == p_id:
                found = True
                print("Current Status for", p["name"], "is:", p["status"])
                print("1. Set to Pending")
                print("2. Set to In Progress")
                print("3. Set to Completed")
                
                st_choice = input("Enter choice (1-3): ")
                if st_choice == '1':
                    p["status"] = "Pending"
                    print("Status updated to Pending.")
                elif st_choice == '2':
                    p["status"] = "In Progress"
                    print("Status updated to In Progress.")
                elif st_choice == '3':
                    p["status"] = "Completed"
                    print("Status updated to Completed.")
                else:
                    print("Invalid status option selected!")
                break
                
        if found == False:
            print("Wrong Patient ID!")
            
    # Option 6: Exit
    elif ch == '6':
        print("\nThank you for using Mini Hospital Management System!")
        print("Exiting program...")
        run = False
        
    else:
        print("Wrong option entered! Please try again.")
