class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name : self})


def create_person_list(people: list) -> list:
    new_people = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if person.get("wife"):
            new_people[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            new_people[index].husband = Person.people[person["husband"]]
    return new_people
