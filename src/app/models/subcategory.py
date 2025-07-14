from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.db.database import Base
from datetime import UTC, datetime

class SubCategory(Base):
    __tablename__ = "sub_category"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), index=True)
    subcategory: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(255), default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    # # Relationships
    # buildings: Mapped[list["Building"]] = relationship(back_populates="category")