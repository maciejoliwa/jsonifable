import typing as tp
import json

from jsonifable import Jsonifable
from enum import IntEnum


class Release:

    def __init__(self, release_type: int, name: str) -> None:
        self.release_type = release_type
        self.name = name


class Dependency:

    def __init__(self, name: str, version: str, release_type: tp.Optional[Release] = None) -> None:
        self.name = name
        self.version = version
        self.release = release_type


@Jsonifable
class Project:

    def __init__(self, name: str, id: int, author: str, description: str, **kwargs) -> None:
        self.name = name
        self.id = id
        self.author = author
        self.description = description
        self.data = kwargs


def test_class_kwargs() -> tp.NoReturn:
    project = Project("Jsonifable", 0, "Avery", "A funny library indeed", tags=[
                      "json", "python"], release="0.0.9")
    jsonified = json.loads(project.to_json())

    assert jsonified["data"]["release"] == "0.0.9" and len(
        jsonified["data"]["tags"]) == 2


def test_class_nested() -> tp.NoReturn:
    dep1 = Dependency("pytest", "7.0.1", Release(0, "FULL_RELEASE"))
    dep2 = Dependency("twine", "something")

    prj = Project("Jsonifable", 0, "Avery", "funi", deps=[dep1, dep2])

    jsonified = json.loads(prj.to_json())

    assert jsonified["data"]["deps"][0]["name"] == "pytest" and jsonified["data"]["deps"][0]["release"]["name"] == "FULL_RELEASE"
