


from sqlmodel import Field
from app.models.base_models.Base import TableBase

class TodoBase(TableBase):
    text: str = Field(
        nullable=False,
        unique=True,
        index=True,
        description="用户名,系统内唯一"
    )
    completed: bool = Field(
        default=False,
        description="是否完成"
    )