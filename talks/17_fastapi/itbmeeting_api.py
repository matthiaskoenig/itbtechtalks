"""FastAPI example

documentation features
"""
from pathlib import Path
from typing import Optional, Dict, Any, List, Union

from dataclasses import dataclass
from fastapi import FastAPI
import uvicorn
import yaml

# -------------------------------------------------------------------------------------
# Data base/model
# -------------------------------------------------------------------------------------
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
    speakers: List[Person]
    alumnis: List[Person]
    talks: List[Talk]


def load_data() -> MeetingData:
    """Load meeting data."""
    db_path = Path(__file__).parent / "database"
    data = Dict[str, Union[Person, Talk]]

    for key in ["speakers", "alumnis", "talks"]:
        with open(db_path / f"{key}.yaml", "r") as f_yaml:
            data[key] = yaml.load(f_yaml)

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





@api.get("/api/examples", tags=["examples"])
def examples() -> Response:
    """Get examples for reports."""
    try:
        content = {
            "examples": [example["metadata"] for example in examples_info.values()]
        }
        return _render_json_content(content)

    except Exception as e:
        return _handle_error(e)


@api.get("/api/examples/{example_id}", tags=["examples"])
def example(example_id: str) -> Response:
    """Get specific example."""
    try:
        example = examples_info.get(example_id, None)
        content: Dict
        if example:
            source: Path = example["file"]  # type: ignore
            content = _content_for_source(source=source)
        else:
            content = {"error": f"example for id does not exist '{example_id}'"}

        return _render_json_content(content)
    except Exception as e:
        return _handle_error(e)



if __name__ == "__main__":
    # shell command: uvicorn itbmeeting:app --reload --port 4446
    uvicorn.run(
        "itbmeeting_api:app",
        host="localhost",
        port=4446,
        log_level="info",
        reload=True,
    )
