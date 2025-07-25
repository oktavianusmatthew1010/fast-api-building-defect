import uuid as uuid_pkg
from datetime import UTC, datetime
from sqlalchemy import Column, DateTime, ForeignKey, String,Integer,Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.core.db.database import Base
from ..models.building_level import BuildingLevel


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(500), default="")
    year_built: Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    building_type: Mapped[int]= mapped_column(Integer,  default="0", nullable=False)
    area_sq_meters: Mapped[float] = mapped_column(Float,  default="0.0", nullable=False)
    levels_count: Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    sides_count: Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    latitude: Mapped[float] = mapped_column(Float,  default="0.0", nullable=False)
    longitude: Mapped[int] = mapped_column(Float,  default="0.0", nullable=False)
    status_construction : Mapped[int] = mapped_column(Float,  default="0.0", nullable=False)
    construction_start_date : Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    construction_end_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    
    
    
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    levels = relationship("BuildingLevel", back_populates="building", cascade="all, delete-orphan")

    project = relationship("Project", back_populates="buildings")
    