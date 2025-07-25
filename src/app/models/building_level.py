from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import UTC, datetime

from ..schemas.building import Building

from ..core.db.database import Base


class BuildingLevel(Base):
    __tablename__ = "building_level"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    building_id: Mapped[int] = mapped_column(Integer(), default=0)

    level_name: Mapped[str] = mapped_column(String(50), default=None)
    description: Mapped[str | None] = mapped_column(String(255), default=None)
    primary_usage: Mapped[str] = mapped_column(String(50),default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    

   