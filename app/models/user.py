from app.core.db_async import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Boolean, String, Text


class user(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    role: Mapped[str] = mapped_column(String(20))
    isActive: Mapped[bool] = mapped_column(default=True)
    password: Mapped[str] = mapped_column()
