import uuid as uuid_pkg
from datetime import UTC, datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.core.db.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500), default="")
    address_detail: Mapped[str] = mapped_column(String(200), default="")
    latitude: Mapped[int] = mapped_column(String(20),  default="0", nullable=False)
    longtitude: Mapped[int] = mapped_column(String(20),  default="0", nullable=False)
    customer_id : Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    status : Mapped[int] = mapped_column(Integer, default="0", nullable=False)
    created_by : Mapped[int] = mapped_column(Integer,  default="0", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)

    buildings = relationship("Building", back_populates="project")