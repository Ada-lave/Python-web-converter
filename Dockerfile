FROM python:3.11

WORKDIR /var/www/converter

ENV PORT=PORT

RUN apt-get update 
RUN apt-get install -y libreoffice-writer --fix-missing

CMD pip install -r req.txt && gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:$PORT