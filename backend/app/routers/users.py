from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserRegister, UserLogin, UserResponse, Token

router = APIRouter(prefix="/users", tags=["用户"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(body: UserRegister, db: Session = Depends(get_db)):
    """用户注册"""
    # TODO: 实现注册逻辑
    raise HTTPException(status_code=501, detail="注册功能尚未实现")


@router.post("/login", response_model=Token)
def login(body: UserLogin, db: Session = Depends(get_db)):
    """用户登录"""
    # TODO: 实现登录逻辑（验证密码、生成 JWT）
    raise HTTPException(status_code=501, detail="登录功能尚未实现")


@router.get("/me", response_model=UserResponse)
def get_current_user(db: Session = Depends(get_db)):
    """获取当前登录用户信息"""
    # TODO: 从 JWT 中解析用户 ID，查询并返回用户信息
    raise HTTPException(status_code=501, detail="用户信息接口尚未实现")


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """获取指定用户的公开信息"""
    # TODO: 按 ID 查询用户
    raise HTTPException(status_code=501, detail="用户信息接口尚未实现")
