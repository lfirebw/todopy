from pydantic import BaseModel
from uuid import UUID

class CollectionOut(BaseModel):
    unique_id: UUID
    name: str
    color: str

    class Config:
        orm_mode = True

class TaskOut(BaseModel):
    unique_id: UUID
    text: str
    description: str
    checked: bool
    collection: CollectionOut | None

    class Config:
        orm_mode = True