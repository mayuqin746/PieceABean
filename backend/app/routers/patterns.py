from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.pattern import PatternCreate, PatternResponse, PatternListResponse

router = APIRouter(prefix="/patterns", tags=["图鉴"])


@router.get("/categories")
def list_categories():
    """获取所有图纸分类"""
    categories = ["全部", "动物", "植物", "卡通", "食物", "几何", "节日", "其他"]
    return {"categories": categories}


@router.get("/", response_model=PatternListResponse)
def list_patterns(
    category: str | None = Query(None, description="按分类筛选"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    db: Session = Depends(get_db),
):
    """分页获取图纸列表，支持按分类筛选"""
    # TODO: 实现分页查询 + 分类筛选
    raise HTTPException(status_code=501, detail="图鉴列表接口尚未实现")


@router.get("/{pattern_id}", response_model=PatternResponse)
def get_pattern(pattern_id: int, db: Session = Depends(get_db)):
    """获取单个图纸详情"""
    # TODO: 按 ID 查询图纸，同时增加浏览量
    raise HTTPException(status_code=501, detail="图纸详情接口尚未实现")


@router.post("/", response_model=PatternResponse, status_code=201)
def create_pattern(body: PatternCreate, db: Session = Depends(get_db)):
    """创建新图纸"""
    # TODO: 保存图纸信息到数据库
    raise HTTPException(status_code=501, detail="创建图纸接口尚未实现")
