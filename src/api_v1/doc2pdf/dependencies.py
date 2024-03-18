from .repo import FileRepository
from .service import FileService


def file_service():
    return FileService(FileRepository)
