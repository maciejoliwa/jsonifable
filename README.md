# JSONIFABLE

A very small library, consisting of one decorator, which adds **to_json** method, that converts your class to JSON.

### Installation:
```
pip install jsonifable
```

### Example:
```python
from jsonifable import Jsonifable

# it is not required to use dataclasses
# using them will just make this example shorter
from dataclasses import dataclass


@Jsonifable
@dataclass
class Person:

    name: str
    surname: str


person = Person("Avery", "Oliwa")
jsonified = person.to_json()
print(jsonified)
```

Will result in:
```{"name": "Avery", "surname": "Oliwa"}```

You can also use it with nested classes!
```python
from jsonifable import Jsonifable
from dataclasses import dataclass


@Jsonifable
@dataclass
class Animal:

    name: str
    species: str


# Notice how you're not required to add @Jsonifable decorator if you don't need the class instance to be manually converted using to_json
@dataclass
class Address:

    street_no: int
    street_name: str
    city: str


@Jsonifable
@dataclass
class Person:

    name: str
    surname: str
    address: Address
    animal: Animal


person = Person("Avery", "Oliwa", Address(20, "STREET", "London"), Animal("Guido", "dog"))
jsonified = person.to_json()
print(jsonified)
```

Will result in:
```{"name": "Avery", "surname": "Oliwa", "address": {"street_no": 20, "street_name": "STREET", "city": "London"}, "animal": {"name": "Guido", "species": "dog"}}```

It's because Jsonifable forces nested classes to be converted to JSON too.

### CAUTION:
Versions *0.0.1* and *0.0.2* do not work, do not install them, only install the newest version.

## TODO:
* Converting dictionaries which key's point at class instances
Trying to convert a dictionary, that is a property of a class like ```{ "a": Person("avery") }``` **won't** work.
* Converting nested lists within lists, same for tuples and sets