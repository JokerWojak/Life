import os
import json
import zipfile
from persons.person import Person  # Assuming Person class is defined in persons/person.py

def load_game_data_from_zip(zip_file):
    """
    Load game data from a zip file.

    Args:
        zip_file (str): The path to the zip file containing game data.

    Returns:
        dict: Game data loaded from the zip file as a dictionary, or None if an error occurs.
    """
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # List all files in the zip for debugging
            print(f"Files in {zip_file}: {zip_ref.namelist()}")

            # Find main_character.json in the zip file
            main_character_files = [file for file in zip_ref.namelist() if file.endswith('main_character.json')]
            if not main_character_files:
                print(f"Error: No main_character.json found in {zip_file}")
                return None

            main_character_file = main_character_files[0]
            with zip_ref.open(main_character_file) as file:
                game_data = json.load(file)

        return game_data

    except FileNotFoundError:
        print(f"Error: Zip file '{zip_file}' not found.")
        return None

    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{main_character_file}' in {zip_file}.")
        return None

    except Exception as e:
        print(f"Unexpected error occurred while loading {zip_file}: {str(e)}")
        return None


def extract_main_character_info(game_data):
    """
    Extract main character information from the loaded game data.

    Args:
        game_data (dict): Loaded game data as a dictionary.

    Returns:
        dict: Dictionary containing main character information (first_name, last_name, age, traits).
              Returns None if 'main_character' key is missing in game_data.
    """
    try:
        # Ensure game_data is a dictionary
        if not isinstance(game_data, dict):
            raise ValueError("Game data must be a dictionary.")

        # Extract main character information
        main_character = game_data.get('main_character', None)
        if not main_character:
            print("Error: 'main_character' key not found in game data.")
            return None

        first_name = main_character.get('first_name', 'Unknown')
        last_name = main_character.get('last_name', 'Unknown')
        age = main_character.get('age', 0)
        traits = main_character.get('traits', {})

        return {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'traits': traits
        }

    except Exception as e:
        print(f"Error occurred during extraction of main character info: {str(e)}")
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

            # Extract main character information
            main_character_info = extract_main_character_info(game_state)
            if not main_character_info:
                print("Failed to extract main character information.")
                return

            # Update UI elements
            character_label.text = f"{main_character_info['first_name']} {main_character_info['last_name']}"
            age_label.text = f"Age: {main_character_info['age']}"
            bar_graph.update_characteristics(main_character_info['traits'])
            print(f"Updated UI elements: character_label={character_label.text}, age_label={age_label.text}")
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

# Example usage:
# You would typically call load_game with appropriate parameters for your UI setup
# For instance:
# character_label = Label()
# age_label = Label()
# bar_graph = BarGraph()
# load_game(character_label, age_label, bar_graph)
