from datetime import datetime
from pydantic import BaseModel


class PatternBase(BaseModel):
    title: str
    description: str | None = None
    category: str = "其他"


class PatternCreate(PatternBase):
    grid_data: dict | None = None
    width: int = 0
    height: int = 0


class PatternResponse(PatternBase):
    id: int
    image_url: str | None = None
    width: int
    height: int
    beads_count: int
    views: int
    likes: int
    created_at: datetime

    model_config = {"from_attributes": True}


class PatternListResponse(BaseModel):
    total: int
    items: list[PatternResponse]
