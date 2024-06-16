import os
import json
import random
import sys

def save_person_to_json(person):
    """
    Save a Person object to a JSON file.

    Args:
        person (Person): The Person object to save.

    Returns:
        str: The filename where the Person data was saved.
    """
    print(f"Saving person {person.id} to JSON...")

    # Ensure saving only to the "run" directory
    save_dir = os.path.join(os.getcwd(), 'run')
    if not os.path.exists(save_dir):
        print(f"Error: Directory 'run' does not exist. Exiting with code 216615.")
        sys.exit(216615)

    # Prepare filename based on person id
    filename = f"{person.id}.json"
    save_filename = os.path.join(save_dir, filename)

    # Prepare data to save
    data_to_save = {
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'age': person.age,
        'traits': person.traits,
        'money': random.randint(1000, 10000),  # Example: Random money amount
        'property': "None",  # Example: Placeholder for property data
        'relationship': person.get_parents_relationships()  # Example: Assuming method exists
    }

    # Save data to JSON file under "run" directory
    with open(save_filename, 'w') as f:
        json.dump(data_to_save, f, indent=4)

    print(f"Saved {person.id} to {save_filename}")
    return save_filename
