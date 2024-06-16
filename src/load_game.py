import os
import json
from screens.widgets.bargraph import BarGraphWidget
from persons.person import Person

def load_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'run', 'main_character.json')  # Load from 'run' directory

    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
            character_label.text = f"{game_state.get('first_name', 'Unknown')} {game_state.get('last_name', 'Unknown')}"
            age_label.text = f"Age: {game_state.get('age', 0)}"
            bar_graph.update_characteristics(game_state.get('traits', {}))
            print(f"Loaded game data from {filename}")

            # Load parents data
            if 'parents' in game_state:
                load_parents_data(game_state['parents'])
            else:
                print("No parents data found in the game state.")

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
    except json.JSONDecodeError as je:
        print(f"Error decoding JSON from {filename}: {str(je)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

def load_parents_data(parents):
    father = parents.get('father', {})
    mother = parents.get('mother', {})
    print(f"Father: {father.get('first_name', 'Unknown')} {father.get('last_name', 'Unknown')}, Age: {father.get('age', 0)}")
    print(f"Mother: {mother.get('first_name', 'Unknown')} {mother.get('last_name', 'Unknown')}, Age: {mother.get('age', 0)}")

if __name__ == "__main__":
    # Example usage
    character_label = {"text": ""}
    age_label = {"text": ""}
    bar_graph = BarGraphWidget()

    load_game(character_label, age_label, bar_graph)
