import typing as tp
import json

from jsonifable import Jsonifable
from dataclasses import dataclass


@Jsonifable
@dataclass
class Person:

    name: str
    surname: str


@Jsonifable
@dataclass
class Repository:

    name: str
    watchers: tp.Sequence[Person]
    starred_by: tp.Sequence[Person]


def test_dataclasses_simple() -> tp.NoReturn:
    person = Person("Avery", "Olive")
    jsonified = json.loads(person.to_json())

    assert jsonified["name"] == "Avery" and jsonified["surname"] == "Olive"


def test_dataclasses_nested() -> tp.NoReturn:
    rep = Repository("Jsonifable", [Person("Avery", "Olive")], [])
    jsonified = json.loads(rep.to_json())

    assert len(jsonified["starred_by"]) == 0 and len(
        jsonified["watchers"]) == 1
