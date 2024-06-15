import random
import uuid
import json


class Person:
    MAX_RECURSION_DEPTH = 12

    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each character
        self.gender = self.generate_gender()
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.age = 0  # Initialize age to 0 upon creation
        self.parents = []  # List to store relationships with parents

    def generate_gender(self):
        return random.choice(["Male", "Female"])

    def generate_first_name(self):
        if self.gender == "Male":
            return random.choice(["John", "Alex", "Michael", "David"])
        else:
            return random.choice(["Jane", "Emily", "Sarah", "Anna"])

    def generate_last_name(self):
        return random.choice(["Smith", "Doe", "Brown", "Johnson"])

    def create_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def generate_family(self, current_depth=0):
        if current_depth >= Person.MAX_RECURSION_DEPTH:
            return

        father = Person()
        mother = Person()
        father.age = random.randint(30, 60)
        mother.age = random.randint(30, 55)
        father.first_name = random.choice(["John", "Michael", "David"])
        mother.first_name = random.choice(["Emily", "Anna", "Sarah"])
        father.last_name = self.last_name
        mother.last_name = self.last_name
        self.parents.append({
            'father': father.create_full_name(),
            'mother': mother.create_full_name()
        })

        father.generate_family(current_depth + 1)
        mother.generate_family(current_depth + 1)

    def to_dict(self):
        return {
            'id': self.id,
            'gender': self.gender,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'parents': self.parents
        }

    def save_to_json(self):
        filename = f"{self.id}.json"
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
        return filename

    @classmethod
    def from_dict(cls, data):
        person = cls()
        person.id = data.get('id', str(uuid.uuid4()))
        person.gender = data.get('gender', 'Male')
        person.first_name = data.get('first_name', '')
        person.last_name = data.get('last_name', '')
        person.age = data.get('age', 0)
        person.parents = data.get('parents', [])
        return person

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"


if __name__ == "__main__":
    child = Person()
    child.generate_family()

    # Save child and parents to separate JSON files
    child_filename = child.save_to_json()
    print(f"Saved child to {child_filename}")

    for parent_dict in child.parents:
        father_name = parent_dict['father']
        mother_name = parent_dict['mother']

        # Extract first names for parent IDs
        parent_id = f"{father_name.split()[0]}_{mother_name.split()[0]}"

        # Create parent instance
        parent = Person()
        parent.first_name = father_name
        parent.last_name = child.last_name
        parent_filename = parent.save_to_json()
        print(f"Saved parent to {parent_filename}")
