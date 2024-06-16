import os
import json
from screens.widgets.bargraph import BarGraphWidget

def load_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'main_character.json')

    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
            first_name = game_state.get('first_name', 'Unknown')
            last_name = game_state.get('last_name', 'Unknown')
            character_label.text = f"{first_name} {last_name}"
            age_label.text = f"{game_state.get('age', 0)}"
            if 'traits' in game_state:
                bar_graph.update_characteristics(game_state['traits'])
            print(f"Loaded game data from {filename}")
    except FileNotFoundError:
        print(f"No saved game data found at {filename}")
    except json.JSONDecodeError as je:
        print(f"Error decoding JSON from {filename}: {str(je)}")
