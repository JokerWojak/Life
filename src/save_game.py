import os
import json
import random
from persons.person import Person
from persons.generate_parents import generate_parents

def save_game(character_label, age_label, bar_graph):
    print("Starting save_game...")
    main_character = generate_main_character(character_label, age_label, bar_graph)
    main_character_filename = save_person_to_json(main_character, "main_character")

    family_queue = main_character.generate_family()

    while family_queue:
        person = family_queue.pop(0)
        filename = save_person_to_json(person, person.id)
        print(f"Saved person to {filename}")
        family_queue.extend(person.generate_family(current_depth=person.depth))

def generate_main_character(character_label, age_label, bar_graph):
    print("Generating main character...")
    # Generate main character data
    if isinstance(character_label, dict) and "text" in character_label:
        name_parts = character_label["text"].split()
        if len(name_parts) == 2:
            first_name, last_name = name_parts
        else:
            first_name, last_name = "Unknown", "Unknown"
    else:
        first_name, last_name = "Unknown", "Unknown"

    main_character = Person()
    main_character.first_name = first_name
    main_character.last_name = last_name
    print(f"Main character name: {first_name} {last_name}")

    main_character.age = int(age_label["text"].split(": ")[1]) if isinstance(age_label, dict) and "text" in age_label and len(age_label["text"].split(": ")) > 1 else 0
    print(f"Main character age: {main_character.age}")

    # Check if bar_graph is callable and has a get_characteristics method
    if hasattr(bar_graph, "get_characteristics") and callable(getattr(bar_graph, "get_characteristics")):
        main_character.traits = bar_graph.get_characteristics()
    else:
        main_character.traits = {}
    print(f"Main character traits: {main_character.traits}")

    # Save main character's parents data
    parents_data = generate_parents(main_character.age, 60)
    main_character.parents = parents_data
    print(f"Main character parents: {parents_data}")

    return main_character

def save_person_to_json(person, filename):
    print(f"Saving person {person.id} to JSON...")
    # Create a directory "run" under the current working directory if it doesn't exist
    save_dir = os.path.join(os.getcwd(), 'run')
    os.makedirs(save_dir, exist_ok=True)

    if filename == "main_character":
        save_filename = os.path.join(save_dir, "main_character.json")
    else:
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
    print("Game saved successfully!")
