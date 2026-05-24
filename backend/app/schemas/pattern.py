from datetime import datetime
from pydantic import BaseModel, model_validator
from app.core.config import settings


class PatternBase(BaseModel):
    title: str
    description: str | None = None
    category: str = "其他"


class PatternCreate(PatternBase):
    series: str | None = None
    colors: list[str] | None = None
    grid_data: dict | None = None
    width: int = 0
    height: int = 0


class PatternResponse(PatternBase):
    id: int
    series: str | None = None
    colors: list[str] | None = None
    image_url: str | None = None
    full_image_url: str | None = None
    width: int
    height: int
    beads_count: int
    views: int
    likes: int
    created_at: datetime

    model_config = {"from_attributes": True}

    @model_validator(mode="after")
    def prepend_base_url(self):
        base = settings.STATIC_BASE_URL.rstrip("/")
        if self.image_url and not self.image_url.startswith("http"):
            self.image_url = f"{base}{self.image_url}"
        if self.full_image_url and not self.full_image_url.startswith("http"):
            self.full_image_url = f"{base}{self.full_image_url}"
        return self


class PatternListResponse(BaseModel):
    total: int
    items: list[PatternResponse]
