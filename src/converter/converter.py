import subprocess
from fastapi import UploadFile
from pathlib import Path
import aiofiles


class Converter:
    def __init__(self, file: UploadFile) -> None:
        self.file = file
        self.input_file = Path(f"files/{file.filename}")
        self.output_file = Path(f"files/{file.filename}.pdf")

    async def save_file(self):

        async with aiofiles.open(self.input_file, "wb") as file:
            content = await self.file.read()
            await file.write(content)

    async def doc2pdf(self):
        await self.save_file()
        sub = subprocess.Popen(
            [
                "libreoffice",
                "--headless",
                "-convert-to",
                "pdf",
                f"{self.input_file}",
                "--outdir",
                "files/",
            ]
        )
        sub.wait()

        filename = Path(self.file.filename).stem
        res = f"{Path('files') / filename}.pdf"
        
        return [res, filename]
