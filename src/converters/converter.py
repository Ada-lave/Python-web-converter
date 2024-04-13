import subprocess
from fastapi import UploadFile
from pathlib import Path
import aiofiles


class Converter:
    async def save_file(self):
        async with aiofiles.open(self.input_file, "wb") as file:
            content = await self.file.read()
            await file.write(content)

    async def convert_to(self, format: str):
        sub = subprocess.Popen(
            [
                "libreoffice",
                "--headless",
                "-convert-to",
                format,
                f"{self.input_file}",
                "--outdir",
                "files/",
            ]
        )
        sub.wait()
    
