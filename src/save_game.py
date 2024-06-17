import os
import json
import random
import zipfile
from persons.generate_main_character import generate_main_character
from persons.save_person import save_person_to_json

def save_game(character_label, age_label, bar_graph):
    """
    Save the main character and their family members recursively.

    Args:
        character_label (dict): Label for the main character.
        age_label (dict): Label for the age of the main character.
        bar_graph (BarGraphWidget): Example bar graph widget.

    """
    print("Starting save_game...")

    # Generate main character
    main_character = generate_main_character(character_label, age_label, bar_graph)

    # Create a directory to hold all saved game files
    save_dir = os.path.join(os.getcwd(), 'run', 'saved_games', f"{main_character.id}")
    os.makedirs(save_dir, exist_ok=True)

    # Save main character
    main_character_filename = save_person_to_json(main_character, os.path.join(save_dir, "main_character"))

    # Generate and save family members recursively
    family_queue = main_character.generate_family()

    while family_queue:
        person = family_queue.pop(0)
        filename = save_person_to_json(person, os.path.join(save_dir, person.id))
        print(f"Saved person to {filename}")
        family_queue.extend(person.generate_family(current_depth=person.depth))

    # Zip all saved JSON files into a single archive
    zip_filename = os.path.join(os.getcwd(), 'run', 'saved_games', f"{main_character.id}.zip")
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(save_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(save_dir, '..')))

    print(f"Game saved successfully to {zip_filename}!")

if __name__ == "__main__":
    # Example usage
    character_label = {"text": "John Smith"}  # Example character label
    age_label = {"text": "Age: 25"}  # Example age label
    bar_graph = BarGraphWidget()  # Example bar graph widget

    save_game(character_label, age_label, bar_graph)
