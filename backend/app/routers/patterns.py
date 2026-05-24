from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.pattern import Pattern
from app.schemas.pattern import PatternCreate, PatternResponse, PatternListResponse

router = APIRouter(prefix="/patterns", tags=["图鉴"])


@router.get("/categories")
def list_categories():
    return {"categories": ["全部", "动漫/IP", "萌宠动物", "美食饮品", "生活日常", "明星应援", "其他"]}


@router.get("/", response_model=PatternListResponse)
def list_patterns(
    category: str | None = Query(None, description="按分类筛选"),
    sort: str = Query("created_at", description="排序字段: created_at, likes, views"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    db: Session = Depends(get_db),
):
    query = db.query(Pattern)
    if category and category != "全部":
        query = query.filter(Pattern.category == category)

    sort_col = getattr(Pattern, sort, Pattern.created_at)
    total = query.count()
    items = query.order_by(sort_col.desc()).offset((page - 1) * page_size).limit(page_size).all()
    return PatternListResponse(total=total, items=items)


@router.get("/{pattern_id}", response_model=PatternResponse)
def get_pattern(pattern_id: int, db: Session = Depends(get_db)):
    pattern = db.query(Pattern).filter(Pattern.id == pattern_id).first()
    if not pattern:
        raise HTTPException(status_code=404, detail="图纸不存在")
    pattern.views = Pattern.views + 1
    db.commit()
    db.refresh(pattern)
    return pattern


@router.post("/", response_model=PatternResponse, status_code=201)
def create_pattern(body: PatternCreate, db: Session = Depends(get_db)):
    pattern = Pattern(**body.model_dump())
    db.add(pattern)
    db.commit()
    db.refresh(pattern)
    return pattern
