"""FastAPI example

Run with:
    uvicorn itbmeeting:app --reload --port 4447

API:
    http://127.0.0.1:4447

Interactive docs:
    http://127.0.0.1:4447/docs
    http://127.0.0.1:4447/redoc
    http://127.0.0.1:4447/openapi.json

Examples:
    http://127.0.0.1:4447/talks_by_speaker/?search_string=K%C3%B6nig'
"""
import uvicorn

from fastapi import FastAPI, Request, Response
from fastapi import FastAPI

from meeting_data import MEETING_DATA as DATA


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


# --- Talks ---
@api.get("/talks/", tags=["talks"])
def get_talks() -> Response:
    """Get talks of the ITB meeting."""
    return [t.to_dict() for t in DATA.talks.values()]


@api.get("/talks/{talk_id}", tags=["talks"])
def get_talk(talk_id: int) -> Response:
    """Get talk by id."""
    talk = DATA.talks[talk_id]
    if talk:
        talk = talk.to_dict()
    return talk


@api.get("/talks_by_speaker/", tags=["talks"])
def search_talks_by_speaker(search: str):
    """Get talk by speaker."""
    talks = []
    for talk in DATA.talks.values():
        if search.lower() in talk.name.lower():
            talks.append(talk)
    return [t.to_dict() for t in talks]


@api.get("/talks_by_group/", tags=["talks"])
def search_talks_by_speaker(search: str):
    """Get talk by group."""
    talks = []
    for talk in DATA.talks.values():
        person = DATA.persons.get(talk.person)
        if person and person.group:
            if search.lower() in person.group.lower():
                talks.append(talk)

    return [t.to_dict() for t in talks]


# --- People ---
@api.get("/persons/", tags=["people"])
def get_persons(alumni: bool = None) -> Response:
    """Get persons of the ITB meeting.
    The alumni parameter allows to filter for alumnis.
    """
    return [p.to_dict() for p in DATA.persons.values()]


@api.get("/persons/{person_id}", tags=["people"])
def get_person(person_id: int) -> Response:
    """Get person by id."""
    person = DATA.persons.get(person_id, None)
    if person:
        person = person.to_dict()
    return person


if __name__ == "__main__":
    # shell command: uvicorn itbmeeting:app --reload --port 4447
    uvicorn.run(
        "itbmeeting_api:api",
        host="localhost",
        port=4447,
        log_level="info",
        reload=True,
    )
