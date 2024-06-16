import os
import json
import random
import sys
from persons.generate_main_character import generate_main_character
from persons.person import Person

def save_game(character_label, age_label, bar_graph):
    print("Starting save_game...")

    # Generate main character
    main_character = generate_main_character(character_label, age_label, bar_graph)

    # Save main character
    main_character_filename = save_person_to_json(main_character, "main_character")

    # Generate and save family members recursively
    family_queue = main_character.generate_family()

    while family_queue:
        person = family_queue.pop(0)
        filename = save_person_to_json(person, person.id)
        print(f"Saved person to {filename}")
        family_queue.extend(person.generate_family(current_depth=person.depth))

    print("Game saved successfully!")

def save_person_to_json(person, filename):
    print(f"Saving person {person.id} to JSON...")

    # Ensure saving only to the "run" directory
    save_dir = os.path.join(os.getcwd(), 'run')
    if not os.path.exists(save_dir):
        print(f"Error: Directory 'run' does not exist. Exiting with code 216615.")
        sys.exit(216615)

    # Check if filename is valid
    if not filename or '/' in filename or '\\' in filename:
        print(f"Error: Invalid filename '{filename}'. Exiting with code 216615.")
        sys.exit(216615)

    # Prepare full path for saving
    save_filename = os.path.join(save_dir, f"{filename}.json")

    # Prepare data to save
    data_to_save = {
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'age': person.age,
        'traits': person.traits,
        'money': random.randint(1000, 10000),  # Example: Random money amount
        'property': "None",  # Example: Placeholder for property data
        'relationship': person.get_parents_relationships()  # Assuming get_parents_relationships() method exists
    }
    print(f"Data to save for {person.id}: {data_to_save}")

    # Save data to JSON file under "run" directory
    with open(save_filename, 'w') as f:
        json.dump(data_to_save, f, indent=4)

    print(f"Saved {filename} to {save_filename}")
    return save_filename

if __name__ == "__main__":
    # Example usage
    character_label = {"text": "John Smith"}  # Example character label
    age_label = {"text": "Age: 25"}  # Example age label
    bar_graph = BarGraphWidget()  # Example bar graph widget

    save_game(character_label, age_label, bar_graph)
