import os
import json
import random
from persons.person import Person
from persons.generate_parents import generate_parents


def save_game(character_label, age_label, bar_graph):
    main_character = generate_main_character(character_label, age_label, bar_graph)
    main_character_filename = save_person_to_json(main_character, "main_character")

    family_queue = main_character.generate_family()

    while family_queue:
        person = family_queue.pop(0)
        filename = save_person_to_json(person, person.id)
        print(f"Saved person to {filename}")
        family_queue.extend(person.generate_family(current_depth=person.depth))


def generate_main_character(character_label, age_label, bar_graph):
    # Generate main character data
    name_parts = character_label.text.split()
    if len(name_parts) == 2:
        first_name, last_name = name_parts
    else:
        first_name, last_name = "Unknown", "Unknown"

    main_character = Person()
    main_character.first_name = first_name
    main_character.last_name = last_name
    main_character.age = int(age_label.text.split(": ")[1]) if len(age_label.text.split(": ")) > 1 else 0
    main_character.traits = bar_graph.get_characteristics()

    # Save main character's parents data
    parents_data = generate_parents(main_character.age, 60)
    main_character.parents = parents_data

    return main_character


def save_person_to_json(person, filename):
    # Create a directory if it doesn't exist
    save_dir = os.path.join(os.getcwd(), 'run')
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
        'relationship': person.parents_relationships  # Example: Assuming parents_relationships is defined
    }

    # Save data to JSON file
    save_filename = os.path.join(save_dir, f"{filename}.json")
    with open(save_filename, 'w') as f:
        json.dump(data_to_save, f, indent=4)

    return save_filename


if __name__ == "__main__":
    # Example usage
    character_label = {"text": "John Smith"}  # Example character label
    age_label = {"text": "Age: 25"}  # Example age label
    bar_graph = {"get_characteristics": lambda: {"trait1": 0.8, "trait2": 0.6, "trait3": 0.4,
                                                 "trait4": 0.2}}  # Example bar graph

    save_game(character_label, age_label, bar_graph)
