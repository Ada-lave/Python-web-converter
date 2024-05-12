import subprocess
from fastapi import UploadFile
from pathlib import Path
import aiofiles
from .converter import Converter

class Doc2Pdf(Converter):
    def __init__(self, file: UploadFile) -> None:
        self.file = file
        self.input_file = Path(f"files/{file.filename}")

    async def doc2pdf(self):
        await self.save_file()
        await self.convert_to("pdf")
        filename = Path(self.file.filename).stem
        res = f"{Path('files') / filename}"
        
        return [res, filename]
    
    async def pdf2doc(self):
        await self.save_file()
        await self.convert_to("docx")
        filename = Path(self.file.filename).stem
        res = f"{Path('files') / filename}"
        
        return [res, filename]