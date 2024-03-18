from converter.converter import Converter


# async def convert_to_pdf(file):
#     conv = Converter(file=file)
#     res = await conv.doc2pdf()

#     return res
from fastapi import UploadFile
from utils.repository import AbstractRepository
from .schemas import BaseFile


class FileService:
    def __init__(self, file_repo: AbstractRepository):
        self.file_repo = file_repo()

    async def convert_file(self, file: BaseFile, _file: UploadFile):
        conv = Converter(file=_file)
        res = await conv.doc2pdf()
        file = await self.file_repo.add_one(file.model_dump())
        return res
    
    async def get_all_files(self):
        return await self.file_repo.find_all()
