from fastapi import APIRouter, UploadFile, Depends
from .service import FileService
from fastapi.responses import FileResponse
from .dependencies import file_service
from .schemas import BaseFile
from starlette.background import BackgroundTask
from .backgroud_tasks import delete_files_after_send


router = APIRouter(prefix="")

@router.post("/doc2pdf")
async def convert_doc_to_pdf(
    file: UploadFile, file_service: FileService = Depends(file_service)
):
    
    file_s = BaseFile(name=file.filename, file_type_id=1, size=file.size)
    converted_pdf_file = await file_service.convert_file_doc_to_pdf(file_s, file)
    
    file_path = converted_pdf_file[0]
    filename = f"{converted_pdf_file[1]}.pdf"
    print(file_path)
    return FileResponse(path=file_path, 
                        filename=filename, 
                        background=BackgroundTask(delete_files_after_send, file_path))


