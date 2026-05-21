"""
工作台 —— 图片上传与拼豆图纸生成接口

该模块负责：
1. 接收用户上传的原始图片
2. 调用图像处理算法，将图片转换为拼豆网格数据 (grid_data)
3. 返回生成结果（PNG 预览图 + 颜色网格 JSON）供前端渲染画布

当前版本为骨架实现，仅做接口定义和参数校验占位。
算法具体实现将在后续迭代中补充。
"""

import os
import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.config import settings
from app.core.database import get_db

router = APIRouter(prefix="/generator", tags=["工作台"])


class GenerateResponse(BaseModel):
    """拼豆图纸生成结果"""
    task_id: str
    preview_url: str
    grid_data: dict
    width: int
    height: int
    colors_used: list[str]
    beads_count: int


# ─── 辅助函数 ───────────────────────────────────────────────────────────────

def allowed_file(filename: str) -> bool:
    """检查文件扩展名是否允许"""
    ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def save_upload(file: UploadFile) -> str:
    """保存上传文件到本地，返回保存后的文件路径"""
    upload_dir = Path(settings.UPLOAD_DIR)
    upload_dir.mkdir(parents=True, exist_ok=True)

    ext = Path(file.filename).suffix if file.filename else ".png"
    saved_name = f"{uuid.uuid4().hex}{ext}"
    file_path = upload_dir / saved_name

    content = file.file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    file.file.seek(0)

    return str(file_path)


# ─── 路由 ───────────────────────────────────────────────────────────────────

@router.post("/upload", response_model=dict)
async def upload_image(
    file: UploadFile = File(..., description="要上传的图片，支持 JPG / PNG / WebP / BMP"),
):
    """上传原始图片（第一步）"""
    if not file.filename:
        raise HTTPException(status_code=400, detail="文件名不能为空")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="不支持的文件格式，仅支持 JPG / PNG / WebP / BMP")

    file_size_mb = file.size / (1024 * 1024) if file.size else 0
    if file_size_mb > settings.MAX_UPLOAD_SIZE_MB:
        raise HTTPException(status_code=413, detail=f"文件大小超过限制（{settings.MAX_UPLOAD_SIZE_MB}MB）")

    saved_path = save_upload(file)
    task_id = uuid.uuid4().hex

    return {
        "task_id": task_id,
        "filename": file.filename,
        "size_bytes": file.size,
        "message": "图片上传成功",
    }


@router.post("/generate", response_model=GenerateResponse)
async def generate_pattern(
    task_id: str = Form(..., description="上传接口返回的 task_id"),
    grid_size: int = Form(29, ge=10, le=100, description="拼豆网格尺寸（默认 29x29）"),
    color_count: int = Form(24, ge=4, le=64, description="最大颜色数"),
):
    """
    根据上传的图片生成拼豆图纸（第二步）

    算法流程（待实现）：
    1. 根据 task_id 读取已上传的原始图片
    2. 缩放至 grid_size × grid_size 像素
    3. 将每个像素量化到最近的标准拼豆颜色
    4. 生成网格 JSON 以及对应的预览 PNG
    5. 返回前端渲染所需的全部数据
    """
    # TODO: 实现图片像素化算法
    # 以下为骨架占位返回
    raise HTTPException(
        status_code=501,
        detail="图片转拼豆算法正在开发中，敬请期待！",
    )


@router.get("/colors", response_model=list[str])
async def get_bean_colors():
    """获取当前支持的标准拼豆颜色列表（十六进制色值）"""
    # TODO: 从配置/数据库中读取标准色板
    return [
        "#FFFFFF",  # 白色
        "#000000",  # 黑色
        "#FF0000",  # 红色
        "#00FF00",  # 绿色
        "#0000FF",  # 蓝色
        "#FFFF00",  # 黄色
        "#FFA500",  # 橙色
        "#800080",  # 紫色
        "#FFC0CB",  # 粉色
        "#A52A2A",  # 棕色
        "#808080",  # 灰色
        "#87CEEB",  # 天蓝
    ]
