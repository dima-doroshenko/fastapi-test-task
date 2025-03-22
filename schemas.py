from datetime import date, datetime

from pydantic import (
    BaseModel,
    Field,
    field_validator,
)


class TaskCreate(BaseModel):
    title: str = Field(max_length=200)
    description: str = Field(max_length=5000)
    deadline: str

    @field_validator("deadline")
    def deadline_validator(cls, value: str) -> str:
        date_ = datetime.strptime(value, "%d-%m-%Y").date()
        if date_ <= date.today():
            raise ValueError("The date must be in the future")
        return value
    
class TaskGet(TaskCreate):
    id: int