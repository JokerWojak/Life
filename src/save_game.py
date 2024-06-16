import os
import json

def save_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'main_character.json')  # Save to root folder

    # Assuming the character label contains both first name and last name
    name_parts = character_label.text.split()
    if len(name_parts) == 2:
        first_name, last_name = name_parts
    else:
        first_name, last_name = "Unknown", "Unknown"

    save_data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': int(age_label.text.split(": ")[1]) if len(age_label.text.split(": ")) > 1 else 0,
        'traits': bar_graph.get_characteristics(),
        'parents': generate_parents_data()  # Save parents data
    }

    try:
        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=4)
        print(f"Saved game data to {filename}")
    except Exception as e:
        print(f"Error saving game data: {e}")

def generate_parents_data():
    # Generate parents data for testing
    father = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 50
    }
    mother = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 48
    }
    return {'father': father, 'mother': mother}
