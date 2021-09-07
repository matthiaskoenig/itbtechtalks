"""FastAPI example

documentation features
"""
from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from dataclasses import dataclass
import yaml
from rich import print

import uvicorn

from fastapi import FastAPI, Request, Response
from fastapi import FastAPI


# -------------------------------------------------------------------------------------
# Data base/model
# -------------------------------------------------------------------------------------
from yaml import FullLoader


@dataclass
class Person:
    name: str
    group: str


@dataclass
class Talk:
    name: str
    date: str
    title: str
    slides: bool


@dataclass
class MeetingData:
    speakers: Dict[int, Person]
    alumnis: Dict[int, Person]
    talks: Dict[str, Talk]


def load_data() -> MeetingData:
    """Load meeting data."""
    db_path = Path(__file__).parent / "database"
    data: Dict[str, Union[Person, Talk]] = {}

    for key in ["speakers", "alumnis", "talks"]:
        with open(db_path / f"{key}.yaml", "r") as f_yaml:
            _data = yaml.load(f_yaml, Loader=FullLoader)[key]

            # add ids for lookup
            clean_data: Dict = {}
            for k, item in enumerate(_data):
                clean_data[k] = {
                    "id": k,
                    **item
                }

            data[key] = clean_data

    return MeetingData(**data)


MEETING_DATA = load_data()
print(MEETING_DATA)

# -------------------------------------------------------------------------------------
# API
# -------------------------------------------------------------------------------------



description = """
# ITB meeting information

For more details and future schedule see
https://github.com/matthiaskoenig/itbmeeting

For code see
https://github.com/matthiaskoenig/itbtechtalks
"""

api = FastAPI(
    title="TechTalk",
    description="TechTalkAPI",
    version="0.1.0",
    terms_of_service="https://github.com/matthiaskoenig/sbmlutils/blob/develop/sbml4humans/privacy_notice.md",
    contact={
        "name": "Matthias König",
        "url": "https://livermetabolism.com",
        "email": "konigmatt@googlemail.com",
    },
    license_info={
        "name": "LGPLv3",
        "url": "http://opensource.org/licenses/LGPL-3.0",
    },
    openapi_tags=[
        {
            "name": "people",
            "description": "Information about speakers and alumnis.",
        },
        {
            "name": "talks",
            "description": "Information about talks.",
        },
    ]
)


@api.get("/speakers/", tags=["people"])
def get_speakers() -> Response:
    """Get speakers of the ITB meeting."""
    return MEETING_DATA.speakers


@api.get("/speakers/{speaker_id}", tags=["people"])
def get_speaker(speaker_id: int) -> Response:
    """Get speaker by id."""
    return MEETING_DATA.speakers[speaker_id]


@api.get("/alumnis/", tags=["people"])
def get_alumnis() -> Response:
    """Get alumnis of the ITB meeting."""
    return MEETING_DATA.alumnis


@api.get("/alumni/{alumni_id}", tags=["people"])
def get_alumni(alumni_id: int) -> Response:
    """Get alumni by id."""
    return MEETING_DATA.alumnis[alumni_id]


@api.get("/talks/", tags=["talks"])
def get_talks() -> Response:
    """Get talks of the ITB meeting."""
    return MEETING_DATA.talks


@api.get("/talks/{talk_id}", tags=["talks"])
def get_alumni(talk_id: int) -> Response:
    """Get talk by id."""
    return MEETING_DATA.talks[talk_id]

# talk_search; person_search


if __name__ == "__main__":
    # shell command: uvicorn itbmeeting:app --reload --port 4446
    uvicorn.run(
        "itbmeeting_api:api",
        host="localhost",
        port=4446,
        log_level="info",
        reload=True,
    )
