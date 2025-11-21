# -----------------------------------------------------------
# Name: Kartik Patidar
# Roll No: 2501940026
# Date: 13-Nov-2025
# Assignment Title: Python Command-Line Attendance Tracker
# Course Code: ETCCPP171 | MCA (AI & ML)
# -----------------------------------------------------------

import datetime

# Task 1: Setup & Project Initialization
print("\nWelcome to the Python Attendance Tracker!")
print("This tool helps record and manage student attendance efficiently.\n")

# Initialize dictionary to store attendance data
attendance = {}

# Task 2: Input & Data Collection
try:
    total_entries = int(input("How many students do you want to record attendance for? "))

    for i in range(total_entries):
        print(f"\n--- Entry {i+1} ---")
        name = input("Enter student name: ").strip()

        # Task 3: Data Validation
        while name == "":
            print("Name cannot be empty. Please re-enter this student's details.")
            name = input("Enter student name again: ").strip()

        if name in attendance:
            print("This student is already marked present! Skipping duplicate entry.")
            continue

        time = input("Enter check-in time (e.g., 09:15 AM): ").strip()
        if time == "":
            print("Check-in time cannot be empty. Please re-enter.")
            time = input("Enter check-in time again (e.g., 09:15 AM): ").strip()

        # Store entry
        attendance[name] = time

except ValueError:
    print(" Invalid input! Please enter a valid number for total entries.")
    exit()

# Task 4: Attendance Summary Generation
print("\n" + "-"*40)
print(f"{'Student Name':<20}{'Check-in Time'}")
print("-"*40)

for name, time in attendance.items():
    print(f"{name:<20}{time}")

print("-"*40)
print(f"Total Students Present: {len(attendance)}")

# Task 5: Absentee Validation (Optional Enhancement)
try:
    total_students = int(input("\nEnter total number of students in the class: "))
    absentees = total_students - len(attendance)
    if absentees < 0:
        absentees = 0
    print(f"\nTotal Present: {len(attendance)}")
    print(f"Total Absent: {absentees}")
except ValueError:
    print("Skipped absentee validation (invalid total student count).")

# Task 6: Bonus - Save Attendance Report to File
save_option = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save_option == "yes":
    file_name = "attendance_log.txt"
    with open(file_name, "a") as file:
        file.write("\n" + "="*50 + "\n")
        file.write("Attendance Report\n")
        file.write("="*50 + "\n")
        file.write(f"{'Student Name':<20}{'Check-in Time'}\n")
        file.write("-"*40 + "\n")

        for name, time in attendance.items():
            file.write(f"{name:<20}{time}\n")

        file.write("-"*40 + "\n")
        file.write(f"Total Present: {len(attendance)}\n")
        try:
            file.write(f"Total Absent: {absentees}\n")
        except:
            file.write("Total Absent: Not calculated\n")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Report generated on: {current_time}\n")
    print(f"Attendance report saved successfully to '{file_name}'!")
else:
    print("Report not saved.")

print("\nThank you for using the Attendance Tracker! ✨")
