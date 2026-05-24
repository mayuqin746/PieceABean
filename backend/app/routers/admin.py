"""管理后台 —— 图纸上传接口（仅限已登录管理员访问）"""
import uuid
from pathlib import Path
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.pattern import Pattern
from app.models.user import User
from app.schemas.pattern import PatternResponse

router = APIRouter(prefix="/admin", tags=["管理后台"])

DATA_DIR = Path(r"D:\Desktop\pieceabean-data\patterns")
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


@router.post("/upload", response_model=PatternResponse, status_code=201)
async def upload_pattern(
    file: UploadFile = File(...),
    title: str = Form(...),
    category: str = Form(...),
    series: str = Form(default=""),
    colors: str = Form(default="[]"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ext = Path(file.filename).suffix.lower() if file.filename else ".png"
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="仅支持 PNG / JPG / WebP 格式")

    file_size_mb = (file.size or 0) / (1024 * 1024)
    if file_size_mb > 10:
        raise HTTPException(status_code=413, detail="文件超过 10MB 限制")

    import json
    try:
        colors_list = json.loads(colors) if colors else []
    except json.JSONDecodeError:
        colors_list = []

    saved_name = f"{uuid.uuid4().hex}{ext}"

    thumb_dir = DATA_DIR / "thumbnail"
    full_dir = DATA_DIR / "full"
    thumb_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)

    content = await file.read()

    thumb_path = thumb_dir / saved_name
    with open(thumb_path, "wb") as f:
        f.write(content)

    full_path = full_dir / saved_name
    with open(full_path, "wb") as f:
        f.write(content)

    pattern = Pattern(
        title=title,
        category=category,
        series=series or None,
        colors=colors_list or None,
        image_url=f"/static/patterns/thumbnail/{saved_name}",
        full_image_url=f"/static/patterns/full/{saved_name}",
    )
    db.add(pattern)
    db.commit()
    db.refresh(pattern)
    return pattern
