from fastapi import APIRouter, UploadFile, Depends
from .service import FileService
from fastapi.responses import FileResponse
from .dependencies import file_service
from .schemas import BaseFile

router = APIRouter(prefix="")


@router.post("/docx2pdf")
async def convert_doc_to_pdf(
    file: UploadFile, file_service: FileService = Depends(file_service)
):
    
    file_s = BaseFile(name=file.filename, file_type_id=1, size=file.size)
    res = await file_service.convert_file(file_s, file)
    print(res)
    return FileResponse(f"{res[0]}", filename=f"{res[1]}.pdf")


@router.get("/docx2pdf")
async def get_doc_to_pdf(file_service: FileService = Depends(file_service)):
    res = await file_service.get_all_files()
    return res
