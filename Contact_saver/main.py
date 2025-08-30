# create main.py that uses file_ops.py to run the interactive contact saver 
# Main program for contact saver project

from pathlib import Path
from participant_pkg import file_ops

# Define CSV file path
csv_path = Path("workspace/contacts.csv")

def get_valid_input(prompt, validator, error_msg):
    """Helper function to keep asking until valid input is given."""
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print(error_msg)

def main():
    print("\nWelcome to Optimist Contact Saver!")

    while True:
        # Collect details with validation
        name = get_valid_input(
            "\nEnter participant name:\t",
            lambda v: v.strip() != "",
            "Name cannot be empty!"
        )

        age = get_valid_input(
            "Enter age:",
            lambda v: v.isdigit(),
            "Age must be a number!"
        )

        phone = get_valid_input(
            "Enter phone number:",
            lambda v: v.isdigit() and len(v) >= 11,
            "Phone must be digits and at least 11 characters!"
        )

        track = get_valid_input(
            "Enter track:",
            lambda v: v.strip() != "",
            "Track cannot be empty!"
        )

        # Save as dictionary
        participant = {
            "Name": name,
            "Age": int(age),
            "Phone": phone,
            "Track": track
        }

        file_ops.save_participant_informations(csv_path, participant)
        print(f"\n Saved {name} successfully!\n")

        more = input("Add another participant? (yes/no): ").lower()
        if more != "yes":
            break


    all_participants = file_ops.load_participant_informations(csv_path)
    print(f"\n Total participants saved: {len(all_participants)}")
    for p in all_participants:
        print(f"- {p['Name']} ({p['Age']} yrs, {p['Phone']}, Track: {p['Track']})")

if __name__ == "__main__":
    main()
