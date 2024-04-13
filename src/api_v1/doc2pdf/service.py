from converters.converter import Converter
from fastapi import UploadFile
from utils.repository import AbstractRepository
from .schemas import BaseFile
from converters.doc2pdf import Doc2Pdf

class FileService:
    def __init__(self, file_repo: AbstractRepository):
        self.file_repo = file_repo()

    async def convert_file_doc_to_pdf(self, file: BaseFile, _file: UploadFile):
        doc_converter = Doc2Pdf(file=_file)
        res = await doc_converter.doc2pdf()
        file = await self.file_repo.add_one(file.model_dump())
        return res
    
    async def get_all_files(self):
        return await self.file_repo.find_all()
