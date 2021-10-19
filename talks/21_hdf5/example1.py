from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from rich import print


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


if __name__ == "__main__":

    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01 12:22',
        'friends': [1, 2, '3'],
    }

    # generate object and validate data
    user = User(**external_data)

    print(user.id)
    print(repr(user.signup_ts))
    print(user.friends)
    print(user.dict())
