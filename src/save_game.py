import os
import json
import datetime

# Function to ensure the directory exists
def ensure_directory_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory, exist_ok=True)
    else:
        print(f"Directory already exists: {directory}")

# Function to save data
def save_data(data, path):
    ensure_directory_exists(path)
    with open(path, 'w') as file:
        json.dump(data, file)
    print(f"Saved data to: {path}")

# Function to save game state
def save_game(name, age, bar_graph):
    # Define the save path
    save_path = '/Users/mac/PycharmProjects/Life/src/run/main_character.json'
    print(f"Preparing to save game data to {save_path}")

    # Example data to save
    main_character_data = {
        'id': 'bed8a47e-dda2-44a1-ad87-6fa44869b5bd',
        'first_name': name.split()[0] if name else 'Unknown',
        'last_name': name.split()[-1] if name else 'Unknown',
        'age': age,
        'traits': {},
        'money': 9240,
        'property': 'None',
        'relationship': [],
        'saved_at': datetime.datetime.now().isoformat()
    }

    # Save the main character data
    try:
        save_data(main_character_data, save_path)
        print("Game data saved successfully")
    except Exception as e:
        print(f"Error saving game data: {e}")

# Debug information about the current working directory and file structure
print(f"Current working directory: {os.getcwd()}")
print("Directory contents:")
for root, dirs, files in os.walk(os.getcwd()):
    level = root.replace(os.getcwd(), '').count(os.sep)
    indent = ' ' * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
