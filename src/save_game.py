import os
import json
from screens.widgets.bargraph import BarGraphWidget

def save_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'main_character.json')  # Save to root folder

    first_name, last_name = character_label.text.split()
    save_data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': int(age_label.text.split(": ")[1]),  # Extract age from label
        'traits': bar_graph.get_characteristics()
    }

    try:
        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=4)
        print(f"Saved game data to {filename}")
    except Exception as e:
        print(f"Error saving game data: {e}")
