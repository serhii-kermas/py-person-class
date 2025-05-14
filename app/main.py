class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people.update({self.name : self})


def create_person_list(people: list) -> list:
    new_people = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_keys = person.keys()

        if "wife" in person_keys:
            new_person.wife = person["wife"]

        elif "husband" in person_keys:
            new_person.husband = person["husband"]

        new_people.append(new_person)

    for person in new_people:
        if person.wife is not None:
            person.wife = Person.people[person.wife]
        else:
            del person.wife
        if person.husband is not None:
            person.husband = Person.people[person.husband]
        else:
            del person.husband

    return new_people
