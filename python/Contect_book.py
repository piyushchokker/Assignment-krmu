"""
Project: Contact Book Management System
Author: Kartik Patidar
Roll-No: 2501940026
Date: 13-Nov-2025
Course: Programming for Problem Solving using Python
"""
import csv
import json
from datetime import datetime

CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json"
ERROR_LOG = "error_log.txt"

def log_error(error_message, operation):
    """Logs errors with timestamp and operation details."""
    with open(ERROR_LOG, "a") as f:
        f.write(f"[{datetime.now()}] {operation}: {error_message}\n")

def read_contacts():
    """Reads all contacts from CSV and returns a list of dictionaries."""
    contacts = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            contacts = list(reader)
    except FileNotFoundError:
        log_error("CSV file not found", "Read Contacts")
    except Exception as e:
        log_error(str(e), "Read Contacts")
    return contacts

def write_contacts(contacts):
    """Writes a list of contact dictionaries to CSV."""
    try:
        with open(CSV_FILE, "w", newline="") as f:
            fieldnames = ["name", "phone", "email"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
    except Exception as e:
        log_error(str(e), "Write Contacts")

def add_contact():
    """Adds a new contact."""
    try:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()

        contacts = read_contacts()
        contacts.append({"name": name, "phone": phone, "email": email})
        write_contacts(contacts)

        print(f"\n Contact '{name}' added successfully!\n")
    except Exception as e:
        log_error(str(e), "Add Contact")

def display_contacts():
    """Displays all contacts in tabular format."""
    contacts = read_contacts()
    if not contacts:
        print("\n No contacts found.\n")
        return

    print("\n Contact List:")
    print("-" * 50)
    print(f"{'Name':<15}\t{'Phone':<15}\t{'Email'}")
    print("-" * 50)
    for c in contacts:
        print(f"{c['name']:<15}\t{c['phone']:<15}\t{c['email']}")
    print("-" * 50)

def search_contact():
    """Search contact by name."""
    name = input("Enter name to search: ").strip().lower()
    contacts = read_contacts()
    found = [c for c in contacts if c["name"].lower() == name]

    if found:
        print("\n Contact Found:")
        for c in found:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print(f"\n No contact found with name '{name}'.\n")

def update_contact():
    """Update phone or email of a contact."""
    name = input("Enter name to update: ").strip().lower()
    contacts = read_contacts()
    for c in contacts:
        if c["name"].lower() == name:
            print("\nLeave blank if you don't want to change a field.")
            new_phone = input("Enter new phone: ").strip()
            new_email = input("Enter new email: ").strip()
            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            write_contacts(contacts)
            print(f"\n Contact '{name}' updated successfully!\n")
            return
    print(f"\n No contact found with name '{name}'.\n")

def delete_contact():
    """Delete contact by name."""
    name = input("Enter name to delete: ").strip().lower()
    contacts = read_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(updated_contacts) < len(contacts):
        write_contacts(updated_contacts)
        print(f"\n Contact '{name}' deleted successfully!\n")
    else:
        print(f"\n No contact found with name '{name}'.\n")

def export_to_json():
    """Export all contacts from CSV to JSON file."""
    try:
        contacts = read_contacts()
        with open(JSON_FILE, "w") as f:
            json.dump(contacts, f, indent=4)
        print(f"\n Contacts exported to {JSON_FILE} successfully!\n")
    except Exception as e:
        log_error(str(e), "Export to JSON")

def load_from_json():
    """Load and display contacts from JSON file."""
    try:
        with open(JSON_FILE, "r") as f:
            contacts = json.load(f)
        print("\n Contacts Loaded from JSON:")
        print("-" * 50)
        for c in contacts:
            print(f"{c['name']:<15}\t{c['phone']:<15}\t{c['email']}")
        print("-" * 50)
    except FileNotFoundError:
        print("\n JSON file not found.\n")
        log_error("JSON file not found", "Load from JSON")
    except Exception as e:
        log_error(str(e), "Load from JSON")

def main():
    print("=" * 60)
    print(" Welcome to Contact Book Manager")
    print("=" * 60)

    while True:
        print("""
1  Add Contact
2  Display All Contacts
3  Search Contact
4  Update Contact
5  Delete Contact
6  Export Contacts to JSON
7  Load Contacts from JSON
8  Exit
""")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            export_to_json()
        elif choice == "7":
            load_from_json()
        elif choice == "8":
            print("\n Exiting Contact Book.\n")
            break
        else:
            print("\n Invalid choice! Please enter a number between 1-8.\n")

if __name__ == "__main__":
    main()
