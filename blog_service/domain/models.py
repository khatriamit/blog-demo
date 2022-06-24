from pydantic import BaseModel
import typing
from datetime import datetime
from app import models as orm


class BlogPost(BaseModel):
    id_: typing.Optional[str]
    title: str
    heading: str
    body: str
    created_by: orm.User

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def blog_post_factory(
    title: str,
    heading: str,
    body: str,
    created_by: orm.User,
) -> BlogPost:
    return BlogPost(
        title=title,
        heading=heading,
        body=body,
        created_by=created_by,
    )
