from sqlalchemy import Column, String, ForeignKey,DateTime,Float ,Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import UTC, datetime
from ..core.db.database import Base


class BuildingSide(Base):
    __tablename__ = "building_side"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(255), default=None)
    orientation_degrees: Mapped[float] = mapped_column(Float,  default="0.0", nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    building_id: Mapped[int]= mapped_column(Integer,  default="0", nullable=False)
    
    
    # # Relationships
    # buildings: Mapped[list["Building"]] = relationship(back_populates="category")