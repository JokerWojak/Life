import os
import json
from screens.widgets.bargraph import BarGraphWidget

def save_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'main_character.json')  # Save to root folder

    first_name, last_name = character_label.text.split()
    age_text = age_label.text

    # Extract age from label safely
    if "Age: " in age_text:
        try:
            age = int(age_text.split(": ")[1])
        except (IndexError, ValueError):
            age = 0  # Default age if parsing fails
    else:
        age = 0  # Default age if label text is not in the expected format

    save_data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'traits': bar_graph.get_characteristics()
    }

    try:
        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=4)
        print(f"Saved game data to {filename}")
    except Exception as e:
        print(f"Error saving game data: {e}")
