from .doc2pdf.router import router as doc2pdf_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(doc2pdf_router, tags=["Docs & Pdf"])
