import random
from persons.person import Person
from persons.generate_parents import generate_parents

def generate_main_character(character_label, age_label, bar_graph):
    print("Generating main character...")

    # Extract first name and last name from character_label if available
    if isinstance(character_label, dict) and "text" in character_label:
        name_parts = character_label["text"].split()
        if len(name_parts) == 2:
            first_name, last_name = name_parts
        else:
            first_name, last_name = "Unknown", "Unknown"
    else:
        first_name, last_name = "Unknown", "Unknown"

    main_character = Person()
    main_character.first_name = first_name
    main_character.last_name = last_name
    print(f"Main character name: {first_name} {last_name}")

    # Extract age from age_label if available
    main_character.age = int(age_label["text"].split(": ")[1]) if isinstance(age_label,
                                                                             dict) and "text" in age_label and len(
        age_label["text"].split(": ")) > 1 else 0
    print(f"Main character age: {main_character.age}")

    # Check if bar_graph is callable and has a get_characteristics method
    if hasattr(bar_graph, "get_characteristics") and callable(getattr(bar_graph, "get_characteristics")):
        main_character.traits = bar_graph.get_characteristics()
    else:
        main_character.traits = {}
    print(f"Main character traits: {main_character.traits}")

    # Generate and save main character's parents data
    parents_data = generate_parents(main_character.age, 60)
    main_character.parents = parents_data
    print(f"Main character parents: {parents_data}")

    return main_character
