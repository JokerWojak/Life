import os
import json

def load_main_character(character_label, age_label, bar_graph):
    save_dir = os.path.join(os.getcwd(), 'run')
    main_character_filename = os.path.join(save_dir, "main_character.json")

    if os.path.exists(main_character_filename):
        with open(main_character_filename, 'r') as f:
            data = json.load(f)

            character_label.text = f"Name: {data['first_name']} {data['last_name']}"
            age_label.text = f"Age: {data['age']}"

            # Update bar graph or any other widgets with traits data
            # Assuming bar_graph.update_characteristics(data['traits']) is defined
            if 'traits' in data:
                bar_graph.update_characteristics(data['traits'])
            else:
                bar_graph.update_characteristics({})  # Handle case where traits are missing

        print(f"Loaded main character from {main_character_filename}")
    else:
        print(f"Main character file {main_character_filename} does not exist. Unable to load.")

    return character_label, age_label, bar_graph
