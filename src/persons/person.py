import random
import uuid
import json
import os
import logging  # Step 1: Import the logging module

# Step 2: Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Person:
    MAX_RECURSION_DEPTH = 3

    def __init__(self, depth=0):
        self.id = str(uuid.uuid4())
        self.gender = self.generate_gender()
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.age = random.randint(0, 0) if depth == 0 else random.randint(30, 60)
        self.parents = []
        self.parents_relationships = []
        self.traits = {}
        self.depth = depth

        logging.debug(f'Initialized Person object: {self}')

    def generate_gender(self):
        return random.choice(["Male", "Female"])

    def generate_first_name(self):
        while True:
            if self.gender == "Male":
                names_file = "male_names.txt"
            else:
                names_file = "female_names.txt"

            names_path = os.path.join(os.getcwd(), "assets", names_file)
            with open(names_path, 'r') as f:
                names_list = [name.strip() for name in f.readlines()]
            first_name = random.choice(names_list)

            if first_name != "Unknown":
                logging.debug(f'Generated first name: {first_name}')
                return first_name

    def generate_last_name(self):
        while True:
            names_file = "last_names.txt"
            names_path = os.path.join(os.getcwd(), "assets", names_file)
            with open(names_path, 'r') as f:
                names_list = [name.strip() for name in f.readlines()]
            last_name = random.choice(names_list)

            if last_name != "Unknown":
                logging.debug(f'Generated last name: {last_name}')
                return last_name

    def create_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        logging.debug(f'Created full name: {full_name}')
        return full_name

    def generate_family(self, current_depth=0):
        if current_depth >= Person.MAX_RECURSION_DEPTH:
            return []

        father = Person(depth=current_depth + 1)
        mother = Person(depth=current_depth + 1)
        father.last_name = self.last_name

        self.parents.append({
            'father': father.to_dict(),
            'mother': mother.to_dict()
        })

        self.parents_relationships.append(f"{father.first_name} & {mother.first_name}")

        logging.debug(f'Generated family for {self.first_name}: Father: {father}, Mother: {mother}')

        father.generate_family(current_depth + 1)
        mother.generate_family(current_depth + 1)

        return [father, mother]

    def to_dict(self):
        return {
            'id': self.id,
            'gender': self.gender,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'parents': self.parents,
            'traits': self.traits
        }

    def save_to_json(self):
        filename = os.path.join(os.getcwd(), f"{self.id}.json")
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
        logging.info(f'Saved Person object to JSON file: {filename}')
        return filename

    @classmethod
    def from_dict(cls, data):
        person = cls()
        person.id = data.get('id', str(uuid.uuid4()))
        person.gender = data.get('gender', 'Male')
        person.first_name = data.get('first_name', 'Unknown')
        person.last_name = data.get('last_name', 'Unknown')
        person.age = data.get('age', 0)
        person.parents = data.get('parents', [])
        person.traits = data.get('traits', {})
        logging.debug(f'Created Person object from dictionary: {person}')
        return person

    def get_parents_relationships(self):
        return self.parents_relationships

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"


# Example usage:
if __name__ == "__main__":
    logging.debug("Starting the program")
    person = Person()
    person.create_full_name()
    person.generate_family()
    person.save_to_json()
    logging.debug("Program completed successfully")
