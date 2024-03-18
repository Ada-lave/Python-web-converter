from fastapi import FastAPI, UploadFile
from converter.converter import Converter
from fastapi.responses import FileResponse
from api_v1 import router
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)