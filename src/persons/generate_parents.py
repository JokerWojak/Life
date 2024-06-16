import random
import os
from persons.person import Person


def generate_parents(child_age, max_parent_age):
    root_person = Person()
    root_person.age = child_age
    root_person.generate_family()

    family_queue = root_person.generate_family()

    parents_list = []

    while family_queue:
        person = family_queue.pop(0)
        if person.age <= max_parent_age:
            filename = person.save_to_json()
            parents_list.append(filename)
            family_queue.extend(person.generate_family(current_depth=person.depth))

    return parents_list


if __name__ == "__main__":
    child_age = int(input("Enter the age of the child: "))
    max_parent_age = int(input("Enter the maximum age of the parents to generate: "))

    parents_list = generate_parents(child_age, max_parent_age)
    if parents_list:
        print("Saved parent data to the following files:")
        for filename in parents_list:
            print(filename)
    else:
        print("No parent data generated.")
