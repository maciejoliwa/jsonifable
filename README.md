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
```
{"name": "Avery", "surname": "Oliwa"}
```