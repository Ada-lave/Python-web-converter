from utils.repository import SQLAlchemyRepository
from models.models import File

class FileRepository(SQLAlchemyRepository):
    model = File
