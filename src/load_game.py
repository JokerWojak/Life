import os
import json
from screens.widgets.bargraph import BarGraphWidget
from persons.person import Person


def load_game(character_label, age_label, bar_graph):
    filename = os.path.join(os.getcwd(), 'src', 'run', 'main_character.json')  # Correct path to 'main_character.json'

    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
            print(f"Loaded game state: {game_state}")

            # Extract character information
            first_name = game_state.get('first_name', 'Unknown')
            last_name = game_state.get('last_name', 'Unknown')
            age = game_state.get('age', 0)
            traits = game_state.get('traits', {})

            # Update UI elements
            character_label['text'] = f"{first_name} {last_name}"
            age_label['text'] = f"Age: {age}"
            bar_graph.update_characteristics(traits)
            print(f"Updated UI elements: character_label={character_label['text']}, age_label={age_label['text']}")
            print("UI elements updated successfully.")

            # Load parents data if available
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
    print(
        f"Father: {father.get('first_name', 'Unknown')} {father.get('last_name', 'Unknown')}, Age: {father.get('age', 0)}")
    print(
        f"Mother: {mother.get('first_name', 'Unknown')} {mother.get('last_name', 'Unknown')}, Age: {mother.get('age', 0)}")


if __name__ == "__main__":
    # Example usage (replace with actual UI components as needed)
    character_label = {"text": ""}  # Placeholder for UI label
    age_label = {"text": ""}  # Placeholder for UI label
    bar_graph = BarGraphWidget()  # Placeholder for UI widget

    load_game(character_label, age_label, bar_graph)
