from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    full_name: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None