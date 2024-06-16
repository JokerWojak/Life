import random
import uuid
import json
import os
from persons.person import Person


if __name__ == "__main__":
    # Create a root person (the child in this case)
    root_person = Person()
    root_person.generate_family()

    # Save root person
    root_filename = root_person.save_to_json()
    print(f"Saved root person to {root_filename}")

    # Save all family members recursively
    family_queue = root_person.generate_family()

    while family_queue:
        person = family_queue.pop(0)
        filename = person.save_to_json()
        print(f"Saved person to {filename}")
        family_queue.extend(person.generate_family(current_depth=person.depth))
