import random

from Data.data import Person
from faker import Faker

faker_ru = Faker()

def generate_person():
    yield Person(
        first_name = faker_ru.first_name(),
        last_name = faker_ru.last_name(),
        full_name = faker_ru.first_name() + " " + faker_ru.last_name(),
        email = faker_ru.email(),
        age = random.randint(1, 100),
        salary = random.randint(100, 100000),
        department = faker_ru.job(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address()
    )