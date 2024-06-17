import os
import json
import zipfile
from persons.person import Person

def load_game_data_from_zip(zip_file):
    """
    Load game data from a zip file.

    Args:
        zip_file (str): The path to the zip file containing game data.

    Returns:
        dict: Game data loaded from the zip file as a dictionary.
    """
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Assuming main_character.json is always present in the root of the zip file
            main_character_file = [file for file in zip_ref.namelist() if file.endswith('main_character.json')][0]
            with zip_ref.open(main_character_file) as file:
                game_data = json.load(file)
        return game_data
    except FileNotFoundError:
        print(f"Error: Zip file '{zip_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{zip_file}'.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        return None

def load_game(character_label, age_label, bar_graph):
    saved_games_dir = os.path.join(os.getcwd(), 'run', 'saved_games')

    # List all zip files in the saved_games directory
    zip_files = [file for file in os.listdir(saved_games_dir) if file.endswith('.zip')]

    if not zip_files:
        print("No saved games found.")
        return

    # Assuming loading the first zip file found in the directory
    first_zip_file = os.path.join(saved_games_dir, zip_files[0])

    try:
        game_state = load_game_data_from_zip(first_zip_file)
        if game_state:
            print(f"Loaded game state from {first_zip_file}: {game_state}")

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
