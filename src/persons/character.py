import random
import uuid

class Person:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each character
        self.gender = self.generate_gender()
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()

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
