from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class File_type(Base):
    name: Mapped[str]


class File(Base):
    name: Mapped[str]
    size: Mapped[int]
    file_type_id: Mapped[int] = mapped_column(ForeignKey("file_types.id"))


class Conversion(Base):
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"))
    conversion_status_id: Mapped[int] = mapped_column(ForeignKey("conversion_statuses.id"))
    outfile_name: Mapped[str]
    time: Mapped[float]

class Conversion_status(Base):
    __tablename__ = "conversion_statuses"
    name: Mapped[str]