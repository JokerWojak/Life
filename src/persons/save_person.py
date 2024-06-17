import os
import json
import random
import sys

def save_person_to_json(person, filename):
    """
    Save a Person object to a JSON file.

    Args:
        person (Person): The Person object to save.
        filename (str): The path where the JSON file should be saved.

    Returns:
        str: The full path where the JSON file is saved.
    """
    print(f"Saving person {person.id} to JSON...")

    # Ensure saving only to the specified directory
    save_dir = os.path.dirname(filename)
    os.makedirs(save_dir, exist_ok=True)

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

    # Save data to JSON file
    with open(filename, 'w') as f:
        json.dump(data_to_save, f, indent=4)

    print(f"Saved {person.id} to {filename}")
    return filename