"""Prepare ITB meeting data for API."""
from pathlib import Path
from typing import Dict, Union

import yaml
from yaml import FullLoader
from dataclasses import dataclass


@dataclass
class Person:
    id: int
    name: str
    group: str
    alumni: bool

    def to_dict(self):
        """JSON conversion."""
        return self.__dict__


@dataclass
class Talk:
    id: int
    person: int
    name: str
    date: str
    title: str
    slides: bool

    def to_dict(self):
        """JSON conversion."""
        return self.__dict__


@dataclass
class MeetingData:
    persons: Dict[int, Person]
    talks: Dict[str, Talk]


def load_data() -> MeetingData:
    """Load meeting data."""
    db_path = Path(__file__).parent / "database"
    data: Dict[str, Union[Person, Talk]] = {}

    _data: Dict = {}
    for key in ["speakers", "alumnis", "talks"]:
        with open(db_path / f"{key}.yaml", "r") as f_yaml:
            _data[key] = yaml.load(f_yaml, Loader=FullLoader)[key]

    # set alumni flag
    alumnis = _data["alumnis"]
    for p in alumnis:
        p["alumni"] = True
    speakers = _data["speakers"]
    for p in speakers:
        p["alumni"] = False

    # add speakers id
    persons = speakers + alumnis
    persons_dict = {}
    for k, item in enumerate(persons):
        # remove unnecessary fields
        for field in ["location", "web"]:
            if field in item:
                del item[field]

        persons_dict[k] = Person(**{
            "id": k,
            **item
        })

    # add talks id
    talks = _data["talks"]
    talks_dict = {}
    for k, talk in enumerate(talks):
        person = None
        for p in persons_dict.values():
            # match via person name
            if p.name == talk["name"]:
                person = p.id

        talks_dict[k] = Talk(**{
            "id": k,
            "person": person,
            **talk,
        })

    return MeetingData(
        persons=persons_dict, talks=talks_dict
    )

MEETING_DATA = load_data()

if __name__ == "__main__":
    from pprint import pprint
    pprint(MEETING_DATA)

