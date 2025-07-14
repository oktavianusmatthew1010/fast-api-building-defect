from sqlalchemy import String, ForeignKey,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import UTC, datetime

from ..core.db.database import Base


class BuildingLevel(Base):
    __tablename__ = "building_level"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), index=True)
    level_number: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(255), default=None)
    primary_usage: Mapped[str] = mapped_column(String(50),default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

   