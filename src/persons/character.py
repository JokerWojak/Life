import random
import uuid
import json


class Person:
    MAX_RECURSION_DEPTH = 12

    def __init__(self, depth=0):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each character
        self.gender = self.generate_gender()
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.age = random.randint(0, 10) if depth == 0 else random.randint(30, 60)  # Random age for root or parents
        self.parents = []  # List to store relationships with parents
        self.depth = depth

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
            return []

        father = Person(depth=current_depth + 1)
        mother = Person(depth=current_depth + 1)
        father.last_name = self.last_name  # Parents share the child's last name

        self.parents.append({
            'father': father.to_dict(),
            'mother': mother.to_dict()
        })

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
            'parents': self.parents
        }

    def save_to_json(self):
        filename = os.path.join(os.getcwd(), f"{self.id}.json")
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
