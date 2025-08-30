# Creating two functions
# save_participant(path, participant_dict)
# load_participants(path)
import csv
from pathlib import Path


# defined a function called save_participant(path, participant_dict)

def save_participant_informations(path: Path, informations: dict ):

    # Save information collected into the CSV file.
    file_exists = path.exists()

    try:
        # Check if file is empty or doesn't exist
        if not file_exists or path.stat().st_size == 0:
            # Write with header for new or empty files
            with path.open(mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])
                writer.writeheader()
                writer.writerow(informations)
        else:
            # Append without header for existing files
            with path.open(mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])
                writer.writerow(informations)
    except Exception as e:
        print(f"Error saving participant information: {e}")




def load_participant_informations(path: Path):
    """Load all participants from the CSV file and return as list of dicts."""
    informations = []
    if not path.exists():
        return informations  # return empty if file doesn't exist

    try:
        with path.open(mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                informations.append(row)
    except Exception as e:
        print(f"Error loading participant informations: {e}")

    return informations