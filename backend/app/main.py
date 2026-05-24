"""拼豆 PieceABean —— FastAPI 应用入口"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import engine, Base
from app.models import User, Pattern  # 注册模型到 Base.metadata
from app.routers import users, patterns, generator
from app.routers.admin import router as admin_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期：启动时创建数据库表（开发环境）"""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="拼豆图纸在线生成与分享平台",
    lifespan=lifespan,
)

# ─── 静态文件：图纸图片 ──────────────────────────────────────────────────────
patterns_dir = Path(r"D:\Desktop\pieceabean-data\patterns")
if patterns_dir.exists():
    app.mount("/static/patterns", StaticFiles(directory=str(patterns_dir)), name="patterns")

# ─── CORS 跨域配置 ──────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── 注册路由 ──────────────────────────────────────────────────────────────
app.include_router(users.router, prefix="/api/v1")
app.include_router(patterns.router, prefix="/api/v1")
app.include_router(generator.router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")


# ─── 根路径健康检查 ─────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": f"欢迎来到 {settings.APP_NAME} API", "version": "0.1.0"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
