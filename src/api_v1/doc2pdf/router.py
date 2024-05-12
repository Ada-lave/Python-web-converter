from fastapi import APIRouter, UploadFile, Depends
from .service import FileService
from .dependencies import file_service
from .schemas import BaseFile
from fastapi import BackgroundTasks
from .backgroud_tasks import delete_file_after_send

router = APIRouter(prefix="")

@router.post("/doc2pdf")
async def convert_doc_to_pdf(
    file: UploadFile,
    backgroud_tasks: BackgroundTasks,
    file_service: FileService = Depends(file_service)
):
    
    file_s = BaseFile(name=file.filename, file_type_id=1, size=file.size)
    converted_pdf_file_data = await file_service.convert_file_doc_to_pdf(file_s, file)   
    backgroud_tasks.add_task(delete_file_after_send, f"{converted_pdf_file_data[0]}.pdf") 
    return await file_service.file_response(converted_pdf_file_data, "pdf")
    
#test

@router.post("/pdf2doc")
async def convert_pdf_to_docx(
    file: UploadFile, 
    backgroud_tasks: BackgroundTasks,
    file_service: FileService = Depends(file_service),
):
    converted_doc_file = await file_service.convert_pdf_file_to_doc(file)
    return await file_service.file_response(converted_doc_file, "docx")
    
    
